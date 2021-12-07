'''
Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

my_file = open ('test_2.txt', 'r', encoding = 'utf8')
data = my_file.read()
print(data)
my_file = open('test_2.txt', 'r')
data = my_file.readlines()
print(f'Количество строк в файле: {len(data)}')
my_file = open ('test_2.txt', 'rt', encoding = 'utf8')
data = my_file.read()
print(f'Количество слов в файле: {len(data.split())}')