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

# -----tests-----
if __name__ == '__main__':
    sol = Solution()

    # test 1
    nums = [1,1,3]
    print(sol.permute(nums))
