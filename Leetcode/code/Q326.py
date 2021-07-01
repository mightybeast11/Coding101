class Solution:
    def isPowerOfThree(self, n):
        if n < 1: # edge case
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
