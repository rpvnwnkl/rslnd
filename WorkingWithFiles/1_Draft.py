file = open('./paragraphToRead.txt')
paragraphList = []
for line in file:
    paragraphList.append(line.strip('\n'))
##print paragraphList
for line in range(1, (len(paragraphList)+1)):
    if line % 2 == 0:
        print paragraphList[line-1]
