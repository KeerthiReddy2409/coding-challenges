import math

class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        root = int(math.isqrt(n))
        if root * root != n:
            return False
        for i in range(2, int(math.isqrt(root)) + 1):
            if root % i == 0:
                return False
        return True

        #if p is prime number then 1,p,p**2 these will only have three divisors so sqrt p should be prime 