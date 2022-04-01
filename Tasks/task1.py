#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
соединение, строк. В остальных случаях введенные числа суммируются.
"""


class Summa:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def addition(self):
        print("Сумма чисел: ", int(self.a) + int(self.b))

    def concatenation(self):
        print("Результат конкатенации: ", self.a + self.b)


def main():
    try:
        num1 = input("Первое значение: ")
        num2 = input("Второе значение: ")
        result = Summa(num1, num2)
        result.addition()
    except ValueError:
        result = Summa(num1, num2)
        result.concatenation()


if __name__ == "__main__":
    main()