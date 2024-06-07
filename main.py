from noun_tokenizer import *
from corpus import get_column_corpus
from langchain_community.llms import Ollama
import time

def generate_synthetic_data(sourcefile:str, fromLine: int, toLine: int): 

    llm = Ollama(model="phi3:mini", base_url="https://5937-34-16-192-5.ngrok-free.app/")
    indexLine = -1

    synthetic_list = []
    with open(sourcefile, 'r', encoding="utf8") as file:
        lines = file.readlines()

        for line in lines:

            indexLine += 1
            if  fromLine <= indexLine <= toLine:
                print(indexLine)    

                sentence =  get_column_corpus(line, 2)
                sentence_id = get_column_corpus(line, 0)
                nouns = NounTokenizer(sentence)
            
                if (len(nouns) == 0):
                    synthetic_list.append(sentence_id + "| ")
                    continue

                prompt = str.format('''replace the word "{0}" with a similar semantich word in the sentence : "{1}"''',
                            nouns.firts_noun(),
                            sentence
                            )
                result = llm.invoke(prompt)
                firts_line = substr_get_firts_line(result)
                if (firts_line == None) :
                    synthetic_list.append(sentence_id + "| ")
                    continue

                res = substr_doble_quote(firts_line)
                # print("noun : " + nouns.firts_noun())
                # print("original : " + sentence)
                if (res == None):
                    synthetic_list.append(sentence_id + "|" + firts_line)
                else:
                    synthetic_list.append(sentence_id + "|" + res)
    return synthetic_list

def save_data(target_file: str, data:list):
    with open(target_file, 'w', encoding="utf8") as file:
        for line in data:
            file.write(line + '\n')

def save_data_append(target_file: str, data:list):
    with open(target_file, 'a', encoding="utf8") as file:
        for line in data:
            file.write(line + '\n')




sourcefile = f"dataset/corpus_paralelo_quz.data"
targetfile = f"dataset/corpus_synthetic_quz.data"

# startTime = time.time()

increment = 100
iteration = 186
while (iteration < 1255) :
    fromIndex = iteration * 100
    toIndex = fromIndex + increment - 1
    synthetic = generate_synthetic_data(sourcefile, fromIndex, toIndex)
    save_data_append(targetfile, synthetic)

    iteration += 1

# endTime = time.time()
# tiempo_transcurrido = endTime - startTime
# print(f'Elapsed Time : {tiempo_transcurrido} segundos') 


# print(result)
# print(substr_doble_quote(result))
