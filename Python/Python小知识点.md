# 字典遍历

`enumerate(x)`的作用是在遍历过程中输出index，跟key没有任何关系。

```python
# 打印key and value
for k, v in dic.items():
    print(k, v)
    
# 打印index, key and value
for i, k, v in enumerate(dic.items()):
    print(i, k, v)
```

---

# 创建deque

创建新队列的参数必须是1个iterable。如果是一个node类型的instance，就会报错，只能先创建空deque：

```python
from collections import deque

d = deque()
d.append(root) # assume root is a Node class instance
```

---

# Walrus operator

Python 3.8 推出的新operator, 目的是在large expression中赋值的时候, 保留这个变量, 以便后面继续使用.

我自己记作: **保留赋值符**

```python
def walrus():
    s = 'wzh'
    if (n := len(s)) > 0:
        print(f'Test walrus operator: {n}')

    while x := [1,2,3]:
        print(x)
        break
```

---

# list中重复元素的所有index

```python
l = ['a', 'b', 'a']
indices = [i for i,v in enumerate(l) if v == "a"]
```

---

# 生成全部子集



**forloop方法**

(个人不推荐, 下面的方法更neat)

```python
List = [1, 2, 3, 4]
subsets = [[]]
for i in range(len(List)):     	# 定长，如果也会变长，loop无法结束
    for j in range(len(subsets)):  # 变长，这是个range，所以可以loop，是原list就不行
        subsets.append(subsets[j] + [List[i]])
```



**`itertools.combinations`方法**

为什么这里的syntax是`sum(list_of_list, [])`?

-   `sum()`函数的第一个参数是需要求和的object, 但是其实有第二个参数, default为0
-   list与0相加, 显而易见会报错. 所以我们就需要一个空list作为第二个参数

`combinations()`函数的举例: 求(0,1,2,3)所有长度为3的子集 (输出是一个itertools.combinations object, 需要转换)

```python
combinations(range(4), 3)
```

>   (0,1,2), (0,1,3), (0,2,3), (1,2,3)

所以生成所有子集的写法如下: 把itertools.combinations object内部的元素用`map(list, combinations())`拆出来

```python
from itertools import combinations
List = [1, 2, 3]
subsets = sum([list(map(list, combinations(List, i))) for i in range(len(List) + 1)], []) 
```

>   [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]

---

# 用重复元素创建新集合

-   重复元素是`int`等时可以用: `[1] * 3`
-   重复元素是空list时不能用`[[]] * 3`, 修改其中一个元素, 其他所有元素也都会变, 所有元素其实是同一个list. 所以必须用: `[[] for _ in range(3)]`

---
