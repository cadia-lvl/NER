from os import listdir
from os.path import isfile, join
import sys
import os

mypath = '/home/alma/verkefni/corpuses/MIM-GOLD_1.0/'
token_count = 0
class Sentence:
    text = ''
    token_list = []
    POS_tags = []
    NER_tags = []
    lemmas = []
    length = 0

    def __init__(self, token_list, NER_tags = [], POS_tags = [], lemmas = []):
        self.text = ' '.join(token_list)
        self.token_list = token_list
        self.NER_tags = NER_tags
        self.POS_tags = POS_tags
        self.lemmas = lemmas
        self.length = len(token_list)

    def __str__(self):
        return self.text + ' '.join(self.NER_tags)



def get_gold_files():

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def parse_gold_file(gold_file):
    with open(mypath+gold_file, 'r') as f:
        gold_lines = f.readlines()

    gold_sents = []
    sent_tokens = []
    sent_pos_tags = []
    sent_lemmas = []
    for token in gold_lines:
        parts = token.split('\t')
        if len(parts) != 3:
            gold_sents.append(Sentence(sent_tokens, POS_tags=sent_pos_tags, lemmas=sent_lemmas))
            sent_tokens = []
            sent_pos_tags = []
            sent_lemmas = []
            continue
        sent_tokens.append(parts[0])
        sent_pos_tags.append(parts[1])
        sent_lemmas.append(parts[2])

    if len(sent_tokens) != 0:
        gold_sents.append(Sentence(sent_tokens, POS_tags=sent_pos_tags, lemmas=sent_lemmas))
        print('GOOD THING ÁSI THOUGHT OF THIS EDGE CASE')
    return gold_sents

def parse_CoNLL_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    sents = []
    sent_tokens = []
    sent_NER_tags = []
    for token in lines:
        parts = token.split('\t')
        if len(parts) != 2:
            sents.append(Sentence(sent_tokens, NER_tags=sent_NER_tags))
            sent_tokens = []
            sent_NER_tags = []
            continue
        sent_tokens.append(parts[0])
        sent_NER_tags.append(parts[1])

    if len(sent_tokens) != 0:
        gold_sents.append(Sentence(sent_tokens, NER_tags=sent_NER_tags))
        print('GOOD THING ÁSI THOUGHT OF THIS EDGE CASE')
    return sents

def get_gold_sents():
    gold_files = get_gold_files()
    sents = []
    for file in gold_files:
        sents.extend(parse_gold_file(file))
    return sents

corpus_file = sys.argv[1]
batch = sys.argv[2]
print(corpus_file)

dirparts = corpus_file.split('/')
filename = dirparts[len(dirparts)-1]

CoNLL_sents = parse_CoNLL_file(corpus_file)
gold_sents = get_gold_sents()

def find_sent_in_gold(sent):
    for gold_sent in gold_sents:
        if sent.text == gold_sent.text:
            return gold_sent

    print('SENTENCE NOT IN GOLD, SHOULD NOT HAPPEN')
    print(sent.text)
    print('SENTENCE NOT IN GOLD, SHOULD NOT HAPPEN')



def write_extended_file():
    corpus_dir = '/home/alma/verkefni/corpuses/CRF-corpuses/{}/'.format(batch)
    path_filename = corpus_dir + 'extended-' + filename + '.tsv'
    os.system('rm {}'.format(path_filename))
    os.system('touch {}'.format(path_filename))
    for sent in CoNLL_sents:
        gold_sent = find_sent_in_gold(sent)
        for i in range(0, sent.length):
            write_str = "{}\t{}\t{}\t{}\n".format(sent.token_list[i], sent.NER_tags[i].replace('\n', ''), gold_sent.POS_tags[i], gold_sent.lemmas[i].replace('\n', ''))
            with open(path_filename, 'a') as f:
                f.write(write_str)

        with open(path_filename, 'a') as f:
            f.write('\n')

#compare total number of sentences with number of unique sentences
def analyze_corpus():
    sent_set = set()
    token_count = 0
    multi_sent_dict = {}
    for sent in gold_sents:
        sent_count = multi_sent_dict.get(str(sent), 0)
        multi_sent_dict[str(sent)] = sent_count + 1
        sent_set.add(str(sent))
        token_count += sent.length
    print('# of gold_sents : {}'.format(len(gold_sents)))
    print('# of unique sents : {}'.format(len(sent_set)))
    print('# of tokens in corpus: {}'.format(token_count))

    # Filter dictionary by keeping only sentences that appear more than once.
    newDict = dict(filter(lambda elem: elem[1] > 1, multi_sent_dict.items()))
    print('# of sentences appearing multiple times: {}'.format(len(newDict)))
    # print({k: v for k, v in sorted(newDict.items(), key=lambda item: item[1])})



#for sent in gold_sents:
#    if 'Elskulegur faðir okkar , tengdafaðir og afi , Gunnar Þorbjörn Gunnarsson' in sent.text:
#        print(sent.text)


write_extended_file()