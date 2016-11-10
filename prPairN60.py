__author__ = 'vikram'


def findPrime(start, stop):
    """
    :rtype : list
    """

    pList = []
    for x in range(start, stop):
        isPrime = 1
        for y in range(2, x):
            if (x % y) == 0:
                isPrime = 0
        if isPrime == 1:
            pList.append(x)
    return pList
def isItPrime(numList):
    """
    :rtype : list
    """

    pList = []
    for x in numList:
        isPrime = 1
        for y in range(2, x):
            if (x % y) == 0:
                isPrime = 0
        pList.append(isPrime)
    return pList

print findPrime(800, 900)

fourList = ["3", "7", "109", "673"]
combPlist = []
for x in range(0, len(fourList)):
    for y in range(0, len(fourList)):
        if (x != y):
            combPlist.append(int(fourList[x] + fourList[y]))

print combPlist
print isItPrime(combPlist)
if 0 not in combPlist:
    print "all are primes!!"

