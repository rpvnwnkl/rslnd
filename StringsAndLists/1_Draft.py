file = open('./humptydumpty.txt')
testString = file.readline()
indices = file.readline()
indices = indices.split(' ')
print indices[0]
print type(indices[0])
print indices[1]
print indices[2]
print indices[3]

newWord = testString[int(indices[0]):(int(indices[1]) + 1)] + \
              ' ' + testString[int(indices[2]):(int(indices[3]) + 1)]
print newWord
