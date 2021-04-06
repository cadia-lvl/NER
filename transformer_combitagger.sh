mkdir bert_outputs
cp saved_test_outputs/phase2/electra-small.txt bert_outputs/.
cp saved_test_outputs/phase2/electra-base.txt bert_outputs/.
cp saved_test_outputs/phase2/multilingual-bert.txt bert_outputs/.
python3 scripts/remove_added_lines.py test bert_outputs/electra-small.txt
python3 scripts/remove_added_lines.py test bert_outputs/electra-base.txt
python3 scripts/remove_added_lines.py test bert_outputs/multilingual-bert.txt
current_dir=$(pwd)
cd CombiTagger

#$current_dir/bert_outputs/multilingual-bert.txt
#$current_dir/bert_outputs/electra-base.txt
java -jar dist/CombiTagger.jar -t $current_dir/bert_outputs/electra-base.txt $current_dir/bert_outputs/multilingual-bert.txt  $current_dir/bert_outputs/electra-small.txt -o $current_dir/tempout
#$current_dir/bert_outputs/electra-small.txt
cd - > /dev/null 2>&1
awk -v OFS='\t' 'NR>1{ print $1, $NF}' tempout > bert_outputs/combitagger.txt
rm tempout
python3 scripts/createCoNLLEvaluationOutput.py bert_outputs/ test
tmp=$(ls eval/ | wc -w)
session_no=$(expr $tmp - 1)

python3 scripts/known_unknown_filtering.py /mnt/c/Users/auzi/verkefni_phase2/NER_GOGN/1000K test bert_outputs/multilingual-bert.txt $current_dir/bert_outputs UseValidation
python3 scripts/known_unknown_filtering.py /mnt/c/Users/auzi/verkefni_phase2/NER_GOGN/1000K test bert_outputs/electra-small.txt $current_dir/bert_outputs UseValidation
python3 scripts/known_unknown_filtering.py /mnt/c/Users/auzi/verkefni_phase2/NER_GOGN/1000K test bert_outputs/electra-base.txt $current_dir/bert_outputs UseValidation
python3 scripts/known_unknown_filtering.py /mnt/c/Users/auzi/verkefni_phase2/NER_GOGN/1000K test bert_outputs/combitagger.txt $current_dir/bert_outputs UseValidation

python3 scripts/createCoNLLEvaluationOutput.py bert_outputs/known_only known_gold
tmp=$(ls eval/ | wc -w)
session_no_known=$(expr $tmp - 1)
python3 scripts/createCoNLLEvaluationOutput.py bert_outputs/unknown_only unknown_gold
tmp=$(ls eval/ | wc -w)
session_no_unknown=$(expr $tmp - 1)

#python3 scripts/known_unknown_filtering.py /mnt/c/Users/auzi/verkefni_phase2/NER_GOGN/1000K test output/multilingual-bert.txt UseValidation


echo "ELECTRA-small"
perl scripts/conlleval.pl < eval/$session_no/electra-small.txt
echo 'KNOWN ENTITIES ONLY:'
perl scripts/conlleval.pl < eval/$session_no_known/electra-small.txt
echo 'UNKNOWN ENTITIES ONLY:'
perl scripts/conlleval.pl < eval/$session_no_unknown/electra-small.txt
echo "multilingual-BERT"
perl scripts/conlleval.pl < eval/$session_no/multilingual-bert.txt
echo 'KNOWN ENTITIES ONLY:'
perl scripts/conlleval.pl < eval/$session_no_known/multilingual-bert.txt
echo 'UNKNOWN ENTITIES ONLY:'
perl scripts/conlleval.pl < eval/$session_no_unknown/multilingual-bert.txt
echo "ELECTRA-base"
perl scripts/conlleval.pl < eval/$session_no/electra-base.txt
echo 'KNOWN ENTITIES ONLY:'
perl scripts/conlleval.pl < eval/$session_no_known/electra-base.txt
echo 'UNKNOWN ENTITIES ONLY:'
perl scripts/conlleval.pl < eval/$session_no_unknown/electra-base.txt
echo "CombiTagger"
perl scripts/conlleval.pl < eval/$session_no/combitagger.txt
echo 'KNOWN ENTITIES ONLY:'
perl scripts/conlleval.pl < eval/$session_no_known/combitagger.txt
echo 'UNKNOWN ENTITIES ONLY:'
perl scripts/conlleval.pl < eval/$session_no_unknown/combitagger.txt


rm -r bert_outputs
