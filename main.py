import random
from verification import Verification

class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 1

    def info(self):
        print('Имя - ' + self.name + ' ' + 'Возраст ' + str(self.__age))

    def set_age(self, age):  # Setter mutator
        if age in range(1, 150):
            self.__age = age
        else:
            print('Не допустимое значение возраста! Должно быть положительным числом!')

    def get_age(self):  # Getter или Аксессор
        print(self.__age)

class V2(Verification):
    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.age = age
        self.__save()

    def __save(self):
        with open('user.txt') as r:
            for i in r:
                if f'{self.login, self.password}'+'\n' == i:
                    raise ValueError('User is exists!')
        super().save()

#  MRO(Method Resolution Order)
class A:
    def a(self):
        print('A')

class B:
    def a(self):
        print('B')

class C(B):
    pass
    # def a(self):
    #     print('C')

class D(A, C):
    def a(self):
        super().a()
        print(self.__class__.__mro__)

x = D()
x.a()
