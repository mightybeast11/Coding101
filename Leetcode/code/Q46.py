class Solution:
    def permute(self, nums):
        def backtrack(depth):
            if depth == n:
                permutations.append(nums[:])
                return
            for i in range(depth, n):
                nums[depth], nums[i] = nums[i], nums[depth]
                backtrack(depth + 1)
                nums[i], nums[depth] = nums[depth], nums[i]

        n = len(nums)
        permutations = []
        backtrack(0)
        return permutations


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
