from noun_tokenizer import *
from langchain_community.llms import Ollama

# get english part of jw300 corpus
# id | quechua type (que, quz, quy) | english str | quechua str
def get_english_corpus(string :str, index : int):
    splited = string.split(sep="|")
    return splited[index]



llm = Ollama(model="phi3:mini")
counter = 5
with open('dataset/qu.paralelo.clean', 'r', encoding="utf8") as file:
    lines = file.readlines()
    for line in lines:
        if (counter == 0): break
        counter -= 1

        sentence =  get_english_corpus(line, 2)
        nouns = NounTokenizer(sentence)
        
        if (len(nouns) == 0):
            print("NO NOUN")
            continue

        prompt = str.format('''replace the word "{0}" with a similar semantich word in the sentence : "{1}"''',
                    nouns.firts_noun(),
                    sentence
                    )
        result = llm.invoke(prompt) 
        firts_line = substr_get_firts_line(result)
        if (firts_line == None) :
            print("NO RESPONSE")
            continue

        res = substr_doble_quote(firts_line)
        print("noun : " + nouns.firts_noun())
        print("original : " + sentence)
        if (res == None):
            print("synthetic : " + firts_line)
        else:
            print("synthetic : " + res)

        
        



# print(result)
# print(substr_doble_quote(result))