# Скрипт, который пройдет по файлу этой базы, выберет все ключи содержащие
# key и сохранит в отдельный txt или csv файл. Как вариант база Букварикс

import csv


# Чтение любого большого текстового файла
def read_big_file(input_file, key):
    try:
        keywords = []
        with open(input_file, 'r', encoding='utf-8', newline='') as f:
            file_reader = csv.reader(f, delimiter=' ')
            for raw in file_reader:
                if key in set(raw):
                    keywords.append(raw)

        return keywords
    except FileNotFoundError:
        print('File not Found')


# Сохранить файл по нужному ключевому слову
def write_file_keywords(input_file, output_file, key):
    try:
        keywords = read_big_file(input_file, key)
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            file_writer = csv.writer(f, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
            for key in keywords:
                file_writer.writerow(key)

        return file_writer
    except FileNotFoundError:
        print('File not Found')
