#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    school={
        '1а':22,
        '1б':32,
        '2б': 33,
        '6а': 25,
        '7в': 10
    }
    for clas, num in school.items():
        print(f'В {clas} {num} учащихся')

    school['7в'] = 9
    print(f'В 7в изменилось количество учеников - {school.get('7в')}')

    school['10г'] = 11
    print(f'Сформирован новый класс 10г')

    del school['7в']
    print(f'Расформировали 7в')

    for clas, num in school.items():
        print(f'В {clas} {num} учащихся')
    print(f'Сумма учеников в школе {sum(school.values())}')

