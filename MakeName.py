def makeNames(name, initialNumber, finalNumber):
    nameFolder = []
    for i in range(initialNumber, finalNumber+1):
        temp = name + str(i)
        nameFolder.append(temp)
    return nameFolder

def makeName(name, Number):
    name = name + str(Number)
    return name
    