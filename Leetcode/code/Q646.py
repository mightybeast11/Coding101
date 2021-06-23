class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [1] * n

        for j in range(n):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = [[1,2], [2,3], [3,4]]
    print(sol.findLongestChain(t1))
    
    # test 2
    t2 = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]
    print(sol.findLongestChain(t2))
