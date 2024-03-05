import operator


str = """ Today, Richard Rael and Tony Riggs tell the story of American astronomer edwin hubble. He changed our ideas about the universe and how it developed.
Edwin hubble made his most important discoveries in the nineteen twenties. Today, other astronomers continue the work he began. Many of them are using the Hubble space telescope that is named after him.
Edwin Hubble was born in eighteen eighty-nine in Marshfield, Missouri. He spent his early years in the state of Kentucky. Then he moved with his family to Chicago, Illinois. He attended the University of Chicago. He studied mathematics and astronomy. """
listStr=str.split(".")

newlistStr=[]
for sentence in listStr:
    if operator.contains(sentence,"Edwin Hubble"):
        print(f"Edwin Hubble contains: \n{sentence}")
        print("*"*20)
                
for sentence in listStr:
    if  operator.contains(sentence,"edwin Hubble"):
        print(f"edwin Hubble:{sentence}")
        print("*"*20)
        newSentence1=sentence.replace("edwin Hubble","Edwin Hubble")
        newlistStr.append(newSentence1)
    elif operator.contains(sentence,"edwin hubble"):
        print(f"edwin hubble:{sentence}")
        print("*"*20)
        newSentence2=sentence.replace("edwin hubble","Edwin Hubble")
        newlistStr.append(newSentence2)
    elif operator.contains(sentence,"Edwin hubble"):
        print(f"Edwin hubble:\n{sentence}")
        print("*"*20)
        newSentence3=sentence.replace("Edwin hubble","Edwin Hubble")
        newlistStr.append(newSentence3)
    else: 
        newlistStr.append(sentence)
    
    
print(".".join(newlistStr))
print("*"*20)
        
         
        