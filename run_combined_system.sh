#!/bin/bash

rm output/*
#

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
##
rm output/CRF-input output/CRF-input-final
#
cp neuro_ner output/neuro_ner
#
./scripts/run_agerri_model.sh $nerc_model $1 $nerc_executable
cd CombiTagger
java -jar dist/CombiTagger.jar -t $current_dir/output/neuro_ner $current_dir/output/ixa-pipe $current_dir/output/CRF  -o $current_dir/output/combitagger-output/
cd - > /dev/null 2>&1
awk -v OFS='\t' 'NR>1{ print $1, $NF }' output/combitagger-output > output/combitagger
rm output/combitagger-output