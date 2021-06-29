class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s

        palin = s[0]
        for i in range(n-1):
            b = 1 # start from length 3
            while i - b >= 0 and i + b < n:
                if s[i-b] == s[i+b]:
                    if 2*b+1 > len(palin):
                        palin = s[i-b:i+b+1]
                else:
                    break
                b += 1
            
            j = i + 1
            b = 0 # start from length 2
            while i - b >= 0 and j + b < n:
                if s[i-b] == s[j+b]:
                    if 2*(b+1) > len(palin):
                        palin = s[i-b:j+b+1]
                else:
                    break
                b += 1
        
        return palin

# -----tests-----
if __name__ == '__main__':
    sol = Solution()

    # test 1
    s = "aaaa"
    print(sol.longestPalindrome(s))
    
    # test 2
    s = "cbbd"
    print(sol.longestPalindrome(s))
