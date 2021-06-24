class Solution:
    def makeEqual(self, words):
        k = len(words)
        if k == 1:
            return True

        whole = "".join(words)
        n = len(whole)
        if n % k != 0:
            return False

        whole = sorted(whole)
        counts = [len(set(whole[i:i+k])) for i in range(0, n, k)]
        return counts == [1] * (n // k)

if __name__ == '__main__':
    sol = Solution()

    # test 1
    t1 = ["abc","aabc","bc", "abc"]
    print(sol.makeEqual(t1))
    
    # test 2
    t2 = ["a","a","a"]
    print(sol.makeEqual(t2))
