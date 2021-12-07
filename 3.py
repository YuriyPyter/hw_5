'''
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
'''

with open('file_3.txt', 'r', encoding = 'utf-8') as f:
    workers = {}
    sum_workers = 0
    counter = 0
    for line in f:
        key, value = line.split()
        workers[key] = value
        if float(value) < 20000:
            print(f'{key}: зарплата меньше 20000 руб.')
        sum_workers += float(value)
        counter += 1
    print(f'Средняя величина дохода сотрудников: {sum_workers / counter} руб.')