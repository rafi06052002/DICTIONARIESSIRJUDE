# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 23:14:10 2020

@author: User
"""




#number1
def removekeys(mydict,keylist):
     for i in keylist:
        if i in mydict:
            mydict.pop(i)
            return mydict
                 
if __name__ ==  "__main__":
    dictionaries={'rafi':'single','cereal':'honey_stars','drink':'Aqua'}
    print(dictionaries)
    thekey=input('input the keys to remove:').split(',')
    print(removekeys(dictionaries,thekey))
    
#nomber2
def accept_login(users,username,password):
    if username in users:
        if users[username] == password:
            return True
    else:
        return False
           
         
if __name__ == "__main__":
    user1={'rafi':'12345','vacation':'covid19'}
    print('the secret:')
    myname1=input('username:')
    mypass1=input('password:')
    print(accept_login(user1,myname1,mypass1))
    
#nomber3
def findvalue(mydict,val):
    the_list=[]
    for key in mydict.keys():
        if val == mydict[key]:
            the_list.append(key)
    return the_list
        
if __name__ == "__main__":  
    dictionaries={'games':'r6','skill':'diedfirst','rafi':'1','max':'1','paul':'1'}
    inputed=input('the value that i want:')
    print(findvalue(dictionaries,inputed))
    
#nomber4
def wordfrequencies(mylist):
    the_dictionaries= {}
    for i in mylist:
        for word in i.split():
            the_dictionaries.setdefault(word,0)
            the_dictionaries[word] +=1
    return the_dictionaries
         
           
       
if __name__ == "__main__":
    string_list=['im','a','a','numero','rafi','champion']
    print(wordfrequencies(string_list))
    
#numero 5
def k_mer(DNA,thevalue):
    mydict1={}
    
    
    for x in range(len(DNA)):
        kmer = DNA [x:(k+x)]
        
        if len(kmer) == k:
            mydict1.setdefault(x+1,kmer)
    return mydict1
    
     
    
          
if __name__ == "__main__":
    theDNA='ACGAGGTACGAAGTTCG'
    k=int(input('thevalue:'))
    print(k_mer(theDNA,k))

#numro 6
def ROT_13(thetext):
    newborn=''
    
    key={'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m','A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z','N':'A','O':'B''P':'C','Q':'D','R':'E','S':'F','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M'}
    
    for x in range(len(thetext)):
        
        for i in thetext[x]:
            if i in sorted(key.keys()):
                newborn=newborn+str(key.get(i))
            else:
                newborn=newborn+i
            newborn=newborn + ''
    return newborn
    
    
    

if __name__=="__main__":
    print(ROT_13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))
               
#######

def rot13_decode(secret):
    key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
           'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
           'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
           'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
           'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}

    words = [words for words in secret.split()]
    results = []
    for word in words:
        results.append("".join([key[char] if char in key.keys() else char for char in word]))
    return " ".join(results)


if __name__ == "__main__":
    print (rot13_decode("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"))               

    


  


    
    
                  
    
    
    

    
    
    
   
    
    
    
    
  
    