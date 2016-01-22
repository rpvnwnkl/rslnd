file = open('./numbersToSum.txt')
testNumbers = file.readline()
testNumbers = testNumbers.split(' ')
totalSum = 0.0
for x in range(int(testNumbers[0]), (int(testNumbers[1]) + 1)):
    if x % 2 == 1:
        totalSum += x

print totalSum
