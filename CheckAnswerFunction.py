import KeyAndQuestion as kaq

def sentenceSeperator(ans):
    ans = ans.replace(', ',' ').strip('.')
    ans = ans.lower().split()
    return (ans)

def sentenceSeperatorPlus(ans):
    ans = ans.replace(', ','#').strip('.').split('#')
    i = 0
    for elem in ans:
        elem = elem.lower().split()
        ans[i] = elem
        i += 1
    return (ans)

def checkAns(index, ans):
    qType = kaq.findQuestion(index)[0]
    ansKey = kaq.findKey(index)
    ans = sentenceSeperator(ans)
    if(qType == 'YesNo'):
        if(ans == ansKey):
            return True
        else:
            return False
    elif(qType == 'Compare'):
        word = []
        for j in range(0, len(ans)):
            if(ans[j] == ansKey[0]):
                word.append(ans[j])
                for j0 in range(j, len(ans)):
                    word.append('<null>')
                break
            else:
                word.append('<null>')
        for j in range(0, len(ans)):
            if(ans[j] == ansKey[1]):
                word[j] = ans[j]
                break
        for i in range(len(word)-1, -1, -1):
            if(word[i] == '<null>'):
                del[word[i]]
        if(len(word) != 2 or ansKey[2] not in ans):
            return False
        if(ansKey[3] == '0' and 'equal' in ans):
            return True
        elif(ansKey[3] == '1'):
            if ('more' in ans and word[0] == ansKey[0]):
                return True
            elif ('less' in ans and word[0] == ansKey[1]):
                return True
            else:
                return False
        else:
            return False
    elif(qType == 'Describe'):
        ansKey = kaq.findKeyPlus(index)
        for elem in ansKey[0]:
            if elem not in ans:
                return False
        for elem in ansKey[1]:
            if elem in ans:
                return False
        return True