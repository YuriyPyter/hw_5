'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

with open ('file5.txt', 'w', encoding = 'utf-8') as f:
    numbers = input('Введите числа через пробел: ')
    f.writelines(numbers)
    numbers = numbers.split()
    int_numbers = [int(numbers[num]) for num in range(len(numbers))]
    print(sum(int_numbers))
