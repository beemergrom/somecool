# -*- coding: utf-8 -*-
from gensim.models import KeyedVectors
from pymystem3 import Mystem
import re
import word2vec


'''
with open("input.txt", 'r', encoding='utf-8') as file:
    file = [row.strip() for row in file if len(row.strip()) > 0]

with open('test.txt', 'w', encoding='utf-8') as output_file:
    for row in file:
        row = row.lower()
        res = re.findall('[а-яё]+', row)
        for i in res:
            output_file.write(i)
            output_file.write(' ')
        output_file.write("\n")


file = open("test.txt", encoding='utf-8')
text = file.readlines()
m = Mystem()
with open("test_lemma.txt", 'w', encoding='utf-8') as output_file:
    for line in text:
        lem = m.lemmatize(line)
        output_file.write("".join(lem))

word2vec.word2phrase("test_lemma.txt", "phrases.txt-phrases", verbose=True)
word2vec.word2vec("phrases.txt-phrases", "phrases.txt.bin", verbose=True)
'''

model = KeyedVectors.load_word2vec_format("phrases.txt.bin", binary=True, encoding='utf-8')

file = open("слово.txt", 'w', encoding="utf-8")
for i in model.most_similar(positive=['пьер'], topn=100):
    file.write(str(i))
    file.write("\n")

file.close()


