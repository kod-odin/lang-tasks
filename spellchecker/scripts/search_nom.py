#!/usr/bin/python
import string
import os
import sys
import readline
input_file = input('Введите входной файл: ')
file = open(input_file, 'r')
file_output = open("output_nom.txt", 'w')
text = file.read()
predl = text.split('\n')
for row in predl:
    token = 0
    text_p = row.replace(" — ","-")
    slovo = text_p.split(' ')
    for slowo_row in slovo:
      t = 0
      if "-" in slowo_row:
        otd = slowo_row.split("-")
        for otd_row in otd:
          tt = os.popen("echo "+otd_row+" | hunspell -d mari -m 2>/dev/null").read()
          if "+Nom" in tt:
            t = t+1
      if t>1:
        if token==0:
          file_output.write(row + '\n')
          token = 1
file.close()
file_output.close()
