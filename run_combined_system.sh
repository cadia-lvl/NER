#!/bin/bash

rm output/*

cp config.ini CRF/config.ini
cp CRF-train-config.ini CRF/CRF-train-config.ini
nerc_model=$(awk -F ":" '/ixa-pipe-nerc-model/ {print $2}' config.ini)
nerc_executable=$(awk -F ":" '/ixa-pipe-nerc-executable/ {print $2}' config.ini)
echo $nerc_model
echo $nerc_executable
echo $1
gold_path=$(awk -F ":" '/gold_path/ {print $2}' config.ini)
#
current_dir=$(pwd)
tmpdir="/output/CRF-input"
write_address="$current_dir$tmpdir"
#python3 scripts/get_POS_tags_from_gold.py $1 $gold_path $write_address
CRF_input_address="$current_dir/output/CRF-input-final"
CRF_output="$current_dir/output/CRF"
#python3 CRF/convert_to_CRF_format.py $write_address $CRF_input_address
#python3 CRF/run_crf.py $CRF_input_address $CRF_output
#
rm output/CRF-input output/CRF-input-final

cp neuro_ner output/neuro_ner

./scripts/run_agerri_model.sh $nerc_model $1 $nerc_executable
java -jar CombiTagger/dist/CombiTagger.jar -t output/neuro_ner output/ixa-pipe output/CRF  -o output/combitagger-output/
