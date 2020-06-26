from reynir.bincompress import BIN_Compressed


class NELookup:
    """
        Lookup for words that appear in BÍN as a person name. Makes use of the BÍN access module from Reynir, which uses a compressed version of BÍN.

    """

    # tags for given names, surnames and pet names from BÍN

    def __init__(self, bin_module):
        self.bin_module = bin_module
        self.name_tags = ["ism", "föð", "móð", "dyr"]
        self.place_tags = ["örn", "lönd"]
        self.org_tags = ["fyr"]

    def name_in_BIN(self, word, type=None):
        """
            Queries BÍN for a name.

            Args:
                word (str): The name to query.

            Returns:
                True or False (bool)

        """

        bin_result = self.bin_module.lookup(word)
        if not bin_result:
            return False

        if not type:
            tags = self.name_tags
        else:
            tags = ["föð", "móð"]

        for b in bin_result:
            # we want the word to be in one of the classes in 'name_tags' and 'nefnifall eintölu'
            if b[3] in tags and b[5] == "NFET":
                return True
        return False

    def place_in_BIN(self, word):
        """
            Additional function for the place names found in BÍN:

            Args:
                word (str): The location to query.

            Returns:
                True or False (bool)

        """
        bin_result = bin_module.lookup(word)

        if not bin_result:
            return False

        for b in bin_result:
            if b[3] in self.place_tags:
                return True

        return False

    def org_in_BIN(self, word):
        """
        Additional function for the organization names found in BÍN:

        Args:
            word (str): The organization name to query.

        Returns:
            True or False (bool)

        """
        bin_result = bin_module.lookup(word)

        if not bin_result:
            return False

        # some human names are present as companies in BIN, return false in those cases

        if self.name_in_BIN(word):
            return False

        for b in bin_result:
            if b[3] in self.org_tags:
                return True

        return False

    if __name__ == "__main__":
        import sys

        sys.path.append('..')

        '''Removed code to handle add+exclude lists (only relevant for the 200K corpus section).'''


bin_module = BIN_Compressed()

ne_lookup = NELookup(bin_module)
