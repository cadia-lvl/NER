
import os

run_str = "python3 scripts/get_POS_tags_from_gold.py annoted_corpus/batches/{0}/conll/train/train {0}; python3 scripts/get_POS_tags_from_gold.py annoted_corpus/batches/{0}/conll/valid/valid {0}; python3 scripts/get_POS_tags_from_gold.py annoted_corpus/batches/{0}/conll/test/test {0}"

batches = ['200K', '400K', '600K', '800K', '1000K']

for batch in batches:
    os.system(run_str.format(batch))