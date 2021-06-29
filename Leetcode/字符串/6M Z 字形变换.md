# 找规律

Time: O(n), 遍历string

Space: O(n), `split`分段存储的空间. ( `l`组成输出, 应该不算)

```python
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
```

遍历string, 分段存储, 按规律加入代表每行的list.

举例: 

-   输入: `s = "PAYPALISHIRING", numRows = 4`
-   执行: `split = [[s[i:i+numRows], s[i+numRows:i+2*numRows-2]]for i in range(0, len(s), 2*numRows-2)]`
-   返回: `split = [['PAYP', 'AL'], ['ISHI', 'RI'], ['NG', '']]`
-   第一个元素`'PAYP'`按顺序加入代表每行的list
-   第二个元素`'AL'`, 从倒数第二个list按倒序依次加入