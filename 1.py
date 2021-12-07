'''
Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_f = open('test.txt', 'w', encoding = 'utf8')
data = input('Введите текст: ')
while True:
    my_f.writelines(data + '\n')
    data = input('Введите текст: ')
    if not data:
        break
my_f.close()
with open('test.txt', 'r', encoding = 'utf8') as w:
    for line in w:
        print(line)
my_f.close()