class Counter:
    def __init__(self,startNum,endNum):
        self.__startNum=startNum
        self.__endNum=endNum
        
        
    def __iter__(self):
      return self
  
    def __next__(self):
        self.__startNum+=3
        if self.__startNum>self.__endNum:
            raise StopIteration
        return self.__startNum
    
    def __str__(self):
        return f"{self.__startNum}"
c1=Counter(10,100)

for counter in c1:
    print(c1)