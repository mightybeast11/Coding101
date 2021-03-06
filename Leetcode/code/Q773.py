from collections import deque, defaultdict

class Solution:
    def slidingPuzzle(self, board):
        end = [[1,2,3], [4,5,0]]
        if board == end:
            return 0

        # BFS
        d = deque() # [list of lists]
        d.append(end)
        m = defaultdict(int) # (tuple of tuples : int)
        m[tuple([tuple(i) for i in end])] = 0 

        while d:
            step = -1
            status = tuple([tuple(i) for i in d.popleft()]) # old status is tuple
            i, j = [(i, j.index(0)) for i, j in enumerate(status) if 0 in j][0]
                    
            for i_offset in range(-1, 2, 2):
                i_adj = i + i_offset
                if 0 <= i_adj <= 1:
                    step = self.adjacent(status, i, j, i_adj, j, board, d, m)
                    if step != -1:
                        return step
            for j_offset in range(-1, 2, 2): # i_offset can be -1 or 1
                j_adj = j + j_offset
                if 0 <= j_adj <= 2:
                    step = self.adjacent(status, i, j, i, j_adj, board, d, m)
                    if step != -1:
                        return step
        return -1

    def adjacent(self, status, i, j, i_adj, j_adj, board, d, m):
        new = list([list(i) for i in status]) # new is list
        new[i][j] = status[i_adj][j_adj]
        new[i_adj][j_adj] = status[i][j]
        if new == board: # found
            return m[status] + 1
        if tuple([tuple(i) for i in new]) in m.keys(): # overlap
            return -1
        else:
            d.append(new)
            m[tuple([tuple(i) for i in new])] = m[status] + 1
        return -1

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = [[1,2,3],[5,4,0]]
    print(sol.slidingPuzzle(t1))
    
    # test 2
    t2 = [[4,1,2],[5,0,3]]
    print(sol.slidingPuzzle(t2))
