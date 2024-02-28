import collections
Mobile=collections.namedtuple("Mobile","Name Model Price Colors")
m1=Mobile("apple","12","430000000",["red","blue","black","white"])
m2=Mobile("apple","13","530000000",["gold","blue","black","white"])
m3=Mobile("apple","14","630000000",["rose","blue","black","white"])
m4=Mobile("apple","15","730000000",["purple","blue","black","white"])
mobileList=[]
for mobile in (m1,m2,m3,m4):
    mobileList.append(mobile._asdict())
    
for m in mobileList:
    print(m)