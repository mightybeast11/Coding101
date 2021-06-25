from collections import deque, defaultdict

class Solution:
    def openLock(self, deadends, target):
        # edge cases
        start = "0000"
        if target == start:
            return 0
        if start in deadends:
            return -1

        # 2-way bfs
        d1, d2 = deque(), deque()
        d1.append(start)
        d2.append(target)
        m1,m2 = defaultdict(int), defaultdict(int)
        m1[start] = 0
        m2[target] = 0

        while d1 and d2:
            step = -1
            if len(d1) <= len(d2):
                step = self.search(d1, m1, m2, deadends)
            else:
                step = self.search(d2, m2, m1, deadends)
            if step != -1:
                return step # the shortest path is found
        
        return -1 # no path is found after all search

    def search(self, deque, cur, other, deadends):
        combo = deque.popleft()
        for i in range(4):
            for j in range(-1, 2, 2): # 1 and -1
                new = combo[0:i] + str((int(combo[i]) + j) % 10) + combo[i+1:4]
                if new in deadends:
                    continue
                if new in cur.keys():
                    continue
                if new in other.keys():
                    return cur[combo] + 1 + other[new] # the shortest path is found
                else:
                    deque.append(new)
                    cur[new] = cur[combo] + 1

        return -1 # no path is found after current loop


if __name__ == '__main__':
    sol = Solution()

    # test 1
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(sol.openLock(deadends, target))
    
    # test 2
    deadends = ["0000"]
    target = "8888"
    print(sol.openLock(deadends, target))
