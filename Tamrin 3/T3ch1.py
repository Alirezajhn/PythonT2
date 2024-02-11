class ProgrammingLanguageCourse:
        def __init__(self,courseName,startDateCourse,endDateCourse,teacherCourse,levelCourse):
             self._courseName=courseName
             self._startDateCourse=startDateCourse
             self._endDateCourse=endDateCourse
             self._teacherCourse=teacherCourse
             self._levelCourse=levelCourse
             self.courseSchedule=[]
             
        
           
             
        def addDay(self,day):
            self.courseSchedule.append(day)
            
        def _showCourseInfo(self):
            return f"courseName:{self._courseName}\tstartDateCourse:{self._startDateCourse}\tendDateCourse:{self._endDateCourse}\tteacherCourse:{self._teacherCourse}\tlevelCourse:{self._levelCourse}"
#-----------------------------------------------------------   
class Python(ProgrammingLanguageCourse):
        def __init__(self, courseName, startDateCourse, endDateCourse, teacherCourse, levelCourse,pythonCode,pythonFee):
             super().__init__(courseName, startDateCourse, endDateCourse, teacherCourse, levelCourse)
             self.__pythonCode=pythonCode
             self.__pythonFee=pythonFee
             
        def showPythonInfo(self):
            print(f"pythonCode:{self.__pythonCode}")
            print(self._showCourseInfo())
            print(f"pythonFee:{self.__pythonFee}")
            for day in self.courseSchedule:
                print(day,end=" ")
            
            
        def __str__(self):
             return f"pythonCode:{self.__pythonCode}\tcourseName:{self._courseName}\tteacherCourse:{self._teacherCourse}\tlevelCourse:{self._levelCourse}\tpythonFee:{self.__pythonFee}"

#-----------------------------------------------------------
class Java(ProgrammingLanguageCourse):
        def __init__(self, courseName, startDateCourse, endDateCourse, teacherCourse, levelCourse,javaCode,javaFee):
             super().__init__(courseName, startDateCourse, endDateCourse, teacherCourse, levelCourse)
             self.__javaCode=javaCode
             self.__javaFee=javaFee
             
        def showJavaInfo(self):
            print(f"javaCode:{self.__javaCode}")
            print(self._showCourseInfo())
            print(f"javaFee:{self.__javaFee}")
            for day in self.courseSchedule:
                print(day,end=" ")
            
            
        def __str__(self):
             return f"javaCode:{self.__javaCode}\tcourseName:{self._courseName}\tteacherCourse:{self._teacherCourse}\tlevelCourse:{self._levelCourse}\tjavaFee:{self.__javaFee}"

#-----------------------------------------------------------
class Php(ProgrammingLanguageCourse):
        def __init__(self, courseName, startDateCourse, endDateCourse, teacherCourse, levelCourse,phpCode,phpFee):
             super().__init__(courseName, startDateCourse, endDateCourse, teacherCourse, levelCourse)
             self.__phpCode=phpCode
             self.__phpFee=phpFee
             
        def showPhpInfo(self):
            print(f"phpCode:{self.__phpCode}")
            print(self._showCourseInfo())
            print(f"phpFee:{self.__phpFee}")
            for day in self.courseSchedule:
                print(day,end=" ")
            
            
        def __str__(self):
             return f"phpCode:{self.__phpCode}\tcourseName:{self._courseName}\tteacherCourse:{self._teacherCourse}\tlevelCourse:{self._levelCourse}\tphpFee:{self.__phpFee}"

#-----------------------------------------------------------
#main
p1=Python('p1',"2024/2/11","2024/2/14","abbassi","basic",1,5000000)
p2=Python('p2',"2024/2/12","2024/2/18","ahmadi","advance",2,8000000)
p1.addDay("Saturday")
p2.addDay("Sunday")
p1.addDay("Monday")
p2.addDay("Tuesday")
p1.showPythonInfo()
print()
print(120*"*")
p2.showPythonInfo()
print()
print(120*"*")
j1=Java('j1',"2024/2/15","2024/2/20","mohammadi","basic",1,4000000)
j2=Java('j2',"2024/2/20","2024/2/30","rezaei","advance",2,7000000)
j1.addDay("Saturday")
j2.addDay("Sunday")
j1.addDay("Monday")
j2.addDay("Tuesday")
j1.showJavaInfo()
print()
print(120*"*")
j2.showJavaInfo()
print()
print(120*"*")
courseList=[]
courseList.append(p1)
courseList.append(p2)
courseList.append(j1)
courseList.append(j2)
print("list of courses:")
for course in courseList:
     print(course)