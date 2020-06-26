from Sents2Features import string2Features
from sklearn_crfsuite import CRF
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
names = config['Names']

crf = CRF(algorithm='lbfgs',
                    c1=0.0001,
                    c2=0.0001,
                    max_iterations=100,
                    all_possible_transitions=False,
                    model_filename=names['model_name'])


print(crf.predict_single(string2Features('Ég kenni stærðfræði í Háskóla Íslands öll virk kvöld')))