from datetime import date,datetime,time,timedelta
from khayyam import *

def generateJalaliTOMiladi():
    date1=input("Enter Date (For Example: 1399-06-20):")
    date2=datetime.strptime(date1,"%Y-%m-%d")
    date3=JalaliDate(date2.year,date2.month,date2.day)
    gregorianDate=date3.todate()
    gregorianDate2=date.today()
    days=abs(gregorianDate-gregorianDate2).total_seconds()/(24*60*60)
    yield gregorianDate2
    yield days
    
for item in generateJalaliTOMiladi():
    print(item)

    

    
    

    