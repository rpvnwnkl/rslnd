
# coding: utf-8

# In[23]:

file = open('./haystack.txt')


# In[24]:

wholehaystack = file.readlines()


# In[25]:

hayStack = []
for strawLayer in wholehaystack:
    if strawLayer[0] != '>':
        hayStack[-1] += strawLayer.strip('\n')
    else:
        hayStack.append('')
print hayStack[0]
print 'hayStack[0] len = %s' % len(hayStack[0])
print len(hayStack)


# In[26]:

hayKey = hayStack[0]
start=0
stop=1
longestString = ''
while stop <= len(hayKey):
    nextUp = 1
    isFound = True
    searchKey = hayKey[start:stop]
    ##print searchKey
    while nextUp <= (len(hayStack) - 1) and isFound:
        ##if nextUp > len(hayStack)-1:
          ##  break
        if searchKey not in hayStack[nextUp]:
            #print 'not found'
            isFound = False
        else:
            ##print 'found, nextUp plus 1'
            nextUp+=1
    if isFound:
        if len(searchKey) > len(longestString):
            longestString = searchKey
            print 'longestString = %s' % longestString
            print 'longestString len = %s' % len(longestString)
        stop += 1
    else:
        start += 1
        stop = start
print longestString
    
        


# In[27]:

print longestString


# In[ ]:



