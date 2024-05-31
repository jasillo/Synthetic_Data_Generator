from noun_tokenizer import NounTokenizer
from langchain_community.llms import Ollama

# llm = Ollama(model="phi3:mini")
# prompt = '''replace the word "companionship" with a similar semantich word in the sentence : "do not have companionship with anyone given to anger" short answer'''
# result = llm.invoke(prompt)
# print(result)

sentence =  "do not have companionship with anyone given to anger"
nouns = NounTokenizer(sentence)

print(len(nouns))

