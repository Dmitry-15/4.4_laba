#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

"""
Решите следующую задачу: напишите программу, которая будет генерировать матрицу из
случайных целых чисел. Пользователь может указать число строк и столбцов, а также
диапазон целых чисел. Произведите обработку ошибок ввода пользователя.
"""


class Matrix:
    def __init__(self, first, second, third, fourth):
        self.line = int(first)
        self.column = int(second)
        self.min = int(third)
        self.max = int(fourth)

    def random_init(self):
        print([[random.randrange(self.min, self.max) for _ in range(self.column)] for _ in range(self.line)])


def main():
    try:
        first = input("Введите количество строк: ")
        second = input("Введите количество столбцов: ")
        third = input("Введите минимальную границу диапазона чисел: ")
        fourth = input("Введите максимальную границу диапазона чисел: ")
        matrix = Matrix(first, second, third, fourth)
        matrix.random_init()
    except ValueError:
        print("Ошибка при вводе значения!")


if __name__ == "__main__":
    main()