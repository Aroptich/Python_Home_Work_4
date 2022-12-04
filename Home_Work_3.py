# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def sequence_of_numbers(list_a: list[int]) -> list[int]:
    # Создаем пустой список для уникальных чисел
    list_elem = []
    for i in list_a:
        if list_a.count(i) == 1:
            list_elem.append(i)
    return list_elem


print(sequence_of_numbers([1, 1, 2, 3, 4, 4, 4]))
