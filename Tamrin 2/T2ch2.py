class Person:
    def __init__(self,name,family):
        self.__name=name
        self.__family=family

    def _ShowPersonInfo(self):
        return f"name :{self.__name}\t family :{self.__family}"
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,newName):
        self.__name=newName
        
    @property
    def family(self):
        return self.__family
    @family.setter
    def name(self,newFamily):
        self.__family=newFamily
    
#-----------------------------------------
class Manager(Person):
    managerCount=0
    def __init__(self, name, family,managerCode,salaryManager):
        super().__init__(name, family)
        self.__managerCode=managerCode
        self.__salaryManager=salaryManager
        Manager.managerCount+=1
        
    @property
    def managercode(self):
        return self.__managerCode
    @managercode.setter
    def managerCode(self,newMangerCode):
        self.__managerCode=newMangerCode
    @property
    def salaryManager(self):
        return self.__salaryManager
    @salaryManager.setter
    def salaryManager(self,newsalaryManager):
        self.__salaryManager=newsalaryManager
        
    def ShowManagerInfo(self):
        return f"managerCode:{self.__managerCode} \t Fullname:{self._ShowPersonInfo()} \t salaryManager:{self.__salaryManager}"
#-----------------------------------------
class Employee(Person):
    employeeCount=0
    def __init__(self,name,family,employeeCode,rank):
        super().__init__(name,family)
        self.__employeeCode=employeeCode
        self.__rank=rank
        Employee.employeeCount+=1
    
    @property
    def employeeCode(self):
        return self.__employeeCode
    @employeeCode.setter
    def employeeCode(self,newEmployeecode):
        self.__employeeCode=newEmployeecode
    @property
    def salaryEmployee(self):
        return self.__salaryEmployee
    @salaryEmployee.setter
    def salaryEmployee(self,newsalaryEmployee):
        self.__salaryEmployee=newsalaryEmployee 
           
    def showEmployeeInfo(self):
        return f"EmployeeCode:{self.__employeeCode} \t Fullname:{self._ShowPersonInfo()} \t rank:{self.__rank}"
#-----------------------------------------
class Intern(Person):
    internCount=0
    def __init__(self,name,family,internCode,internShipTime):
        super().__init__(name,family)
        self.__internCode=internCode
        self.__internShipTime=12
        Intern.interCount+=1
    
    
    def showInternInfo(self):
        return f"InternCode:{self.__internCode} \t Fullname:{self._ShowPersonInfo()} \t internShipTime:{self.__internShipTime}"
#-----------------------------------------       
   
managerList=[]
m1=Manager("ali","jahangard",1,200000)
m2=Manager("alireza","jahangard",2,300000)
m3=Manager("danial","jahangard",3,400000)
managerList.append(m1)
managerList.append(m2)
managerList.append(m3)
# for manager in managerList:
#     print(manager.ShowManagerInfo())

print(Manager.managerCount)

m1.salaryManager=500000
for manager in managerList:
    print(manager.ShowManagerInfo())


