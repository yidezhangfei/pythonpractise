# -*- coding: utf-8 -*-

from types import MethodType

class Student(object):
    def __init__(self, name):
        self.__name = name

def set_age(self, age):
    self.age = age

s = Student("lijun")
Student.set_age = MethodType(set_age, s)
s.set_age(25)

print (s.age)
