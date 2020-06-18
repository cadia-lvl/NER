import os



properties_template_file = 'sequenceTrainer-templete.properties'
properties_files = []

session_numb = len([f.path for f in os.scandir('experiments') if f.is_dir()]) - 1
os.system('mkdir experiments/{}'.format(session_numb))
os.system('mkdir experiments/{}/bin'.format(session_numb))
os.system('mkdir experiments/{}/output'.format(session_numb))
os.system('mkdir experiments/{}/combined_output'.format(session_numb))

def create_properties_files(name, set, sessionnumb):
    data_dir = '../MSc-NER/data/annotated_corpus/batches/{0}/conll/{1}/{1}'
    training_set = data_dir.format(set, 'train')
    test_set = data_dir.format(set, 'valid')

    output_model = 'experiments/{}/bin/{}'.format(sessionnumb, name)

    properties_files.append(name)

    sed_command = "sed -e 's!<TRAIN_SET>!{}!; s!<TEST_SET>!{}!; s!<OUTPUT_MODEL>!{}!'  {} > {}".format(training_set, test_set, output_model, properties_template_file, name)
    print(sed_command)

    os.system(sed_command)

#../MSc-NER/data/annotated_corpus/batches/1000K/conll/train/train






names = ['200K', '400K', '600K', '800K', '1000K']

# for name in names:
#     create_properties_files(name, name, session_numb)
#
#
# for file in properties_files:
#    os.system('java -Xms8096m -Xmx8096m -jar target/ixa-pipe-ml-0.0.8-exec.jar sequenceTrainer -p {}'.format(file))
#
# models = [ f.path for f in os.scandir('experiments/{}/bin'.format(session_numb)) ]
#
# # for f in properties_files:
# #     os.system('rm {}'.format(f))
#
for m in names:
    model_file = '/home/alma/verkefni/ixa-pipe-ml/experiments/{0}/bin/{1}.bin'.format(session_numb,m)
    output_file = '/home/alma/verkefni/ixa-pipe-ml/experiments/{0}/output/{1}.tsv'.format(session_numb,m)
    test = '/home/alma/verkefni/MSc-NER/data/annotated_corpus/batches/{0}/conll/test/test'.format(m)
    sys_string = '/home/alma/verkefni/NER-Evaluation/run_agerri_model.sh {} {} > {}'.format(model_file, test, output_file)
    os.system(sys_string)


def createCombinedOutputs(name, corpus):
    guess_file = '/home/alma/verkefni/ixa-pipe-ml/experiments/{0}/output/{1}.tsv'.format(session_numb, name)
    true_file = '../MSc-NER/data/annotated_corpus/batches/{0}/conll/test/test'.format(corpus)
    print(guess_file)
    print(true_file)
    with open(guess_file, 'r') as f:
        guess_lines = f.readlines()

    print(len(guess_lines))

    with open(true_file, 'r') as f:
        true_lines = f.readlines()
    #get guess_lines
    print(len(true_lines))

    with open('experiments/{}/combined_output/{}'.format(session_numb, name), 'w') as f:
        for i in range(0, len(true_lines)):
            true_parts = (true_lines[i]).split('\t')
            guess_parts = (guess_lines[i]).split('\t')


            if len(true_parts) == 2 :
                correct_tag = true_parts[1].replace('\n', '')
                wrt_str = "{} {} {}".format(true_parts[0], correct_tag , guess_parts[1])
                f.write(wrt_str)
            else:
                f.write('\n')



for name in names:
    createCombinedOutputs(name, name)