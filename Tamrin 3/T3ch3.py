productPriceList1=[5000,10000,15000,6000,25000,12000,14000,10000,7000,20000]
productPriceList2=[4000,12000,16000,5000,22000,10000,16000,11000,5000,18000]
#------------------------------------------------------------------------------
class ProductPrice:
    def __init__(self,productPriceList):
        self.productPriceList=productPriceList
    def __add__(self,obj2):
        tempList=[]
        for i in range(0,len(self.productPriceList)):
            sumPrice=self.productPriceList[i]+obj2.productPriceList[i]
            tempList.append(sumPrice)
        return tempList
    
    def __sub__(self,obj2): 
        tempList=[]
        for i in range(0,len(self.productPriceList)):
            subPrice=self.productPriceList[i]-obj2.productPriceList[i]
            tempList.append(subPrice)
        return tempList
    
    def __mul__(self,number): 
        tempList=[]
        for i in range(0,len(self.productPriceList)):
            discountPrice=self.productPriceList[i]*number
            tempList.append(discountPrice)
        return tempList
    def __truediv__(self,number): 
        tempList=[]
        for i in range(0,len(self.productPriceList)):
            avgPrice=self.productPriceList[i]/number
            tempList.append(avgPrice)
        return tempList
    def __lt__(self,obj2): 
        tempList=[]
        for i in range(0,len(self.productPriceList)):
          tempList.append(self.productPriceList[i]<obj2.productPriceList[i])
        return tempList
#------------------------------------------------------------------------------
        
product1=ProductPrice(productPriceList1)    
product2=ProductPrice(productPriceList2)   
sumProduct=product1+product2
product3=ProductPrice(sumProduct)
avgPrice=product3/2
print("TheAvgPrices:")
print(avgPrice)

discountProduct1=product1*0.2    
discountProduct2=product2*0.2
product4=ProductPrice(discountProduct1)
product5=ProductPrice(discountProduct2)
discountProduct14=product1-product4
discountProduct25=product2-product5
product6=ProductPrice(discountProduct14)
product7=ProductPrice(discountProduct25)

sumDiscount=product6+product7
product8=ProductPrice(sumDiscount)
print("AvgwithDiscount:")
print(product8/2)

print("*"*120)

priceComparisonList=product1<product2

for item in priceComparisonList:
    tempList=[]
    if item==True:
        tempList.append(item)
        
if len(tempList)>5:
    print("Store 1 offers to customer better for less money" )
elif len(tempList)==5:
    print("NO diffrence")
else:
    print("Store 2 offers to customer better for less money")