from collections import defaultdict
from itertools import combinations

class Solution:
    def combinationSum3(self, k, n):
        return list(filter(lambda l: sum(l)==n, combinations([i for i in range(1, 10)], k)))


if __name__ == '__main__':
    sol = Solution()

    # test 1

    print(sol.combinationSum3(9,6))
    
    # test 2

    print(sol.combinationSum3(3,9))
