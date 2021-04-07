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

