#!/bin/bash

rm output/*
#
rm -r NeuroNER-input/*

mkdir NeuroNER-input
sed 's/\t/ /g' $1 > NeuroNER-input/deploy.txt
neuroner
cp NeuroNER-output/*/000_deploy.txt output/neuro_ner.raw
rm -r NeuroNER-output/*
python3 scripts/convert_neuroner_to_conll.py output/neuro_ner.raw output/neuro_ner
rm output/neuro_ner.raw

nerc_model=$(awk -F ":" '/ixa-pipe-nerc-model/ {print $2}' config.ini)
nerc_executable=$(awk -F ":" '/ixa-pipe-nerc-executable/ {print $2}' config.ini)

gold_path=$(awk -F ":" '/gold_path/ {print $2}' config.ini)
##
current_dir=$(pwd)
tmpdir="output/CRF-input"
write_address="$current_dir$tmpdir"
python3 scripts/get_POS_tags_from_gold.py $1 $gold_path output/CRF-input
CRF_input_address=output/CRF-input-final
CRF_output=output/CRF
python3 CRF/convert_to_CRF_format.py output/CRF-input $CRF_input_address
python3 CRF/run_crf.py $CRF_input_address $CRF_output

rm output/CRF-input output/CRF-input-final
#
#cp neuro_ner output/neuro_ner
#
./scripts/run_agerri_model.sh $nerc_model $1 $nerc_executable
cd CombiTagger
java -jar dist/CombiTagger.jar -t $current_dir/output/neuro_ner $current_dir/output/ixa-pipe $current_dir/output/CRF  -o $current_dir/output/combitagger-output/
cd - > /dev/null 2>&1
awk -v OFS='\t' 'NR>1{ print $1, $NF }' output/combitagger-output > output/combitagger
rm output/combitagger-output
python3 scripts/createCoNLLEvaluationOutput.py output/ $1
tmp=$(ls eval/ | wc -w)
session_no=$(expr $tmp - 1)
mkdir eval/$session_no/results
perl scripts/conlleval.pl < eval/$session_no/CRF > eval/$session_no/results/CRF
perl scripts/conlleval.pl < eval/$session_no/ixa-pipe > eval/$session_no/results/ixa-pipe
perl scripts/conlleval.pl < eval/$session_no/neuro_ner > eval/$session_no/results/neuro_ner
perl scripts/conlleval.pl < eval/$session_no/combitagger > eval/$session_no/results/combitagger

echo "CRF results"
cat eval/$session_no/results/CRF
echo "ixa-pipe results"
cat eval/$session_no/results/ixa-pipe
echo "NeuroNER results"
cat eval/$session_no/results/neuro_ner
echo "CombiTagger results"
cat eval/$session_no/results/combitagger