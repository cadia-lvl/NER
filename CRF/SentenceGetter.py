class SentenceGetter(object):

    def __init__(self, data):
        self.n_sent = 0
        self.data = data
        self.empty = False
        agg_func = lambda s: [(w, t, p, l) for w, t, p, l in zip(s["word"].values.tolist(),
                                                     s["tag"].values.tolist(),
                                                     s["pos"].values.tolist(),
                                                     s["lemma"].values.tolist())]
        # agg_func = lambda s: [(w, t) for w, t in zip(s["word"].values.tolist(),
        #                                              s["tag"].values.tolist())]

        self.grouped = self.data.groupby("sentence#").apply(agg_func)
        self.sentences = [s for s in self.grouped]

    def get_next(self):
        try:
            s = self.grouped[self.n_sent]
            self.n_sent += 1
            return s
        except Exception as e:
            return None