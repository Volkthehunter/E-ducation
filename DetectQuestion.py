import string

def removeCharAt(index, string):
    return string[:index] + string[index+1:]

def detectQuestion(fileNameToRead, fileNameToWrite):
    qWord = ['question', 'questions', 'assignment', 'quiz', 'exercise', 'exercises']
    fr = open(fileNameToRead, 'r')
    fw = open(fileNameToWrite, 'w')
    text = fr.readlines()
    index = 0
    for elem in text:
        index += 1
        elem = elem.lower().strip('\n')
        if(elem in qWord):
            break
    for i in range(index, len(text)):
        fw.write(text[i])
    fr.close()
    fw.close()
    
def detectIntChangeable(someString):
    try:
        int(someString)
    except:
        return False
    else:
        return int(someString)
   
def analyseQuestion(question):#Rough Version
    YesNoIndicator = [Is, Am, Are, Was, Were, Do, Does, Did]
    DescribeIndicator = ['What', 'When', 'Where', 'How', 'Which']
    for elem in question:
        if(elem[0] in YesNoIndicator):
            qType = YesNo
        elif(elem[0] in DescribeIndicator):
            qType = Describe
        elif(elem[0] in ['Why', 'Compare']):
            qType = Compare
    return qType
    
    
def formQuestion(fileNameToRead, fileNameToWrite):
    qWord = ['question', 'questions', 'assignment', 'quiz', 'exercise', 'exercises']
    fr = open(fileNameToRead, 'r')
    fw = open(fileNameToWrite, 'w')
    text = fr.readlines()
    questionList = []
    index = 0
    for elem in text:
        index += 1
        elem = elem.lower().strip('\n')
        if(elem in qWord):
            break
    for i in range(index, len(text)):
        questionList.append(text[i])
    
    i = 0
    for elem in questionList:
        elem = elem.strip('\n')
        if(elem[1] in [',', '.', '\)']):
            questionList[i] = removeCharAt(1, elem)
        if(detectIntChangeable(elem[0]) != False):
            questionList[i] = removeCharAt(0, questionList[i])
        elif(elem[0] in list(string.ascii_lowercase) or elem[0] in list(string.ascii_uppercase)):
            questionList[i] = removeCharAt(0, text[i])
        questionList[i] = questionList[i].lstrip()
        i += 1
        
    for elem in questionList:
        fw.write(elem + '\n')
    fr.close()
    fw.close()

#analyseQuestion('temp.txt', 'QuestionFromText.txt')
#print(detectIntChangeable('18'))
