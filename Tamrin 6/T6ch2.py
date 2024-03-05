def removeNum(func):
    def inner(*args ,**kargs):
        numberList1=list(*args)
        numberlist2=[]
        for number in numberList1:
            if type(number)==int and number>0:
                numberlist2.append(number)
        return numberlist2 
        
    return inner
        

@removeNum
def fact(numberList):
    numberListNew=[]
    for number in numberList:
        multi=1
        for number in range(number,0,-1):
            multi*=number
            numberListNew.append(multi)
    return numberListNew 
   
    
#------------------------------------


numberList=[4, 3, 8, 0, -3, -45, 2, 10, -16, 23, 9, 1, -6, 55, 3.4, 6, 11.5]

print(fact(numberList)) 
