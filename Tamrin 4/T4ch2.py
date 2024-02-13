from abc import ABC,abstractclassmethod

class participant(ABC):
    def __init__(self,name,family,nationalCode,fuildStudy,address):
        self.__name=name
        self.__family=family
        self.__nationalCode=nationalCode
        self.__fieldStudy=fuildStudy
        self.__address=address
        
    @abstractclassmethod
    def calcFinalDegree():
        pass
    
    
    def showInfoParticipant(self):
        return f"name: {self.__name}\tfamily:{self.__family}\tnationalCode: {self.__nationalCode}\tfieldStudy: {self.__fieldStudy}\taddress: {self.__address}"
        
#--------------------------------------------------------------------------    
class FreeParticipant(participant):
    def __init__(self, name, family, nationalCode, fuildStudy, address,pfCode,interviewScore,writtenTestScore):
        super().__init__(name, family, nationalCode, fuildStudy, address)
        self.__pfCode=pfCode
        self.__interviewScore=interviewScore
        self.__writtenTestScore=writtenTestScore

    @property
    def interviewScore(self):
        return self.__interviewScore
    @interviewScore.setter
    def interviewScore(self,newInterviewScore):
        self.__interviewScore=newInterviewScore 
        
        
        
    @property
    def writtenTestScore(self):
        return self.__writtenTestScore   
    @writtenTestScore.setter
    def writtenTestScore(self,newWrittenTestScore):
        self.__writtenTestScore=newWrittenTestScore
    
    def __str__(self):
        return f"pfCode: {self.__pfCode}\t {self.showInfoParticipant()}\tScore: {self.calcFinalDegree()}"
    
    
    def calcFinalDegree(self):
        if(0<self.__interviewScore<100 and 0<self.__writtenTestScore<100):
            finalScore=(self.__interviewScore+self.__writtenTestScore)/2
            return finalScore
        else:
            print("unknownDegree")
        
    
#--------------------------------------------------------------------------
class Employee(participant):
    def __init__(self, name, family, nationalCode, fuildStudy, address,eCode,performanceScore,workingYears):
        super().__init__(name, family, nationalCode, fuildStudy, address)
        self.__eCode=eCode
        self.__performanceScore=performanceScore
        self.__workingYears=workingYears
    
    def __str__(self):
        return f"eCode: {self.__eCode}\t {self.showInfoParticipant()}\tScore: {self.calcFinalDegree()}"
    
    
    @property
    def performanceScore(self):
        return self.__performanceScore
    @performanceScore.setter
    def performanceScore(self,newPerformanceScore):
        self.__performanceScore=newPerformanceScore
        
        
        
    @property
    def workingYears(self):
        return self.__workingYears  
    @workingYears.setter
    def workingYears(self,newWorkingYears):
        self.__workingYears=newWorkingYears
                
    def calcFinalDegree(self):
        if(0<self.__performanceScore<100):
            if(1<=self.__workingYears<=5):
                self.__workingYears=0.1
            elif(5<self.__workingYears):
                self.__workingYears=0.2
            finalScore=self.__performanceScore+(self.__workingYears*self.__performanceScore)    
            return finalScore
      

#--------------------------------------------------------------------------
class SpecialParticipant(participant):
    def __init__(self, name, family, nationalCode, fuildStudy, address,psCode,greatPointAvg,univercityRank):
        super().__init__(name, family, nationalCode, fuildStudy, address)
        self.__psCode=psCode
        self.__greatPointAvg=greatPointAvg
        self.__univercityRank=univercityRank
    
    def __str__(self):
        return f"psCode: {self.__psCode}\t {self.showInfoParticipant()}\tScore: {self.calcFinalDegree()}"
    
    @property
    def greatPointAvg(self):
        return self.__greatPointAvg
    @greatPointAvg.setter
    def greatPointAvg(self,newGreatPointAvg):
        self.__greatPointAvg=newGreatPointAvg
       
    @property
    def univercityRank(self):
        return self.__univercityRank
    @univercityRank.setter
    def univercityRank(self,newUnivercityRank):
        self.__univercityRank=newUnivercityRank
    
    
    def calcFinalDegree(self):
        if(self.__univercityRank==1):
            self.__univercityRank=100
        elif(self.__univercityRank==2):
            self.__univercityRank=80
        elif(self.__univercityRank==3):
            self.__univercityRank=60
            
        if(16<=self.__greatPointAvg<=17.5):
            self.__greatPointAvg=60
        elif(17.5<=self.__greatPointAvg<=18.5):
            self.__greatPointAvg=80
        elif(18.5<self.__greatPointAvg):
            self.__greatPointAvg=100
            
        finalScore=(self.__greatPointAvg+self.__univercityRank)/2
        return finalScore
#--------------------main-------------------------------------
participantsList=[]
acceptedParticipantsList=[]

pf1=FreeParticipant("aa","bb","00","cc","dd","pf_1",80,97)
pf2=FreeParticipant("aa","bb","00","cc","dd","pf_2",70,80)
pf3=FreeParticipant("aa","bb","00","cc","dd","pf_3",85,90)
participantsList.append(pf1)
participantsList.append(pf2)
participantsList.append(pf3)

if pf1.calcFinalDegree()>=90:
    acceptedParticipantsList.append(pf1)
if pf2.calcFinalDegree()>=90:
    acceptedParticipantsList.append(pf2)
if pf3.calcFinalDegree()>=90:
    acceptedParticipantsList.append(pf3)

#------------------------------------------------------------------  
ps1=SpecialParticipant("aa","bb","00","cc","dd","pS_1",18.5,3)
ps2=SpecialParticipant("aa","bb","00","cc","dd","pS_2",19,1)
ps3=SpecialParticipant("aa","bb","00","cc","dd","pS_3",19,2)

participantsList.append(ps1)
participantsList.append(ps2)
participantsList.append(ps3)

if ps1.calcFinalDegree()>=90:
    acceptedParticipantsList.append(ps1)
if ps2.calcFinalDegree()>=90:
    acceptedParticipantsList.append(ps2)
if ps3.calcFinalDegree()>=90:
    acceptedParticipantsList.append(ps3)
#------------------------------------------------------------------  

e1=Employee("aa","bb","00","cc","dd","ee_1",88,5)
e2=Employee("aa","bb","00","cc","dd","ee_2",90,3)
e3=Employee("aa","bb","00","cc","dd","ee_3",70,6)
participantsList.append(e1)
participantsList.append(e2)
participantsList.append(e3)

if e1.calcFinalDegree()>=90:
    acceptedParticipantsList.append(e1)
if e2.calcFinalDegree()>=90:
    acceptedParticipantsList.append(e2)
if e3.calcFinalDegree()>=90:
    acceptedParticipantsList.append(e3)
    
#------------------------------------------------------------------

print("participantList:")
for p in participantsList:
    print(p)
print(100*"*")
print("AcceptedParticipantList:")
for p in acceptedParticipantsList:
    print(p)
print(100*"*")