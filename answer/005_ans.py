# -*- coding:utf-8 -*-

import sys

def fizzbuzz(i):

    #type判定を追加
    if type(i) != int:
        raise TypeError("you must input int [i]")

    if i%5==0 and i%3==0:
        print('FizzBuzz')
    elif i%3==0:
        print(Fizz)
    elif i%5==0:
        print(Buzz)
    else:
        print(str(i))


if __name__=='__main__': #mainはここから

    try:
        fizzbuzz(1.0)
    except TypeError:
        print(sys.exc_info()) #エラー内容をprint

    try:
        fizzbuzz(15)
    except TypeError:
        print(sys.exc_info()) #エラー内容をprint