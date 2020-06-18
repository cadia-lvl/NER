import os

properties_files = ['result1-400k.properties']
#                     'result2-400k.properties',
#                     'result6-400k.properties',
#                     'result7-400k.properties',
#                     'result8-400k.properties',
#                     'result9-400k.properties',
#                     'result10-400k.properties',
#                     'result11-400k.properties',
#                     'result12-400k.properties']




for file in properties_files:
   os.system('java -jar target/ixa-pipe-ml-0.0.8-exec.jar sequenceTrainer -p {}'.format(file))

for i in range(1, 10):
    model = 'model{}'.format(str(i))
    model_file = model + '.bin'
    output_file = 'out-400k_' + model + '.tsv'
    os.system('/home/alma/verkefni/NER-Evaluation/run_agerri_model.sh {} /home/alma/verkefni/corpuses/is-400k-test.tsv > {}'.format(model_file, output_file))



