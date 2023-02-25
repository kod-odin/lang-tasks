#!/usr/bin/python
import string
import os
import sys
import readline
input_file = input('Введите входной файл: ')
file = open(input_file, 'r')
file_output = open("output.txt", 'w')
text = file.read()
predl = text.split('\n')
for row in predl:
    t = 0
    tt = os.popen("echo "+row+" | preprocess | hunspell -d mari -m 2>/dev/null").read()
    if "+Cmp" in tt:
      t = 1
    if t==1:
      file_output.write(row + '\n')
file.close()
file_output.close()
