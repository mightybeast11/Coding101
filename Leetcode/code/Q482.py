class Solution:
    def licenseKeyFormatting(self, s, k):
        d = []
        count = k
        s = "".join(s.split("-"))
        for ch in s[::-1]:
            ch = ch.upper()
            if count > 0:
                d.append(ch)
                count -= 1
            else:
                d.append("-")
                d.append(ch)
                count = k - 1
        return "".join(d)[::-1]

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = "5F3Z-2e-9-w"
    print(sol.licenseKeyFormatting(t1, 4))
    
    # test 2
    t2 = "2-5g-3-J"
    print(sol.licenseKeyFormatting(t2, 2))
