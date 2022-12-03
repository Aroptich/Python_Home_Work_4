# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random


def creating_random_numbers(k: int) -> str:
    data_recording = []
    N = k
    for i in range(N + 1):
        number = str(random.randint(0, 100))
        if number == '0':
            continue
        elif N == 1:
            data_recording.append(number + '*' + 'x')
        elif N == 0:
            data_recording.append(number)
        elif N > 1:
            data_recording.append(number + '*' + '(' + 'x**' + str(k) + ')')
        N -= 1

    with open('text.txt', 'w', encoding='UTF-8') as l:
        l.writelines(f'- для k = {k} => {"+".join(data_recording).replace("1*","" )} = 0')
    # print(f'{"+".join(data_recording).replace("1*","" )} = 0')


creating_random_numbers(k=4)
