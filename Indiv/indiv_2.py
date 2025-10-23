#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from datetime import date

if __name__ == '__main__':
    contacts = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            name = input("Фамилия и инициалы?  ")
            number = input("Номер телефона? ")
            birth_date = list(map(int, input("Дата рождения (в формате XX.XX.XXXX)? ").split('.')))

            if number[0] == '+':
                number = '8' + number[2:]

            contact = {
                'name': name,
                'number': number,
                'date': birth_date,
            }
            contacts.append(contact)

            if len(contacts) > 1:
                contacts.sort(key=lambda item: (item.get('date', [0, 0, 0])[2],
                                                item.get('date', [0, 0, 0])[1],
                                                item.get('date', [0, 0, 0])[0]))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 35,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^25} | {:^20} |'.format(
                    "№", "ФИО", "Номер телефона", "Дата рождения"
                )
            )
            print(line)

            for idx, contact in enumerate(contacts, 1):
                date_list = contact.get('date', [0, 0, 0])
                date_str = f"{date_list[0]}.{date_list[1]}.{date_list[2]}"

                print(
                    '| {:>4} | {:<30} | {:<25} | {:<20} |'.format(
                        idx,
                        contact.get('name', ''),
                        contact.get('number', ''),
                        date_str
                    )
                )
                print(line)

        elif command.startswith('select '):
            count = 0
            parts = command.split(' ', maxsplit=1)
            num = parts[1]
            for contact in contacts:
                if contact.get('number') == num:
                    count += 1
                    print(contact.get('name', ''))

            if count == 0:
                print("Контакт не найден в телефонной книге.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить контакт")
            print("list - вывести список контактов")
            print("select <номер> - найти контакт по номеру телефона")
            print("help - отобразить справку")
            print("exit - завершить работу с программой")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)