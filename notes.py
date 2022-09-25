#Lect4

#step 1 - scope - variables and functions
#       - variables as values, variables as pointer to "something else..."
'''
i = 7

def my_f():
    i = 5
    return i

i = my_f()
print(i)
'''

#step 2 - empty class - pass or return?
'''
class Animal:
    #return cannot be used in a class.
    pass

my_animal = Animal()
'''

#step 3 - class attributes and methods - adding self...
from typing import ClassVar


class Animal:


    i = 5

    def return_i(self):
        return self.i

my_animal = Animal()
print(my_animal.i)
print(my_animal.return_i())

#step 4 - add a j attribute and some hints, set instance and class values
#       - new classes contain original instance values

class Animal:


    i: ClassVar[int] = 6
    j: ClassVar[int] = 8
    _i: ClassVar[int] = 16
    _j: ClassVar[int] = 18
    __i: ClassVar[int] = 26
    __j: ClassVar[int] = 28

    def __my_private_func(self, param):
        return "7"

    def get_i(self) -> int:
        return self.i

    def get_j(self) -> int:
        return self.j    

    def set_i(param1: int) -> None:
        return self.__my_private_func(param1)

    def set_j(param1: int) -> None:
        self.j = param1


my_animal = Animal = Animal()
print(my_animal.set_i(12))
# print("Animals i value is", my_animal.i)
# print("Animals i value is", my_animal._i)
# # print("Animals i value is", my_animal.__i)
# print("Animals i value is", my_animal.get_i())

'''Dunder forces it to be private and inaccessible'''


# print(my_animal.i)
# print(my_animal.get_i())
# print(my_animal.j)
# print(my_animal.get_j())

# my_animal.set_i(12)
# print("Animal 1 has an i value of", my_animal.i)

# my_animal2 = Animal = Animal()
# print("Animal 2 has an i value of", my_animal2.i)