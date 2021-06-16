# Adapt from:
# https://leetcode-cn.com/problems/stone-game/solution/shi-zi-you-xi-by-leetcode-solution/

class Solution:
    def stoneGame(self, piles):
        length = len(piles)

        # 1st dimention is l, 2nd dimension is r
        dp = [[0] * length for _ in range(length)] 

        # prepare base case
        for i, pile in enumerate(piles):
            dp[i][i] = pile

        # calculate general case
        for l in range(length - 2, -1, -1): # from 2nd last row to 1st row
            for r in range(l + 1, length): # from the column after diagonal to the last column
                dp[l][r] = max(piles[l] - dp[l + 1][r], piles[r] - dp[l][r - 1])
        
        return dp[0][length-1] > 0


if __name__ == '__main__':
    sol = Solution()

    # test 1
    l1 = [5,3,4,5]
    print(sol.stoneGame(l1))
    
    # test 2
    l2 = [3,2,10,4]
    print(sol.stoneGame(l2))
