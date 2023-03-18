Скрипт sentence_split.py основан на Python-библиотеке Razdel.

Установите Razdel:

pip3 install razdel

В папке, где находится скрипт sentence_split.py создайте две папки: source и result. В папку source поместите файлы в *.txt, которые хотите разбить по предложениям.

Запустите скрипт:

python3 sentence_split.py

Файлы с результами появятся в папке result.


Скрипт sentence_selection.py предназначен для подготовки предложений, чтобы загрузить их в Common Voice: https://commonvoice.mozilla.org/sentence-collector/#/ru

В папку source поместите файлы в *.txt, которые хотите разбить по предложениям для загрузки в Common Voice.

Запустите скрипт:

python3 sentence_selection.py

Файлы с результами появятся в папке result, где файлы *.txt.1.txt – можно сразу загружать в Common Voice, а файлы *.txt.more_than_13.1.txt – необходимы дорабатывать: там в предложениях более 13 слов или содержать скобки и цифры – такие предложения коллектор предложений Common Voice не даёт загружать.


Скрипт checking_valid_characters.py предназначен для поиска в текстах недостимых символов. В файл valid_characters.txt поместите допустимые символы для ваших файлов.

В папку source поместите файлы в *.txt, которые хотите проанализировать на недостимые символы.

Запустите скрипт:

python3 checking_valid_characters.py

Файлы с результами появятся в папке result.
