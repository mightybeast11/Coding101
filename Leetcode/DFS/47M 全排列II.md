# 回溯

Time: O(n * n!), 回溯复杂度是O(n!), 拷贝每个排列数组的复杂度是O(n)
Space: O(n), 递归栈

```python
class Solution:
    def permute(self, nums):
        def backtrack(depth):
            if depth == n:
                permutations.add(tuple(nums))
                return
            for i in range(depth, n):
                nums[depth], nums[i] = nums[i], nums[depth]
                backtrack(depth + 1)
                nums[i], nums[depth] = nums[depth], nums[i]

        n = len(nums)
        permutations = set()
        nums.sort()
        backtrack(0)
        return [list(p) for p in permutations]
```

类似Q46的做法, 只是用set保证不重复.

注意set中元素为tuple而不是list, 因为list is not hashable.