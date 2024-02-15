class MyEceptionHandling(Exception):
    def __init__(self,message):
        super().__init__()
        self.__message=message
        
    def __str__(self):
        return "Erorr: "+self.__message


class PlayerSelection:
    def __init__(self,id,age,height,weight):
        self.__id=id
        self.__age=age
        self.__height=height
        self.__weight=weight
        
    @staticmethod
    def checkFloat(number):
        try :
            float(number)
            return True
        except:
            return False
        
    @staticmethod
    def checkInt(number):
        try :
            int(number)
            return True
        except:
            return False
        
        
    def weightValidation(self):
        if not PlayerSelection.checkInt(self.__age):
            raise MyEceptionHandling("Age is not valid")
        
        if not (15<=int(self.__age)<=35):
            raise MyEceptionHandling("Age out of range This person is not allowed to register")
        else:
            if(15<=int(self.__age)<=25):
                if not PlayerSelection.checkFloat(self.__weight):
                    raise MyEceptionHandling("Weight is not valid")
            
                if not (60.00<=float(self.__weight)<=80.00):
                    raise MyEceptionHandling("Weight out of range This person is not allowed to register")
                return self.__weight
            
            elif(25<=int(self.__age)<=35):
                if not PlayerSelection.checkFloat(self.__weight):
                    raise MyEceptionHandling("Weight is not valid")
                
                if not (50.00<=float(self.__weight)<=75.00):
                    raise MyEceptionHandling("Weight out of range This person is not allowed to register")
                return self.__weight
            
            
    def heightValidation(self):
        if not PlayerSelection.checkInt(self.__height):
            raise MyEceptionHandling("Height is not valid")
        
        if not (170<=int(self.__height)<=190):
            raise MyEceptionHandling("Height out of range This person is not allowed to register")
        return self.__height
    
    def registerPalyer(self):
        try:
            self.weightValidation()
            self.heightValidation()
            return f"id: {self.__id}\tage: {self.__age} weight: {self.__weight}\t height: {self.__height}cm"
        except Exception as e:
            print(e)
    
#--------------------------------------main-----------------------------------
playerList=[]
while True:
    code=input("enter a code:")
    if not code=="0":
        age=input("enter a Age:")
        weight=input("enter a Weight:")
        height=input("enter a Height:")
        print("*****************")
        player=PlayerSelection(code,age,height,weight)
        playerList.append(player.registerPalyer())
    else:
        break
    
    print("The list of registered people:")
    for player in playerList:
        if player!=None:
            print(player)
    
    
        
            
