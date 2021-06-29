class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict()
        for i, num in enumerate(nums):
            if target - num in d.keys():
                return [i, d[target - num]]
            d[num] = i
        return []
