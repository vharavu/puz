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
            continue
        elif x % 3 == 0:
            isPrime = 0
            continue
        else:
            for y in range(5, int(math.sqrt(x)) + 1, 2):
                if (x % y) == 0:
                    isPrime = 0
                    break
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
        elif x % 3 == 0:
            isPrime = 0
        else:
            for y in range(5, int(math.sqrt(x)) + 1, 2):
                if (x % y) == 0:
                    isPrime = 0
                    print '{0}{1}{2}{3}'.format('divisor of ', x, ' is = ', y)
        pList.append(isPrime)
        if isPrime == 0:
            break
    return pList


#print findPrime(600, 700)
samplePrList = findPrime(3, 10000)
#samplePrList = findPrime(129976600, 129976700)
print '{0}{1}'.format('number of primes in given range is -- ', len(samplePrList))
fourList = ["3", "7", "109", "673"]
combPlist = []
for n in range(0, len(samplePrList)):
    print n
    combPlist = []
    fourList.append(str(samplePrList[n]))
    print(fourList)
    for x in range(0, len(fourList) - 1):
        combPlist.append(int(fourList[x] + fourList[-1]))
        combPlist.append(int(fourList[-1] + fourList[x]))
    print combPlist
    resultList = isItPrime(combPlist)
    print(resultList)
    if 0 in resultList:
        del fourList[-1]
    else:
        print "all are primes!!"
        print fourList
        ps = 0
        for final in range(0, len(fourList)):
            ps += int(fourList[final])
        print '{0}{1}'.format('Sum of special primes is ', ps)
        break
