import os
# data_file = open('data.txt', 'r') #режим чтения
# data = data_file.readlines()
# print(data)
# data_file.close()

# file = open('xyz.txt', 'w')
# file.write('Hello Pidarasas')
# file.close()
# file = open('xyz.txt', 'r')
# f = file.read()
# print(f)


# #Данный синтаксис "Менеджер контекста" гарантирует нам, что файл будет закрыт, после работы с ним.
# with open('data.txt', 'r') as data_file:
#     data = data_file.read()
    
# # чтение файла происходит целиком
# print(data)


# ''' построчная читка данных из файла '''
# def read_file(filename):
#     with open(filename, 'r', encoding="utf-8") as song_file:
#         for line in song_file.readlines():
#             yield line.strip()  # убираем переносы строк

# for line in read_file("Vladimirskiy Central.txt"):
#     print(line)

'''Поиск расположения файла'''
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'data.txt') # c:\Users\leo10\auto_lessons\curs_auto\lesson13\data.txt
print(file_path)