from abc import ABCMeta, abstractmethod, abstractstaticmethod

class IDepartment(metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self,employees):
        pass

    @abstractstaticmethod
    def print_department():
        pass


    
class Accounting(IDepartment):

    def __init__(self,employees):
        self.employees = employees

    def print_department(self,):
        print(f'accounting department : {self.employees}')


class Development(IDepartment):

    def __init__(self,employees):
        self.employees = employees

    def print_department(self,):
        print(f'development department : {self.employees}')

class ParentDepartment(IDepartment):
    def __init__(self,employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add(self,dept):
        self.sub_depts.append(dept)
        self.employees += dept.employees


    def print_department(self):
              print("parent department base employees:" + str(self.base_employees))

              for dept in self.sub_depts:
                  dept.print_department()

              print(f'total of employees: {self.employees}')

                
dept1 = Accounting(200)
dept2 = Development(170)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)          
parent_dept.add(dept2)


parent_dept.print_department()
