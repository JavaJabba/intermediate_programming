'''
Student Name:       Dylan Murray
Student Number:     121747725


My CA is based around the Anime One Piece. 
This will act as a basic record the Navy holds of Pirates, their Crews, Abilities, Bounties and Goals.
'''

from typing import ClassVar


class Pirate:
    'Pirate Parent Class with general attributes'

    #Encapsulation with private attributes
    __pirate_name: ClassVar[str]
    __crew: ClassVar[str]


    def __init__(self, class_name, *args:str, **kwargs:str) -> None:

        self.__pirate_name = class_name

        #error handling for no inputs
        if len(kwargs) !=0:
            if "goals" in kwargs.keys():
                self.__goals = kwargs["goals"]
            else:
                raise PirateExceptionError("Seems to be a problem with constructor type for "+str(self.__class__.__name__))
            if "pirate_goals" in kwargs.keys():
                self.__pirate_goals = kwargs["pirate_goals"]
            else:
                raise PirateExceptionError("Goals are missing for "+str(self.__class__.__name__)) 

    @property
    #get the pirate name from the class name
    def pirate_name(self):
        return self.__pirate_name
    #set the pirate name
    @pirate_name.setter
    def pirate_name(self, name: str):
        self.__pirate_name = name
    
    #get the crew name from input
    def get_crew(self) -> str:
        return self.__crew
    #set the crew name
    def set_crew(self, crew: str):
        self.__crew = crew
    
    crew = property(get_crew, set_crew)
    
                

class PirateExceptionError(Exception):
    pass

class Luffy(Pirate):
    'Child class with attributes specific to the child and not the parent'

    __devil_fruit: ClassVar[dict[list]]
    __catchphrase: ClassVar[str]
    __pirate_goals: ClassVar[str]
    __bounty: ClassVar[int]


    def __init__(self, *args:str, **kwargs:str) -> None:
        super().__init__(str(self.__class__.__name__), *args, **kwargs)

        #error handling for missing values
        if "catchphrase" in kwargs.keys():
            self.__catchphrase = kwargs["catchphrase"]
        else:
            raise PirateExceptionError("Catchphrase is missing for "+str(self.__class__.__name__))
        if "pirate_goals" in kwargs.keys():
            self.__pirate_goals = kwargs["pirate_goals"]
        else:
            raise PirateExceptionError("Goals are missing for "+str(self.__class__.__name__))            
        if "bounty" in kwargs.keys():
            self.__bounty = kwargs["bounty"]
        else:
            raise PirateExceptionError("Bounty is missing for "+str(self.__class__.__name__)) 


    def talk(self):
        return super()

'''
Was going to add more for the character to talk and 
say their catchphrase and what crew they are apart of and their name and goals but ran out of time
'''




