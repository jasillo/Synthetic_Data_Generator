from noun_tokenizer import *
from langchain_community.llms import Ollama



# with open('archivo.txt', 'r') as archivo:
#     # Lee todas las líneas del archivo
#     lineas = archivo.readlines()
    
#     # Itera sobre cada línea
#     for linea in lineas:
#         # Procesa cada línea como sea necesario
#         print(linea.strip()) 


sentence =  "the god above us"
nouns = NounTokenizer(sentence)

llm = Ollama(model="phi3:mini")
prompt = str.format('''replace the word "{0}" with a similar semantich word in the sentence : "{1}"''',
                    nouns.firts_noun(),
                    sentence
                    )

result = llm.invoke(prompt)
print(result)
print(substr_doble_quote(result))