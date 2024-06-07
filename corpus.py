from noun_tokenizer import *

# get english part of jw300 corpus
# id | quechua type (que, quz, quy) | english str | quechua str
def get_column_corpus(string :str, index : int):
    splited = string.split(sep="|")
    return splited[index]

def count_quechua_types(file:str):
    dic = {}
    with open(file, 'r', encoding="utf8") as file:
        lines = file.readlines()
        
        for line in lines:
            col =  get_column_corpus(line, 1)
            if ( col in dic):
                dic[col] = dic[col] + 1
            else :
                dic[col] = 1

    for clave, valor in dic.items():
        print(f"{clave}: {valor}")

def extract_quechua_type(source_file:str, target_file: str, q_type :str):

    q_list = []

    with open(source_file, 'r', encoding="utf8") as file:
        lines = file.readlines()
        
        for line in lines:
            col =  get_column_corpus(line, 1)
            if (col == q_type ):
                q_list.append(line)


    with open(target_file + "_" + q_type + ".data", 'w', encoding="utf8") as file:

        for line in q_list:
            file.write(line)




# extract_quechua_type('dataset/qu.paralelo.clean', 'dataset/corpus_paralelo', "quz")
# extract_quechua_type('dataset/qu.paralelo.clean', 'dataset/corpus_paralelo', "que")
# extract_quechua_type('dataset/qu.paralelo.clean', 'dataset/corpus_paralelo', "quy")