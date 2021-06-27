class Solution:
    def validateStackSequences(self, pushed, popped):
        i = 0 # popped index
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == len(popped) # all elements in [popped] are popped

if __name__ == '__main__':
    sol = Solution()

    # # test 1
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print(sol.validateStackSequences(pushed, popped))
    
    # # # test 2
    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    print(sol.validateStackSequences(pushed, popped))
