import math
#Вычислить число c заданной точностью d
def PI_number_accuracy():
    n = int(input("Введите количество знаков после запятой: "))
    return f'- при d = {n}, {chr(960)} = {str(math.pi)[:n+2]}'

print(PI_number_accuracy())
