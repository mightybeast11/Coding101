class Solution:
    def maxAbsoluteSum(self, nums):
        accumulation = [0]
        for i in nums:
            accumulation.append(accumulation[-1] + i)
        return max(accumulation) - min(accumulation)

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = [1,-3,2,3,-4]
    print(sol.maxAbsoluteSum(t1))
    
    # test 2
    t2 = [2,-5,1,-4,3,-2]
    print(sol.maxAbsoluteSum(t2))
