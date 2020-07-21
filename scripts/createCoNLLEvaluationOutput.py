import sys, os

input_dir = sys.argv[1]
output_path = './eval/'
session_numb = len([f.path for f in os.scandir(output_path) if f.is_dir()])
os.system('mkdir {}{}'.format(output_path, session_numb))
full_output_path = '{}{}/'.format(output_path, session_numb)
true_file = sys.argv[2]

file_paths = [f.path for f in os.scandir(input_dir) if not f.is_dir()]
names = []

for path in file_paths:
    parts  = path.split('/')
    print(parts)
    names.append(parts[len(parts) - 1])


def createCombinedOutputs(name, inputdir, outputpath):
    corpus = ''
    if '1000K' in name:
        corpus = '1000K'
    elif '800K' in name:
        corpus = '800K'
    elif '600K' in name:
        corpus = '600K'
    elif '400K' in name:
        corpus = '400K'
    else :
        corpus = '200K'


    guess_file = name
    print(guess_file)
    print(true_file)
    with open(inputdir+ '/' + guess_file, 'r') as f:
        guess_lines = f.readlines()

    print(len(guess_lines))

    with open(true_file, 'r') as f:
        true_lines = f.readlines()
    #get guess_lines
    print(len(true_lines))

    with open(outputpath + name, 'w') as f:
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
    print('name : ' + name)
    createCombinedOutputs(name, input_dir, full_output_path)