import nltk
import re
from nltk.tokenize import word_tokenize

class NounTokenizer:
    def __init__(self, sentence: str):
        tokens = word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)

        # list of (word, isNoun) 
        self.tokens = []
        self.nouns = []
        for word, pos in tagged:
            isNoun = pos == 'NN' or pos == 'NNS'
            tupla = (word,isNoun )
            self.tokens.append(tupla)
            if (isNoun):
                self.nouns.append(word)

    # how many nouns has this sentence
    def __len__(self):
        return len(self.nouns)

    # return the firts noun founded on this sentence
    def firts_noun(self) :
        if (len( self.nouns) > 0):
            return self.nouns[0]
        else :
            return None
        
    # return the n-th noun founded on this sentence
    def noun_th(self, index: int): 
        if (len( self.nouns) > 0):
            return None
        if (index < len( self.nouns)):
            return self.nouns[index]
        else :
            return None
        
# extract the firts sub-sentence that is into doble quote (xxx "extracted" xxx)
def substr_doble_quote(sentence : str) :
    patron = r'"([^"]*)"'
    resultado = re.search(patron, sentence)
    if resultado:
        return resultado.group(1)
    else:
        return None
    
# return the firts line of an string, if empty return none
def substr_get_firts_line(sentence : str):
    firts_line = sentence.splitlines()[0].strip()
    if (firts_line == ""):
        return None
    else:
        return firts_line

