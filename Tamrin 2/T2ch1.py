class company:
    def __init__(self,nameCompany,nameManager,address,countOfEmployee,revenue):
        self.__nameCompany=nameCompany
        self.__nameManager=nameManager
        self.__address=address
        self.__countOfEmployee=countOfEmployee
        self.__revenue=revenue
        
        
    @property
    def nameCompany(self):
        return self.__nameCompany
    @nameCompany.setter
    def nameCompany(self,newNameCompany):
        self.__nameCompany=newNameCompany

    @property
    def nameManager(self):
        return self.__nameManager
    @nameCompany.setter
    def nameCompany(self,newNameManager):
        self.__nameCompany=newNameManager

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self,newAddresss):
        self.__address=newAddresss
        
    
    @property
    def countOfEmployee(self):
        return self.__countOfEmployee
    @address.setter
    def countOfEmployee(self,newcountOfEmployee):
        self.__countOfEmployee=newcountOfEmployee
        
        
    @property
    def revenue(self):
        return self.__revenue
    @address.setter
    def revenue(self,newrevenue):
        self.__revenue=newrevenue
        
    
    def __str__(self):
        return f"NameCompany: {self.__nameCompany}\t nameManager :{self.__nameManager}\taddress:{self.__address}\tcountOfEmployee: {self.__countOfEmployee}\t revenue:{self.__revenue}"
    
    def productivityCalc(self):
        return self.__revenue/self.__countOfEmployee
    
    
    
c1=company("apple","steveJobs","Usa",200,100000000)
print(c1)
print(c1.productivityCalc())
    
    
    
    