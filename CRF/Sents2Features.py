from NELookup import ne_lookup
from FileQuery import *
def getCharNGramForWord(word, n):
  ngrams = []
  if len(word) < n:
    return ngrams
  for i in range(0, len(word)-(n - 1)):
    ngrams.append(word[i:i+n].lower())
  return ngrams

def sent2features_second_guess(sent, old_sent2features, oldpredictor):
    features = old_sent2features(sent)
    prediction = oldpredictor.predict_single(features)
    return [word2features_second_guess(sent, features[i], prediction, i) for i in range(len(sent))]

def sent2labels(sent):
    # return [label for token, label, pos, lemma in sent]
    return [label for token, label in sent]


def sent2tokens(sent):
    return [token for token, label, pos, lemma in sent]


def word2features_second_guess(sent, word_features, predicted_labels, i):
    word_features.update({'model1label': predicted_labels[i]})

    return word_features

def sent2features_final(sent):
    return [word2features_final(sent, i) for i in range(len(sent))]

def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]




def word2features(sent, i):
    word = sent[i][0]
    # pos = sent[i][2]
    # lemma = sent[i][3]
    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),

        'word[-1:]': word[-1:],
        'word[-2:]': word[-2:],
        'word[-3:]': word[-3:],
        'word[-4:]': word[-4:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),

        'name_in_BIN': ne_lookup.name_in_BIN(word),
        'place_in_BIN': ne_lookup.place_in_BIN(word),
        'org_in_BIN': ne_lookup.org_in_BIN(word),
        'in_first_words_org': fs.is_first_word_org(word) or f_org.is_first_word_org(
            word),
        'in_other_words_org': fs.is_other_word_org(word) or f_org.is_other_word_org(
            word),
        'in_last_words_org':  fs.is_last_word_org(word) or f_org.is_last_word_org(
            word),
        'in_first_words_loc': sos.is_first_word_org(word) or f_loc.is_first_word_org(
            word),  # or sos_lemmas.is_first_word_org(lemma),
        'in_other_words_loc': sos.is_other_word_org(word) or f_loc.is_other_word_org(
            word),  # or sos_lemmas.is_other_word_org(lemma),
        # 'in_last_words_loc': sos.is_last_word_org(lemma) or sos.is_last_word_org(word) or f_loc.is_last_word_org(word) or sos_lemmas.is_last_word_org(lemma),
        'in_first_words_per': f_per.is_first_word_org(word),
        'in_other_words_per': f_per.is_other_word_org(word),
        # 'in_last_words_per': f_per.is_last_word_org(word),
        'in_first_words_mis': f_mis.is_first_word_org(word),
        'in_other_words_mis': f_mis.is_other_word_org(word),
        # 'in_last_words_per': f_mis.is_last_word_org(word),
        'in_first_words_ucat': f_ucat.is_first_word_org(word),
        'in_other_words_ucat': f_ucat.is_other_word_org(word),
        'in_last_words_ucat': f_ucat.is_last_word_org(word),
    }

    char2grams = getCharNGramForWord(word, 2)
    for it in range(0, len(char2grams)):
        features.update({'{0}:2gram'.format(it): char2grams[it]})

    char3grams = getCharNGramForWord(word, 3)
    for it in range(0, len(char3grams)):
        features.update({'{0}:3gram'.format(it): char3grams[it]})

    char4grams = getCharNGramForWord(word, 4)
    for it in range(0, len(char4grams)):
        features.update({'{0}:4gram'.format(it): char4grams[it]})

    char5grams = getCharNGramForWord(word, 5)
    for it in range(0, len(char5grams)):
        features.update({'{0}:5gram'.format(it): char5grams[it]})

    if i > 0:
        # word1 = sent[i - 1][0]
        # pos = sent[i - 1][2]
        # lemma = sent[i - 1][3]
        # postag1 = sent[i - 1][1]
        features.update({
        })

    else:
        features['BOS'] = True

    if i < len(sent) - 1:
        # word1 = sent[i + 1][0]
        # pos = sent[i + 1][2]
        # lemma = sent[i + 1][3]
        features.update({

        })
    else:
        features['EOS'] = True

    windowSize = 4

    x = i - 1

    while x >= 0 and i - x < (windowSize + 1):
        word = sent[x][0]
        key = '-{}:word'.format(i - x)
        features.update({key: word})
        x -= 1
    x = i + 1
    while x < len(sent) and x - i < (windowSize + 1):
        word = sent[x][0]
        key = '+{}:word'.format(x - i)
        features.update({key: word})
        x += 1

    return features


