import collections
import collections
studentList1 = [{"Name":"Ali Rezaee", "Age":25},{"Name":"Reza Ahmadi","Age":28},{"Name":"Sara Akbari","Age":25},{"Name":"Bahar Najafi","Age":23},{"Name":"Iman Mohamadi","Age":25},{"Name":"Sima Shaker","Age":25},{"Name":"Negin Ghazi","Age":29},{"Name":"Maryam Yaghoubi","Age":25},{"Name":"Mitra Sharif","Age":23},{"Name":"Ahmad Moradi","Age":25}]
studentList2 = [{"Name":"Amir Radi", "Age":23},{"Name":"Reza Ardakani","Age":23},{"Name":"Sima Sadr","Age":26},{"Name":"Bahman Najafi","Age":30},{"Name":"Mina Mohamadi","Age":23},{"Name":"Mitra Moradi","Age":23},{"Name":"Narges Arab","Age":30},{"Name":"Ali Eshtiyaghi","Age":32}]
newList1=[]
newList2=[]
for student in studentList1:
    newList1.append(student["Age"])

for student in studentList2:
    newList2.append(student["Age"])
 
i=1 
for list1 in (newList1,newList2):   
    listAge=collections.Counter(list1).most_common(1)
    print(f"Group:{i}:{listAge[0]}")
    i+=1

    

