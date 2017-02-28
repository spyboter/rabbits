#!/usr/bin/python3
#-*- coding:UTF-8 -*-



def bunny():
    try:
        r = int(input('Введите любое число: '))
        return r
    except ValueError:
        return bunny()


if bunny() == 1:
    print(bunny(), 'заяц')
elif 4 > bunny() > 1:
    print(bunny(), 'зайца')
else:
    print(bunny(), 'зайцев')