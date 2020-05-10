#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person:



    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

p = Person('jerry')

print(hasattr(p, 'eat')) #判断 实例有没有属性或者方法
# print()
f = getattr(p, 'eat')
f()
print(getattr(p, 'age','20' ))
# f()
#