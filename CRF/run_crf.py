from ModelTrainer import *
from Sents2Features import *
import sys
from sklearn.model_selection import cross_val_predict
import os
input_file = sys.argv[1]
output_file = sys.argv[2]

config = configparser.ConfigParser()
config.read('config.ini')
paths = config['Paths']
model_path = paths['CRF']
sents = getDataFromPath(input_file)
write_to_CoNLL(model_path, sent2features, sents, output_file)

# crf = train(model_name, X_train, y_train_1)
# evaluate(model_name, crf, X_train, y_train_1)
# print('DONE')