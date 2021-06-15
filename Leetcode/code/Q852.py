class Solution:
    def peakIndexInMountainArray(self, nums):
        left = 0
        right = len(nums) - 1
        index = -1

        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                index = mid
                break
            elif nums[mid] > nums[mid-1] and nums[mid] < nums[mid+1]: # ascending
                left = mid + 1
            else:
                right = mid - 1

        return index

if __name__ == '__main__':
    l1 = [0,1,0]
    l2 = [3,4,5,1]
    sol = Solution()
    print(sol.peakIndexInMountainArray(l1))
    print(sol.peakIndexInMountainArray(l2))
