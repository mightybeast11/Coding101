class Solution:
    def myPow(self, x, n):
        def quickPower(n): # quickPower()是inner function, 所以不需要传递x作为参数
            if n == 0: # base case
                return 1.0
            sqrt = quickPower(n >> 1)
            return sqrt * sqrt if n % 2 == 0 else sqrt * sqrt * x
        return quickPower(n) if n >= 0 else 1 / quickPower(-n) # 注意这个-n
