
# class Person:
#     def __init__(self, name, age):  #атрибут эземпляра класса self, name, age
#         self.name = name
#         self.age = age

#     @staticmethod
#     def is_adult(age):
#         return age >= 18

# mark = Person('Mark', 25)
# print(mark.is_adult(32))
# print(Person.is_adult(16))



# import random
# from time import sleep
# from tqdm import tqdm

# print('Взлом серверов NASA в процессе ...')
# for i in tqdm(range(100), colour='green'):
#     sleep(random.uniform(0.01, 0.1))

# print('NASA успешно взломана!!!')           






# file = open('test1.txt', 'w')
# file.write('Hello\n')
# file.writelines(['Hello, Sam'])
# file.write('World')
# file = open('test1.txt', 'a')
# file.write('Hello')
# file = open('test1.txt', 'r')
# f = file.read()
# print(f)
# print(f)
# file = open('test1.txt', 'r')
# # print(file.readline())
# # print(file.readline())
# print(file.readlines(2))
# file.close()



# with open('text1.txt') as file:

#     print(file.read())
    


# сериализация (с python в json ) -> dump, dumps
# десериализация (с json в python) -> load, loads 

import json

# d = {'hello': True, 'age': 2, 'name': None}
# print(json.dumps(d))
## {"hello": true, "age": 2, "name": null}

# d = {'hello': True, 'age': 2, 'name': None}
# json_obj = json.dumps(d)
# python_obj = json.loads(json_obj)
# print(python_obj)
# ## {'hello': True, 'age': 2, 'name': None}

# with open('data.json', 'r') as file:
#     # python_obj = json.loads(file.read())     # с строкой работает 
#     ## {'name': None}
#     python_obj = json.load(file)               # с файлом работает  
#     ## {'name': None}
#     print(python_obj) 


# OOP

class A:
    amount = 0 #атрибут класса
obj = A()
obj.color = 'red' #атрибут экземпляр класса

# __new__
# __init__
# __str__
# __pepr__
# __del__
# __dict__
# __add__


# ~!@#$%^&*()_





















