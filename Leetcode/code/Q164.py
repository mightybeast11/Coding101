import math

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        
        minimum = min(nums)
        r = max(nums) - minimum
        n = len(nums)
        w = max(1, r // (n - 1)) # bucket width
        b = math.ceil(r / w) + 1 # number of buckets
        if b < 2:
            return 0
        buckets = [[] for _ in range(b)]
        
        for num in nums:
            bucket = (num - minimum) // w
            if not buckets[bucket]:
                buckets[bucket].append(num)
            elif num < min(buckets[bucket]):
                buckets[bucket].append(num)
            elif num > max(buckets[bucket]):
                buckets[bucket].append(num)
        
        gaps = []
        buckets = list(filter(lambda x: x != [], buckets))
        if len(buckets) < 2:
            return 0
        for i in range(1, len(buckets)):
            gaps.append(min(buckets[i]) - max(buckets[i-1]))
        return max(gaps)

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = [3,6,9,1] # 3
    print(sol.maximumGap(t1))
    
    # test 2
    t2 = [1, 10] # 9
    print(sol.maximumGap(t2))
