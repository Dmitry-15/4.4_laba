#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import json
import pathlib
import logging

"""
Выполнить индивидуальное задание 1 лабораторной работы 2.19, добавив возможность работы
с исключениями и логгирование.
"""


class MyPeople:
    def __init__(self, line):
        self.line = line

    def select_human(self, people):
        """
        Выбрать человека с заданной фамилией.
        """
        print(self.line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "№",
                "Ф.И.О.",
                "Знак зодиака",
                "Дата рождения"
            )
        )
        print(self.line)
        # Инициализировать счетчик.
        who = input('Кого ищем?: ')
        count = 0
        # Проверить людей из списка.
        for i, num in enumerate(people, 1):
            if who == num['name']:
                count += 1
                print(
                    '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                        count,
                        num['name'],
                        num['zodiac'],
                        ' '.join((str(i) for i in num['year']))))
        print(self.line)
        if count == 0:
            print('Никто не найден')
        print(self.line)

    def display(self, people):
        """
        Отобразить список людей.
        """
        print(self.line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "№",
                "Ф.И.О.",
                "Знак зодиака",
                "Дата рождения"
            )
        )
        print(self.line)
        for idx, human in enumerate(people, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    human['name'],
                    human['zodiac'],
                    ' '.join((str(i) for i in human['year']))
                )
            )
        print(self.line)

    def add_human(self, people, name, zodiac, year):
        people.append(
            {
                'name': name,
                'zodiac': zodiac,
                'year': year,
            }
        )
        return people

    def save_human(self, file_name, people):
        with open(file_name, "w", encoding="utf-8") as file_out:
            json.dump(people, file_out, ensure_ascii=False, indent=4)
        logging.info(f"Данные сохранены в файл: {file_name}")

    def load_human(self, file_name):
        with open(file_name, "r", encoding="utf-8") as f_in:
            return json.load(f_in)


def main(command_line=None):
    logging.basicConfig(
        filename='people.log',
        level=logging.INFO
    )

    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    pl = MyPeople(line)

    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",
    )
    parser = argparse.ArgumentParser("people")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    subparsers = parser.add_subparsers(dest="command")
    add = subparsers.add_parser(
        "add",
        parents=[file_parser]
    )
    add.add_argument(
        "-n",
        "--name",
        action="store",
        required=True,
    )
    add.add_argument(
        "-z",
        "--zodiac",
        action="store"
    )
    add.add_argument(
        "-yr",
        "--year",
        action="store",
        required=True,
    )
    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],
    )
    select = subparsers.add_parser(
        "select",
        parents=[file_parser],
    )
    select.add_argument(
        "-s",
        "--select",
        action="store",
        required=True,
    )
    args = parser.parse_args(command_line)

    is_dirty = False
    name = args.filename
    home = pathlib.Path.cwd() / name

    try:
        people = pl.load_human(home)
        logging.info("Файл найден")
    except FileNotFoundError:
        people = []
        logging.warning("Файл не найден, создается новый")

    if args.command == "add":
        people = pl.add_human(people, args.name, args.zodiac, args.year)
        is_dirty = True
        logging.info("Добавлен человек")
    elif args.command == 'display':
        pl.display(people)
        logging.info("Отображён список людей")
    elif args.command == "select":
        pl.select_human(people)
        logging.info("Выбран человек с заданной фамилией")

    if is_dirty:
        pl.save_human(args.filename, people)


if __name__ == '__main__':
    main()
