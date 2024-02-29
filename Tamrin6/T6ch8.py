import collections
class Mystring(collections.UserString):
    def reverse(self):
        newstr=""
        for ch in range(len(self.data)-1,-1,-1):
             newstr+=self.data[ch]
             
        return newstr
    def insert(self,word1,word2):
        index=self.data.find(word1)
        return self.data[:index]+word2+" "+self.data[index:]        
        
mystring=Mystring("hello")
print(mystring.reverse())
mystring2=Mystring("python is open source language")
print(mystring2.insert("language","programming"))


         
        