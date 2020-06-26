# split is the proporitionality of the training set that first CRF uses

from SentenceGetter import SentenceGetter
import pandas as pd
import configparser
from Sents2Features import sent2labels
from Sents2Features import sent2features
from sklearn_crfsuite import CRF
from sklearn.model_selection import cross_val_predict
from sklearn_crfsuite.metrics import flat_classification_report
import sklearn.model_selection

def getTrainingData(split=2):
    config = configparser.ConfigParser()
    config.read('../trainConfig.ini')
    paths = config['Paths']
    train_path = paths['train_path']
    # train_data = pd.read_csv("CRF-is-400k-train.tsv", sep='\t')
    train_data = pd.read_csv(train_path, sep='\t')
    train_data = train_data.fillna(method="ffill")
    train_getter = SentenceGetter(train_data)
    split_index = round(split * len(train_getter.sentences))  # int(1*(len(train_getter.sentences)/3))round(prop*len(x))
    if split != 2:
        train_sentences_1 = train_getter.sentences[:split_index]
        train_sentences_2 = train_getter.sentences[split_index:]
        return train_sentences_1, train_sentences_2
    else:
        train_sentences_1 = train_getter.sentences
        return  train_sentences_1



def getValidData():
    config = configparser.ConfigParser()
    config.read('../trainConfig.ini')
    paths = config['Paths']

    # print(len(train_getter.sentences))
    # print(len(y_train_1))
    # print(len(y_train_2))
    # valid_data = pd.read_csv("CRF-is-400k-valid.tsv", sep='\t')
    valid_path = paths['valid_path']
    valid_data = pd.read_csv(valid_path, sep='\t')
    valid_data = valid_data.fillna(method="ffill")
    valid_getter = SentenceGetter(valid_data)
    valid_sentences = valid_getter.sentences



    return valid_sentences


def getTestData():
    config = configparser.ConfigParser()
    config.read('../trainConfig.ini')
    paths = config['Paths']
    # test_data = pd.read_csv("CRF-is-400k-test.tsv", sep='\t')
    test_path = paths['valid_path']
    test_data = pd.read_csv(test_path, sep='\t')
    test_data = test_data.fillna(method="ffill")
    test_getter = SentenceGetter(test_data)
    test_sentences = test_getter.sentences
    return  test_sentences

def getDataFromPath(path):
    data = pd.read_csv(path, sep='\t')
    data = data.fillna(method="ffill")
    sent_getter = SentenceGetter(data)
    sents = sent_getter.sentences
    return  sents


def write_to_CoNLL(mdl_file_name, sentence2features, test_sentences, write_path):
    X_test_local = []
    cond_rand_mdl = CRF(algorithm='lbfgs',
                        c1=0.0001,
                        c2=0.0001,
                        max_iterations=100,
                        all_possible_transitions=False,
                        model_filename=mdl_file_name)
    if mdl_file_name[(len(mdl_file_name) - 1)] == '2':
        old_crf = CRF(algorithm='lbfgs',
                      c1=0.0001,
                      c2=0.0001,
                      max_iterations=100,
                      all_possible_transitions=False,
                      model_filename=(mdl_file_name[:(len(mdl_file_name) - 1)]) + '1')
        X_test_local = [sent2features_second_guess(s, sentence2features, old_crf) for s in test_sentences]
    else:
        X_test_local = [sentence2features(s) for s in test_sentences]
    predictions = cond_rand_mdl.predict(X_test_local)
    with open(write_path, 'a') as f:
        for i in range(0, len(predictions)):
            sent = test_sentences[i]
            preds = predictions[i]
            for j in range(0, len(sent)):
                str_to_write = '{}\t{}\n'.format(sent[j][0], preds[j])
                f.write(str_to_write)
            f.write('\n')

def train(model_name, xtrain, ytrain):
    print('hallo')
    crf = CRF(algorithm='lbfgs',
              c1=0.0001,
              c2=0.0001,
              max_iterations=100,
              all_possible_transitions=False,
              model_filename=(model_name))
    crf.fit(xtrain, ytrain)
    print('hallo2')
    return crf


def evaluate(model_name, crf, xvalid, yvalid):
    dict_1 = {}

    pred = cross_val_predict(estimator=crf, X=xvalid, y=yvalid, cv=5)
    # report = flat_classification_report(y_pred=pred, y_true=y_valid, labels=sorted_labels, digits=3, output_dict=True)
    print(flat_classification_report(y_pred=pred, y_true=yvalid, labels=sorted_labels, digits=3))


def execute_experiment(sent_to_features_func, batch, experiment_name, result_dict, split_train_proportion = 2):
    print(experiment_name)
    train_sentences_1, train_sentences_2, valid_sentences, test_sentences=getData(batch)

    y_train_1 = [sent2labels(s) for s in train_sentences_1]
    y_valid = [sent2labels(s) for s in valid_sentences]
    y_test = [sent2labels(s) for s in test_sentences]

    print("getting data done....")
    X_train = [sent_to_features_func(s) for s in train_sentences_1]
    print("train_sents done....")
    crf1 = train(experiment_name+'_1', X_train, y_train_1)
    print('training done....')
    X_valid1 = [sent_to_features_func(s) for s in valid_sentences]
    # evaluate(model_name, crf, xvalid , yvalid):
    evaluate(experiment_name + '_1', crf1, X_valid1, y_valid)
    to_CoNLL(experiment_name +'_1',sent2features_final, test_sentences)
    if split_train_proportion != 2:
        y_train_2 = [sent2labels(s) for s in train_sentences_2]
        X_train = [sent2features_second_guess(s, sent_to_features_func, crf1) for s in train_sentences_2]
        print("train_sents done....")
        crf2 = train(experiment_name+'_2', X_train, y_train_2)
        print('training done....')
        X_valid2 = [sent2features_second_guess(s, sent_to_features_func, crf1) for s in valid_sentences]
        evaluate(experiment_name + '_2', crf2, X_valid2, y_valid)
        to_CoNLL(experiment_name +'_2',sent2features_final, test_sentences)




