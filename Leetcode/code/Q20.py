class Solution:
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False

        stack = []

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            elif not stack:
                return False
            elif not (ord(last := stack.pop()) + 1 == ord(ch) or ord(last) + 2 == ord(ch)):
                return False

        return not bool(stack)

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = "()[]{}" # t
    print(sol.isValid(t1))
    
    # test 2
    t2 = "([)]" # f
    print(sol.isValid(t2))
