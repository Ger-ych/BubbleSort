# Python
# Программа для сортировки списка методом пузырька

# подключение необходимых библиотек
import sys
from random import randint

# функция Bubble для сортировки списка
def Bubble(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                buff = list[j]
                list[j] = list[j+1]
                list[j+1] = buff

try:
    number = int(input("Введите длину списка: ")) # ввод длины списка пользователем

    # объявление списка
    list = []

    # получение диапазона заполнения списка рандомными числами
    range_1 = int(input("Введите первое число диапазона заполнения списка рандомными числами: "))
    range_2 = int(input("Введите второе число диапазона заполнения списка рандомными числами: "))

    # заполнение списка рандомными числами
    for i in range(number):
        list.append(randint(range_1, range_2))

    # сортировка списка с помощью функции Bubble 
    Bubble(list)

    # вывод результата
    print("\nВот так выглядит наш список после сортировки пузырьком: \n", list)
    print("\n")

except: print("Ошибка!")