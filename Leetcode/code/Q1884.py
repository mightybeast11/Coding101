import math

class Solution:
    def twoEggDrop(self, n):
        return math.ceil((-1 + math.sqrt(1 + 8 * n)) / 2)

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = 2
    print(sol.twoEggDrop(t1))
    
    # test 2
    t2 = 100
    print(sol.twoEggDrop(t2))
