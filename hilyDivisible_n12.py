__author__ = 'vikram'
import math

def findDivisors(num):
    allFctrs = []
#        for y in range(2, int(num/2) + 1):
    for y in range(2, int(math.sqrt(num)) + 1):
        if num % y == 0:
            allFctrs.append(y)
    return len(allFctrs) * 2 + 2

def triangleNum(base):
    return base * (base + 1)/2

'''num = 280000000000000
print '{2}{0}{1}'.format(' num of divisors of ', num, findDivisors(num))
'''
base = 10
print '{0}{1}{2}{3}'.format('triangle num of ', base, ' is ', triangleNum(base))
while findDivisors(triangleNum(base)) < 501:
    base += 1
print '{0}{1}{2}{3}'.format('triangle num of ', base, ' is ', triangleNum(base))
print '{0}{1}{2}{3}'.format(triangleNum(base), ' has ', findDivisors(triangleNum(base)), ' factors ')



