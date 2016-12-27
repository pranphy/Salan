#!/usr/bin/env python3
import vc.FetchMeaning as fthmean 

class WordSrv():
    def __init__(self,pword='parable'):
        self.word = pword
        self.eaning_fetched = False
        self.word_info = {'shortdef':'dummy',
                'longdef':'dummy',
                'sentence':[{'sentence':'dummy','url':'#'}]
        }
        self.fetch_meaning()

    def fetch_meaning(self):
        ord_vocab = fthmean.OrderVocab(self.word)
        self.word_info = ord_vocab.get_object()
        self.meaning_fetched = True

    def get_short_def(self):

        return self.word_info['meaning']

    def get_long_def(self):
        return self.word_info['longdef']
