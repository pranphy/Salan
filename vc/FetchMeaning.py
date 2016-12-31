#View for the gre app in my blog
import os
import re
import requests
import random
import datetime
import json
import logging

from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
from .error import NoInternet, NoSentenceInJson,NoWordInInternet

logging.basicConfig(filename='NewLog.log', level=logging.DEBUG,
    format='[%(asctime)s.%(msecs)d] [%(levelname)s] : %(message)s', 
    #format='[%(asctime)s.%(msecs)d %(levelname)s] %(module)s - %(funcName)s: %(message)s', 
    datefmt="%Y-%m-%d %H:%M:%S")

class Util():
    def allwords(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(BASE_DIR+'/gre/static/media/default.txt') as wordlist:
            for OneWord in wordlist:
                word = OneWord.strip()
                word.replace('\n','')
                yield word

    def fetch_from_list(self,wordlist):
        for word in wordlist.split(','):
            yield word.strip().lower()

        
class OrderVocab():
    def __init__(self,word='dummy'):
        self.word = word
        self.number_of_sent = 2

    def get_online_sentences(self,word,vocabobj):
        logging.info('I am trying to find sentences online for word {}'.format(word))
        url = "https://corpus.vocabulary.com/api/1.0/examples.json?query="+\
            word+"&maxResults=" +str(self.number_of_sent)

        # See if thre is internet connection 
        try :
            sent_page = urlopen(url)
            soup = BeautifulSoup(sent_page)
            jsn = ''
            try:
                jsn = str(soup.select('body')[0].string)
            except IndexError as e:
                jsn = str(soup)

            sent_dict = json.loads(jsn)
            try:
                #vocabobj.save()
                example_list= [] 
                for obj in sent_dict['result']['sentences']:
                    sent_info = {}
                    sent_info['sentence'] = obj['sentence']
                    sent_info['url'] = obj['volume']['locator']
                    example_list.append(sent_info)
                #end for
                return  example_list
            except KeyError as e:
                logging.info('Error found {}'.format(str(e)))
                logging.info('No sentences for word {} found'.format(word))
                raise NoSentenceInJson

        # Since there is no internet connection
        except URLError as e:
            raise NoInternet

        
    def get_online_vocab(self):
        word = self.word
        logging.info('Trying to search the word {} online'.format(word))
        vocurl = "http://vocabulary.com/dictionary/"+word
        # Check if internet connection is online
        try:
            #get vocab info from this page 
            voc_page = urlopen(vocurl)
            soup = BeautifulSoup(voc_page)

            shortdef = (soup.select('.definitionsContainer .main .section p.short')[0]).get_text()

            longdef = (soup.select('.definitionsContainer .main .section p.long')[0]).get_text()

            #now try to get the meaning
            filtered = soup.select('.definitions .definition .group .first .definition')[0]
            formtd = re.sub('\s+',' ',str(filtered.text)).strip()
            prt_of_speech,mean= formtd.split(' ',1)
            #logging.info('Type of shortdef is {} and str(shortdef) is {}'.format(type(shortdef),str(shortdef)))
            vc_vocab_obj = {}
            vc_vocab_obj = {
                    'word':word,
                    'meaning':str(mean),
                    'short_def':str(shortdef),
                    'long_def':str(longdef)
            }
            #VcVocab_obj = VcVocab(word=word, meaning = str(mean), short_def = str(shortdef), long_def = str(longdef))
            logging.info(' The word {} is found online '.format(word))
            return vc_vocab_obj
        except URLError as e:
            logging.error(' There is no internet connection ')
            raise NoInternet()
        except IndexError as e:
            logging.info(' There is no such word in internet connection ')
            raise NoWordInInternet()

    def get_object(self):
        logging.info("Trying to get meaning of {}".format(self.word))
        word = self.word
        logging.info(' Got word {}'.format(word))
        word_info  = {}
        #Try to find the word out in local Database
        
        try:
            logging.info(' info or sentence for : {} doesnt exist in local '.format(word))
            try:
                VcVocab_obj = self.get_online_vocab()

                word_info['shortdef'] = VcVocab_obj['short_def']
                word_info['longdef'] = VcVocab_obj['long_def']
                word_info['meaning'] = VcVocab_obj['meaning']

                try:
                    logging.info("Tyring to fetch {} from internet".format(word))
                    word_info['sentences'] = self.get_online_sentences(word,VcVocab_obj)
                    #logging.info(word_info['sentences'])
                except NoSentenceInJson:
                    word_info['sentences'] = [{'sentence':'no sentence in json','url':'#'}]
                except NoInternet:
                    word_info['sentences'] = [{'sentence':'no internet ','url':'#'}]
            #Can't fetch vocab object
            except NoInternet:
                word_info['shortdef'] = 'No internet'
                word_info['longdef'] = 'No internet'
                word_info['meaning'] = 'No Internet '
                word_info['sentences'] = [{'sentence':'no internet ','url':'#'}]
            except NoWordInInternet:
                word_info['shortdef'] = 'No word in internet'
                word_info['longdef'] = 'No word in internet'
                word_info['meaning'] = 'No such word Internet '
                word_info['sentences'] = [{'sentence':'no such word in internet ','url':'#'}]
            #handled word from internet completely
        #handeled word from local or internet completely
        except Exception as e:
            logging.error(e)
        return word_info
