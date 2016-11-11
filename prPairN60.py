__author__ = 'vikram'
import math


def findPrime(start, stop):
    """
    :rtype : list
    """

    pList = []
    for x in range(start, stop):
        isPrime = 1
        if x % 2 == 0:
            isPrime = 0
        if x % 2 == 0:
            isPrime = 0
        for y in range(5, int(math.sqrt(x)) + 1, 2):
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
        # for y in range(2, x):
        if x % 2 == 0:
            isPrime = 0
        if x % 3 == 0:
            isPrime = 0
        for y in range(5, int(math.sqrt(x)) + 1, 2):
            if (x % y) == 0:
                isPrime = 0
        pList.append(isPrime)
    return pList


# print findPrime(673, 20000)
# samplePrList = findPrime(int(1e6), int(2e6))
samplePrList = findPrime(600, 700)
print len(samplePrList)
# fourList = ["3", "7", "109", "673"]
fourList = ["3", "7", "109"]
combPlist = []
for n in range(0, len(samplePrList)):
    print n
    combPlist = []
    fourList.append(str(samplePrList[n]))
    for x in range(0, len(fourList) - 1):
        combPlist.append(int(fourList[x] + fourList[-1]))
        combPlist.append(int(fourList[-1] + fourList[x]))
    # print combPlist
    # print isItPrime(combPlist)
    resultList = isItPrime(combPlist)
    if 0 in resultList:
        del fourList[-1]
    else:
        print "all are primes!!"
        print fourList
        break
