class Address:
    def __init__(self,nameTown,nameStreet,houseNumber):
        self.__nameTown=nameTown
        self.__nameStreet=nameStreet
        self.__houseNumber=houseNumber
        self.dicAddress={}
        
    def addAddressAtribute(self):  
        self.dicAddress["city"]=self.__nameTown
        self.dicAddress["street"]=self.__nameStreet
        self.dicAddress["NO"]=self.__houseNumber
        return self.dicAddress
    
    def showInfo(self):
        return f"nameTown:{self.__nameTown}\tnameStreet:{self.__nameStreet}\thouseNumber:{self.__houseNumber}"
#----------------------------------------------------------------------------------------------
class Person:
    def __init__(self,codeCustomer,name,family,phoneNumber,emailAddress):
        self.__codeCustomer=codeCustomer
        self.__name=name
        self.__family=family
        self.__phoneNumber=phoneNumber
        self.__emailAddress=emailAddress
        self.dicPerson={}
        
    def addPersonAtribute(self):  
        self.dicPerson["id"]=self.__codeCustomer
        self.dicPerson["name"]=self.__name
        self.dicPerson["family"]=self.__family
        self.dicPerson["phonenumber"]=self.__phoneNumber
        self.dicPerson["email"]=self.__emailAddress
        return self.dicPerson
    
    def showInfo(self):
        return f"codeCustomer:{self.__codeCustomer}\tname:{self.__name}\tfamily:{self.__family}\tphoneNumber:{self.__phoneNumber}\temailAddress:{self.__emailAddress}"
#----------------------------------------------------------------------------------------------
class Contact(Person,Address):
    def __init__(self,nameTown,nameStreet,houseNumber ,codeCustomer, name, family, phoneNumber, emailAddress):
        Address.__init__(self,nameTown,nameStreet,houseNumber)
        Person.__init__(self,codeCustomer, name, family, phoneNumber, emailAddress)
        self.contact={}
    def addAddressAndPersonDic(self):
        dic1=self.addPersonAtribute()
        dic2=self.addAddressAtribute()
        for dic in(dic1,dic2):
            self.contact.update(dic)
        return self.contact
    def showInfo(self):
        print(Person.showInfo(self))
        print(Address.showInfo(self))
        
#----------------------------------------------------------------------------------------------  
class PhoneBook:
    def __init__(self):
        self.phoneBook=[]
    
    def addContact(self,contact):
        self.phoneBook.append(contact)
        return self.phoneBook
    
    def showInfo(self):
        for contact in self.phoneBook:
            for key,value in contact.items():
                print(key,":",value,end=" ")
            print()
                
            
        
    def searchCustomer(self,family):
        tempList=[]
        for contact in self.phoneBook:
            if family==contact["family"]:
                tempList.append(contact)
        if tempList==[]:
            print("unknownPerson")
        else:
            for contact in tempList:
                contact=Contact(contact["city"],contact["street"],contact["NO"],contact["id"],contact["name"],contact["family"],contact["phonenumber"],contact["email"])
                contact.showInfo()
#-----------------------------------------------------------------------------------------------


contact1=Contact("sad","Teh","23",'1',"sara","solgi",'09120000000',"sara@")
contact2=Contact("khm","Teh","54",'2',"alireza","jahangard",'09120002300',"Alireza@")
contact3=Contact("rah","Teh","6",'3',"mohammad","jafari",'0912065000',"mhm@")
contactdic1=contact1.addAddressAndPersonDic()
contactdic2=contact2.addAddressAndPersonDic()
contactdic3=contact3.addAddressAndPersonDic()

phoneBook=PhoneBook()
phoneBook.addContact(contactdic1)
phoneBook.addContact(contactdic2)
phoneBook.addContact(contactdic3)
phoneBook.showInfo()
print("#"*120)

phoneBook.searchCustomer("solgi")
print("-"*120)
phoneBook.searchCustomer("jahangard")
print("-"*120)
phoneBook.searchCustomer("rezaei")
