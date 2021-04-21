# from itertools import permutations
# def permute(nums):
#     return list(map(list, permutations(nums, len(nums))))


# 感谢liweiwei1419的题解:
class Solution:
    def permute(self, nums):
        def dfs(nums, size, depth, path, used, res):
            # base case
            if depth == size:
                res.append(path[:]) # slicing to make a copy of path variable
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res) # recursion

                    used[i] = False # 回溯
                    path.pop() # 回溯

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)
