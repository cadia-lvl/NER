import os, sys
from xml.dom.minidom import parse
import datetime


def ratio_of_uppercase(str):
    if len(str) == 0:
        return 0
    ups = 0.
    for i in str:
        if i.isupper():
            ups += 1
    return ups / len(str)


def parse_rmh_for_clustering(path_to_dir, output_file, desired_format):
    print(datetime.datetime.now())

    sentDelim = ''
    tokenDelim = ''
    if desired_format == 'brown':
        sentDelim = '\n'
        tokenDelim = ' '
    elif desired_format == 'clark':
        sentDelim = '\n\n'
        tokenDelim = '\n'
    elif desired_format == 'word2vec':
        sentDelim = ' '
        tokenDelim = ' '
    else:
        sys.exit('format needs to be brown, clark or word2vec')

    for rootdir, _, files in os.walk(path_to_dir):
        for file in files:
            if not file.endswith('.xml'):
                continue
            root = parse(os.path.join(rootdir, file))
            for sentence in root.getElementsByTagName('s'):
                words = sentence.getElementsByTagName('w')
                cs = []  # current sentence
                cs2 = []  # current sentence, lemma only
                for word in words:
                    cs2.append(word.getAttribute('lemma'))
                    cs.append(word.firstChild.nodeValue)
                write_string = tokenDelim.join(cs)
                write_string2 = tokenDelim.join(cs2)
                # ignore all sentances with less than 90% lowercase letters for brown
                # if desired_format == 'brown':
                #     if ratio_of_uppercase(write_string) > 0.1:
                #         continue
                with open(output_file, 'a') as f:

                    f.write(write_string)
                    f.write(sentDelim)
                with open(output_file + '_lemmas', 'a') as f:
                    f.write(write_string2)
                    f.write(sentDelim)
                # ignore all sentances with less than 90% lowercase letters for brown
                if desired_format == 'brown':
                    if ratio_of_uppercase(write_string) > 0.1:
                        continue
                with open(output_file + '_lemmas_filtered', 'a') as f:
                    f.write(write_string2.lower())
                    f.write(sentDelim)

    print(datetime.datetime.now())

def parse_brown_to_clark(input_file, output_file):
    print ('clark')
    print (input_file)
    print(datetime.datetime.now())
    with open(input_file, 'r') as f:

        while True:
            line = f.readline()
            if line:
                with open(output_file, 'a') as f2:
                    tokens = line.split()
                    for token in tokens:
                        f2.write(token.lower())
                        f2.write('\n')
                    f2.write('\n')
            else:
                break
    #     lines = f.readlines()
    # for line in lines:
    #     tokens = line.split()
    #     with open(output_file, 'a') as f2:
    #         for token in tokens:
    #             f2.write(token.lower())
    #             f2.write('\n')
    #         f2.write('\n')
    print(datetime.datetime.now())


def parse_brown_to_w2v(input_file, output_file):
    print ('w2v')
    print (input_file)
    print(datetime.datetime.now())
    with open(input_file, 'r') as f:
        # lines = f.readlines()
        while True:
            line = f.readline()
            if line:
                with open(output_file, 'a') as f2:
                    f2.write(line.lower())
                    f2.write(' ')
            else:
                break
    print(datetime.datetime.now())


def convert_and_filter_corpus_to_lower(input_file, output_file, limit_sentences_by_no_of_tokens):
    print('brown')
    print (input_file)
    print(datetime.datetime.now())
    filename_extension = ''
    if limit_sentences_by_no_of_tokens:
        filename_extension = '-not--two-words'
    output_file = output_file+filename_extension
    with open(input_file, 'r') as f:
        # lines = f.readlines()
        while True:
            line = f.readline()

            if line:
                if limit_sentences_by_no_of_tokens:
                    tokens = line.split()
                    if len(tokens) < 3:
                        continue

                if ratio_of_uppercase(line) > 0.1:
                    continue



                with open(output_file, 'a') as f2:
                    f2.write(line.lower())
                    f2.write('\n')
            else:
                break
    print(datetime.datetime.now())

# parse_brown_to_clark('../corpuses/unmodified/rmh', '../corpuses/clark/rmh')
# parse_brown_to_w2v('../corpuses/unmodified/rmh', '../corpuses/w2v/rmh')
# convert_and_filter_corpus_to_lower('../corpuses/unmodified/rmh', '../corpuses/brown/rmh', True)
# convert_and_filter_corpus_to_lower('../corpuses/unmodified/rmh', '../corpuses/brown/rmh', False)
