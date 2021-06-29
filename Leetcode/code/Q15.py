class Solution:
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []

        sums = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                return sums
            if i != 0 and num == nums[i-1]: # duplicate 1st number
                continue

            l, r = i + 1, n - 1
            while l < r:
                if num + nums[l] + nums[r] == 0:
                    sums.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]: # duplicate 2nd number
                        l += 1
                    while l < r and nums[r] == nums[r-1]: # duplicate 3rd number
                        r -= 1
                    l += 1
                    r -= 1
                elif num + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return sums

# -----tests-----
if __name__ == '__main__':
    sol = Solution()

    # test 1
    nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))
