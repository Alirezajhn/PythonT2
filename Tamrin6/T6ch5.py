import itertools
import operator

expert_List1 = [("Ali","Ahmadi","M",35), ("Sima","Sadri","C",39), ("Ahmad","Moradi","M",30), ("Ftemeh","Majd","C",29), ("Sara","Biglar","IE",27), ("Reza","Rahnama","EE",45)]
expert_List2 = [("Mina","Gohari","EE",40), ("Iman","Shams","M",26), ("Farzad","Yeganeh","M",41), ("Ali","Imani","C",33), ("Aref","Alameh","M",32), ("Narges","Sohrabi","C",35)]
def ExpertList():
    mainList=list(itertools.chain.from_iterable([expert_List1,expert_List2]))
    sortedMainList=sorted(mainList,key=operator.itemgetter(2))
    return sortedMainList

def creatGroup():
    mathList=list(itertools.compress(ExpertList(),[0,0,0,0,0,0,0,0,1,1,1,1,1]))
    groupList=list(itertools.combinations(mathList,3))
    return groupList

# print("Name\tFamily\tMajor\tAge")
# for expert in ExpertList():
#     for information in expert:
#         print(information,end="\t")
#     print()
    
for group in creatGroup():
    print(group)
# print(creatGroup())
