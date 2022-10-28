'''
Student Name:       Dylan Murray
Student Number:     121747725


My CA is based around the Anime One Piece. 
This will act as a basic record the Navy holds of Pirates, their Crews, Abilities, Bounties and Goals.
'''

from logging import exception
from typing import ClassVar


class Pirate:

    __pirate_name: ClassVar[str]
    __pirate_goals: ClassVar[str]
    __haki: ClassVar[dict[list]]
    __devil_fruit: ClassVar[dict[list]]


    def __init__(self, class_name, *args:str, **kwargs:str) -> None:

        self.__pirate_name = class_name

        if len(kwargs) !=0:
            if "goals" in kwargs.keys():
                self.__goals = kwargs["goals"]
            else:
                raise PirateExceptionError("Seems to be a problem with constructor type for "+str(self.__class__.__name__))
            if "haki" in kwargs.keys():
                self.__haki = kwargs["haki"]
            else:
                raise PirateExceptionError("Seems to be a problem with constructor type for "+str(self.__class__.__name__))
            if "devil_fruit" in kwargs.keys():
                self.__devil_fruit = kwargs["devil_fruit"]
            else:
                raise PirateExceptionError("Seems to be a problem with constructor type for "+str(self.__class__.__name__))
                

class PirateExceptionError(Exception):
    pass
