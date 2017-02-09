# -*- coding:utf-8 -*-

class Dog():

    def __init__(self):
        pass #何もしない時はpass文が使えます。

    def bowwow(self):
        print("bowwow")

if __name__ == '__main__':

    dog=Dog() #インスタンスの作成
    dog.bowwow() #bowwowメソッドを呼び出す。

