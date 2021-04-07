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



# 创建deque

创建新队列的参数必须是1个iterable。如果是一个node类型的instance，就会报错，只能先创建空deque：

```python
from collections import deque

d = deque()
d.append(root) # assume root is a Node class instance
```

