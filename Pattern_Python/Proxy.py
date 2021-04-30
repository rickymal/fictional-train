from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass = ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        """interface method"""
        pass


class Student(IPerson):


    def __init__(self,):
        self.name = "Basic student"

        
    def person_method(self,):
        print("I am: " + self.name)
        

class Teacher(IPerson):

    def __init__(self):
        self.name = "Teacher"

    def person_method(self,):
        print("I am a teacher")



    
p1 = Student()
t1 = Teacher()
p1.person_method()
t1.person_method()


class PersonFactory:
    def build_person(person_type):
        if person_type == 'Student':
            return Student()
        if person_type == "Teacher":
            return Teacher()

        print("invalid type")
        return -1



choice = 'Teacher'

ff = PersonFactory.build_person(choice)
ff.person_method()

