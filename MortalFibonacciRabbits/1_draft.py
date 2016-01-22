file = open('./fiboNumbers.txt')
query = file.readline()
query = query.strip()
query = query.split(' ')
n = int(query[0])
m = int(query[1])

tally = {}
def fiboSequence(n, m):
    global tally
    if n <= 2:
        print 'first loop entered for n = ' + str(n)
        tally[n] = 1
        return 1
    elif n in tally:
        print 'found one we already had in here'
        print n
        print tally[n]
        return tally[n]
    elif n <= m:
        print 'entering fourth loop for n = ' + str(n)
        tally[n] = fiboSequence(n-1, m) + fiboSequence(n-2, m)
    else:
        print 'entering recurrent loop for n = ' + str(n)
        tally[n] = fiboSequence(n-1, m) + \
        fiboSequence(n-2, m) - fiboSequence(n-1-m, m)
            
##        tally[n] = 0
##        for i in range(1, m+1):
##            tally[n] += fiboSequence(n-i, m)
##    else:
##        return 0
##print fiboSequence(n, m)
for i in range(1,n+1):
    fiboSequence(i, m)
print 'answer is equal to: ' + str(tally[n])
