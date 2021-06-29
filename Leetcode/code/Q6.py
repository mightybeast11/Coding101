class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        l = [[] for _ in range(numRows)]
        split = [[s[i:i+numRows], s[i+numRows:i+2*numRows-2]] for i in range(0, len(s), 2*numRows-2)]
        for p in split:
            for i, ch in enumerate(p[0]):
                l[i].append(ch)
            for i, ch in enumerate(p[1]):
                l[-2-i].append(ch)

        return "".join(["".join(i) for i in l])

# -----tests-----
if __name__ == '__main__':
    sol = Solution()

    # test 1
    s = "PAYPALISHIRING"
    numRows = 3
    print(sol.convert(s, numRows) == "PAHNAPLSIIGYIR")
    
    # test 2
    s = "PAYPALISHIRING"
    numRows = 4
    print(sol.convert(s, numRows) == "PINALSIGYAHRPI")
