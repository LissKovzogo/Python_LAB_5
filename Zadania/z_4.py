#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    first_dict={
        246:'abc',
        365:'qwe',
        751:'san'
    }
    print(f'Исходный словарь: {first_dict}')
    dict_items = first_dict.items()
    reversed_dict = {value: key for key, value in dict_items}
    print(f'Обратный словарь: {reversed_dict}')