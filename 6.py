'''
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.
'''

def calculate_hours(file_path):
    result = {}
    with open(file_path, 'r', encoding = 'utf-8') as f:
        for line in f:
            subject, numbers = line.split(':')
            subject_sum = sum(int(n) for word in numbers.split() for n in word.split('(') if n.isdigit())
            result[subject] = subject_sum
        print(result)
    return result


calculate_hours('file6.txt')

