#return in list of type and question
def findQuestion(index):
    f = open('Questions.txt','r')
    Qlist=f.readlines()
    return Qlist[int(index-1)].strip('\n').split('@')
    f.close()

#return value in list type with strings inside
def findKey(index):
    g = open('Keys.txt','r')
    Keylist = g.readlines()
    k = Keylist[int(index)-1]
    k = k.strip('\n').split('/')
    return k
    g.close()
    
def findKeyPlus(index):
    k = findKey(index)
    for i in range(len(k)):
        k[i] = k[i].split(', ')
    return k
    
  
#question type
  #YesNo : Answer Yes or No
  #Compare : Main/What thing to compare with/what type to compare/0(Equal), 1(More than)
  #describe : Must have word/Restricted word

#print(findKey(1))
#print(findKey(2))
#print(findKeyPlus(3))