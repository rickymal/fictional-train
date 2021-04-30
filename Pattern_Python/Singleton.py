from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    
    @abstractstaticmethod
    def get_data():
        pass


class PersonSingleton(Iperson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default",0)
        return PersonSingleton.__instance


    def __init__(self,name,age):
        if PersonSinglethon.__instance != None:
            raise Exception('single cannot be instantiated')
        
        self.name = name
        self.age = age
        PersonSinglethon.__instance = self

    @staticmethod
    def print_data():
        print(f"Name : {PersonSingleton.__instance.name}")
        
    
p = PersonSingleton("Mike")
p.print_data()
