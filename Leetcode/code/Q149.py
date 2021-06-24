from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        dd = defaultdict(set)
        n = len(points)
        for i in range(n-1):
            for j in range(i+1, n):
                if points[j][0] == points[i][0]:
                    dd[(math.inf, points[j][0])].add(tuple(points[i]))
                    dd[(math.inf, points[j][0])].add(tuple(points[j]))
                else:
                    k = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    b = points[i][1] - k * points[i][0]
                    dd[(k, b)].add(tuple(points[i]))
                    dd[(k, b)].add(tuple(points[j]))
        return max([len(s) for s in dd.values()])

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = [[1,1],[2,2],[3,3]]
    print(sol.maxPoints(t1))
    
    # test 2
    t2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print(sol.maxPoints(t2))
