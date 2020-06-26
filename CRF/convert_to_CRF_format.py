import sys


def convert_corpus(filepath, outputfile_path):
    print(filepath)
    with open(filepath, 'r') as f:
        lines = f.readlines()

    print(len(lines))
    # if outputfile == '':
    filepath_parts = filepath.split('/')
    filename = filepath_parts[len(filepath_parts)-1]
    # outputfile = batch + filename
    # outputfile_path = '/home/alma/verkefni/corpuses/CRF-corpuses-final/' + outputfile
    with open(outputfile_path, 'w') as f:
        # f.write('word\tsentence#\ttag\n')
        f.write('word\tsentence#\ttag\tpos\tlemma\n')
        sent_count = 0
        for line in lines :
            parts = line.split('\t')
            # if len(parts) != 4:
            if len(parts) != 4:
                sent_count += 1
                f.write('\n')
                continue
            # write_str = '{}\t{}\t{}\n'.format(parts[0],sent_count,parts[1])
            write_str = '{}\t{}\t{}\t{}\t{}'.format(parts[0], sent_count, parts[1], parts[2], parts[3])
            f.write(write_str)

input_file = sys.argv[1]
output_file = sys.argv[2]

convert_corpus(input_file, output_file)


# from os import listdir
# from os.path import isfile, join
#
# mypath = '/home/alma/verkefni/corpuses/CRF-corpuses'
# dirs  = [f for f in listdir(mypath) if not isfile(join(mypath, f))]
#
# for dir in dirs:
#     longer_path = mypath + '/' + dir + '/'
#     files  = [f for f in listdir(longer_path) if isfile(join(longer_path, f))]
#     for file in files:
#         convert_corpus(longer_path + file, dir)