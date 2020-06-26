import os

batches = ['200K', '400K', '600K', '800K', '1000K']


run_str = 'java -jar dist/CombiTagger.jar -t ../neuroner-outputs/may28/correct_{0}.tsv ../agerri-outputs/{0}.tsv ../CRF-outputs/{0}-final_1_output.tsv -o ../combitagger-outputs/{0}.tsv'

for batch in batches:
    os.system(run_str.format(batch))
