import re

class Solution:
    def isNumber(self, s):
        # regex = re.compile("^[+-]?(?:\\d+\\.?\\d*|\\.\\d+)(?:[Ee][+-]?\\d+)?$") # regular string
        regex = re.compile(r"^[+-]?(?:\d+\.?\d*|\.\d+)(?:[Ee][+-]?\d+)?$") # raw string
        result = regex.match(s) # a Match object (always True) or None
        if result == None:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = "0e"
    print(sol.isNumber(t1))
    
    # test 2
    t2 = ".1"
    print(sol.isNumber(t2))


    # Sequential decomposition
    "^" # start of string

    "[+-]?" # 0 or 1 sign, optional
    "(?:)" # non-captureing group
    "\\d+" # at least 1 digit. The start of int or float (with int part)
    "\\.?" # 0 or 1 dot, optional. If 0 then int, if 1 then float (with int part)
    "\\d*" # 0 or more digit. Can be later part of int, or just decimal part of float.

    "()?" # 0 or 1 exponential part, optional
    "[Ee]" # must have exactly 1, can be either E or e

    "$" # end of string
