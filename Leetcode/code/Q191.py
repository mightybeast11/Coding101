class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = 0b00000000000000000000000000001011
    print(sol.hammingWeight(t1))
    
    # test 2
    t2 = 0b00000000000000000000000010000000
    print(sol.hammingWeight(t2))
