file = open('./stringToRead.txt')
stringOfWords = file.read()
wordDict = {}
for word in stringOfWords.split(' '):
    if word.strip() in wordDict:
        wordDict[word.strip()] += 1
    else:
        wordDict[word.strip()] = 1
for key, value in wordDict.items():
    print key + ' ' + str(value)
