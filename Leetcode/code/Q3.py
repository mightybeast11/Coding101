class Solution:
    def lengthOfLongestSubstring(self, s):
        i, j = 0, 0
        length = 0
        hashset = set()

        while j < len(s):
            if s[j] not in hashset:
                hashset.add(s[j])
                j += 1
                length = max(length, j - i)
            else:
                while s[i] != s[j]:
                    hashset.remove(s[i])
                    i += 1
                hashset.remove(s[i])
                i += 1
            
        return length

# -----test-----
if __name__ == '__main__':
    sol = Solution()

    # test 1
    s = "abcabcbb" # 3
    print(sol.lengthOfLongestSubstring(s))
    
    # test 2
    s = "tmmzuxt" # 5
    print(sol.lengthOfLongestSubstring(s))
