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
        self.ord_vocab = fthmean.OrderVocab(self.word)
        self.word_info = self.ord_vocab.get_object()
        self.meaning_fetched = True

    def getMeaning(self):
        return self.word_info['meaning']

    def get_short_def(self):

        return self.word_info['shortdef']

    def getLongDef(self):
        return self.word_info['longdef']

    def getSentences(self):
        sent_list = self.ord_vocab.get_online_sentences(self.word)
        for sent_dict in sent_list:
            yield sent_dict['sentence']

