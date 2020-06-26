import configparser

class FileQuery():
    """
    A utility to wrap a single text file consisting of a simple list of words.
    The words are put into a list and a function to query for whether a word exist
    in that list is supplied.

    Args:
        file_name (file): Name of file to query.

    """

    def __init__(self, file_name):

        try:
            self.file = open(file_name, encoding="UTF-8")

        except OSError:

            print("Unable to open file: " + file_name)
            exit(-1)

        # reading file contents into a list, leaving out the newline character
        self.file_list = [x.strip() for x in self.file]

        self.file.close()

    # a function to query for word existence in the objects list
    def exists_in_file(self, word):
        """
            Looks up the given word in a list

            Args:
                word (str): The word to query.

            Returns:
                True or False (bool)

        """

        if word in self.file_list:
            return True

        else:
            return False


import sys, re


class org_operations:

    def __init__(self, filename):
        # print('hey')
        self.rsk = FileQuery(filename)
        # self.orgs = [[],[],[],[],[],[],[]]
        self.first_words = []
        self.other_words = []
        self.last_words = []
        for line in self.rsk.file_list:
            parts = line.split()
            self.first_words.append(parts[0].lower())
            for i in range(1, len(parts)):
                self.other_words.append(parts[i].lower())
            self.last_words.append(parts[len(parts) - 1].lower())
            # print(line.lower())
            # self.orgs[(len(line.split()))-1].append(line.lower())
        # print(self.orgs[6])
        self.first_words = set(self.first_words)
        self.other_words = set(self.other_words)
        self.last_words = set(self.last_words)

    def is_first_word_org(self, word):
        return word.lower() in self.first_words

    def is_other_word_org(self, word):
        return word.lower() in self.other_words

    def is_last_word_org(self, word):
        return word.lower() in self.last_words


foreign_gaz = ['foreign_LOC.txt', 'foreign_MIS.txt', 'foreign_ORG.txt', 'foreign_PER.txt', 'foreign_UCAT.txt']

config = configparser.ConfigParser()
config.read('config.ini')

print(config.sections())
paths = config['List_Paths']


fs_lemmas = org_operations(paths['companies_lemmatized_list'])
fs = org_operations(paths['companies_list'])
sos = org_operations(paths['locations_list'])
sos_lemmas = org_operations(paths['locations_lemmatized_list'])
f_loc = org_operations(paths['foreign_locations'])
f_mis = org_operations(paths['foreign_miscellaneous'])
f_org = org_operations(paths['foreign_orgs'])
f_per = org_operations(paths['foreign_persons'])
f_ucat = org_operations(paths['foreign_uncategorized'])