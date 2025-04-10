import random

class Prime(object):
    def __init__(self, num):
        self.num = num
    
    def isPrime(self):
        for i in range(2, self.num+1):
            if self.num % i == 0:
                break
        if i == self.num:
            return True
        else:
            return False

prime = Prime(random.randrange(2, 10))
print(f'{prime.num} is prime number') if prime.isPrime() else print(f'{prime.num} is not prime number')