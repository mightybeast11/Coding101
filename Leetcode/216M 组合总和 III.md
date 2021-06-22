# combination

Time: O()

Space: O()

```python
class Solution:
    def combinationSum3(self, k, n):
        subsets = list(map(list, combinations([i for i in range(1, 10)], k)))
        d = defaultdict(list)
        for subset in subsets:
            d[sum(subset)].append(subset)
        return d[n]
```



用`filter()`和`lambda`会更短, 也无需`defaultdict`

直接使用combination object, 而不是list的话, 空间消耗也小很多

```python
class Solution:
    def combinationSum3(self, k, n):
	    return list(filter(lambda l: sum(l)==n, combinations([i for i in range(1, 10)], k)))
```

