#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    u = set("aeiouyAEIOUY")
    x = set(input("Введите строку:"))
    xu = u.intersection(x)
    print(len(xu))