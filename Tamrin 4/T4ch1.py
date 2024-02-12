class Student:
    nameSchool="allameh"
    def __init__(self,studentCode,name,family,level):
        self.__studentCode=studentCode
        self.__name=name
        self.__family=family
        self.__level=level
        
    @staticmethod
    def showCoursesByLevel(level):
        if level==1:
            courselist1=["C1","C2","C3","C4","C5"]
            for course in courselist1:
                print(course,end=" ")
        elif level==2:
            courselist2=["C1","C2","C3","C4","C5","C6"]
            for course in courselist2:
                print(course,end=" ")
        elif level==3:
            courselist3=["C1","C2","C3","C4","C5","C6","C7"]
            for course in courselist3:
                print(course,end=" ")
        elif level==4:
            courselist4=["C1","C2","C3","C4","C5","C6","C7","C8"]
            for course in courselist4:
                print(course,end=" ")
        elif level==5:
            courselist5=["C1","C2","C3","C4","C5","C6","C7","C8","C9"]
            for course in courselist5:
                print(course,end=" ")
        elif level==6:
            courselist6=["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10"]
            for course in courselist6:
                print(course,end=" ")
    
    @classmethod
    def changeNameSchool(cls,newNameSchool):
        Student.nameSchool=newNameSchool
        return Student.nameSchool
    
    def __hash__(self):
        return hash(self.__studentCode)+hash(self.__name)+hash(self.__family)+hash(self.__level)
    
    def __str__(self):
        return f"studentCode:{self.__studentCode}\tname:{self.__name}\tfamily:{self.__family}\tlevel:{self.__level}"
    
    def __eq__(self,obj2):
        if not isinstance(obj2,Student):
            return False
        return self.__studentCode==obj2.__studentCode and self.__name==obj2.__name and self.__family==obj2.__family and self.__level==obj2.__level
    


studentSet=set()
for i in range(2):
    studentCode=int(input("studentCode: "))
    name=input("name: ")
    family=input("family: ")
    level=input("level: ")
    student=Student(studentCode,name,family,level)
    studentSet.add(student)
    
print("----------------------------")
print("listOfStudent:")
for student in studentSet:
    print(student)
print("----------------------------")
level=input("Enter level:")
print(f"level {level}:")
Student.showCoursesByLevel(int(level))

print()
print(f"studentName:{Student.nameSchool}")
print("----------------------------")
print("changeNameschool:",Student.changeNameSchool("alimola"))