def word2features_final(sent, i):
    word = sent[i][0]
    pos = sent[i][2]
    lemma = sent[i][3]
    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),

        'word[-1:]': word[-1:],
        'word[-2:]': word[-2:],
        'word[-3:]': word[-3:],
        'word[-4:]': word[-4:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'pos': pos[0],
        'lemma': lemma,
        'name_in_BIN': ne_lookup.name_in_BIN(word),
        'place_in_BIN': ne_lookup.place_in_BIN(word),
        'org_in_BIN': ne_lookup.org_in_BIN(word),
        'in_first_words_org': fs.is_first_word_org(word) or fs.is_first_word_org(lemma) or f_org.is_first_word_org(
            word) or fs_lemmas.is_first_word_org(lemma),
        'in_other_words_org': fs.is_other_word_org(lemma) or fs.is_other_word_org(word) or f_org.is_other_word_org(
            word) or fs_lemmas.is_other_word_org(lemma),
        'in_last_words_org': fs.is_last_word_org(lemma) or fs.is_last_word_org(word) or f_org.is_last_word_org(
            word) or fs_lemmas.is_last_word_org(lemma),
        'in_first_words_loc': sos.is_first_word_org(word) or sos.is_first_word_org(lemma) or f_loc.is_first_word_org(
            word),  # or sos_lemmas.is_first_word_org(lemma),
        'in_other_words_loc': sos.is_other_word_org(lemma) or sos.is_other_word_org(word) or f_loc.is_other_word_org(
            word),  # or sos_lemmas.is_other_word_org(lemma),
        # 'in_last_words_loc': sos.is_last_word_org(lemma) or sos.is_last_word_org(word) or f_loc.is_last_word_org(word) or sos_lemmas.is_last_word_org(lemma),
        'in_first_words_per': f_per.is_first_word_org(word),
        'in_other_words_per': f_per.is_other_word_org(word),
        # 'in_last_words_per': f_per.is_last_word_org(word),
        'in_first_words_mis': f_mis.is_first_word_org(word),
        'in_other_words_mis': f_mis.is_other_word_org(word),
        # 'in_last_words_per': f_mis.is_last_word_org(word),
        'in_first_words_ucat': f_ucat.is_first_word_org(word),
        'in_other_words_ucat': f_ucat.is_other_word_org(word),
        'in_last_words_ucat': f_ucat.is_last_word_org(word),
    }

    char2grams = getCharNGramForWord(word, 2)
    for it in range(0, len(char2grams)):
        features.update({'{0}:2gram'.format(it): char2grams[it]})

    char3grams = getCharNGramForWord(word, 3)
    for it in range(0, len(char3grams)):
        features.update({'{0}:3gram'.format(it): char3grams[it]})

    char4grams = getCharNGramForWord(word, 4)
    for it in range(0, len(char4grams)):
        features.update({'{0}:4gram'.format(it): char4grams[it]})

    char5grams = getCharNGramForWord(word, 5)
    for it in range(0, len(char5grams)):
        features.update({'{0}:5gram'.format(it): char5grams[it]})

    if i > 0:
        word1 = sent[i - 1][0]
        pos = sent[i - 1][2]
        lemma = sent[i - 1][3]
        postag1 = sent[i - 1][1]
        features.update({
        })

    else:
        features['BOS'] = True

    if i < len(sent) - 1:
        word1 = sent[i + 1][0]
        pos = sent[i + 1][2]
        lemma = sent[i + 1][3]
        features.update({

        })
    else:
        features['EOS'] = True

    windowSize = 4

    x = i - 1

    while x >= 0 and i - x < (windowSize + 1):
        word = sent[x][0]
        key = '-{}:word'.format(i - x)
        features.update({key: word})
        x -= 1
    x = i + 1
    while x < len(sent) and x - i < (windowSize + 1):
        word = sent[x][0]
        key = '+{}:word'.format(x - i)
        features.update({key: word})
        x += 1

    return features

def string2sent(input_string):
    #TODO do proper tokenizing here
    parts = input_string.split()
    return [(w, t) for w, t in zip(parts,len(parts)*['O'])]

def string2Features(input_string):
    sent = string2sent(input_string)
    return sent2features(sent)


