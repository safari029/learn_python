# -*- coding:utf-8 -*-

def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return str(i)

if __name__ == '__main__': #main関数はこちらで定義します。

    for i in range(1,101):
        print(fizzbuzz(i))

    for i in range(1,51): #同じような処理をする場合に冗長的な記述をしなくてよくなった。
        print(fizzbuzz(i))