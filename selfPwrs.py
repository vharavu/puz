__author__ = 'vikram'

pwrSum = 0
for self in range(1, 1001):
    pwrSum += self**self
pwrSum = str(pwrSum)
print pwrSum[-10:]
