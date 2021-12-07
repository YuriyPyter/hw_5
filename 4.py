''' Создать (не программно) текстовый файл со следующим содержимым:
One—1
Two—2
Three—3
Four—4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''


with open('file_4.txt', 'r', encoding = 'utf-8') as f:
    f = [line.rstrip() for line in f] # rsstrip() удаляет знак /n из вывода значений
    dictionary = {}
    new_dictionary = ['Один', 'Два', 'Три', 'Четыре']
    i = 0
    for line in f:
        word, value = line.split('-')
        dictionary[new_dictionary[i]] = value
        n = '\n'
        with open('test4.txt', 'a', encoding='utf8') as my_f:
            my_f.write(f'{new_dictionary[i]}-{value} {n}')
        i += 1
    with open('test4.txt', 'r', encoding='utf8') as my_f:
        print(my_f.read())

