# HashMap

- HashMap的key和value都可以是null，但是因为key的唯一性，当然就只有一个key可以是null。Hashtable的key和value都不能是null。
- 线程不安全
  - `put()`方法可能会导致扩容，扩容的操作因为要重新设计`hash()`方法，必须构建新的map进行数据迁移，如果这时又有人call `put()`添加数据，那么迁移无法结束，扩容操作可能会进入死循环。
  - 使用keyword `synchronized`可以解决这个问题，但是会给整个map的`put()`方法上锁，太慢了。HashTable就是使用的这个方法保证线程安全，不要用。
  - ConcurrentHashMap使用分段锁来锁住一小部分map，这样来保证高效和线程安全。
- HashMap其实就是个数组，存储大量的数据需要消耗过大空间，搞不定。大数据要使用BitMap和Bloom Filter。

## Java7

- 总结：==数组+链表==
- 结构：外层结构是array，array的每一个元素是单链表，使用`h = hash(key)`方法确定将value加入`array[h]`位置的链表
- 用array的原因：使用hash值**快速定位**
- 用链表的原因：发生hash冲突时**快速插入**新值

## Java8

- 总结：==数组+链表+红黑树==

- 结构：外层结构是array，array的每一个元素是单链表或红黑树，使用`h = hash(key)`方法确定将value加入`array[h]`位置的链表

- 用array的原因：使用hash值快速定位

- 用链表的原因：发生hash冲突时快速插入新值

- 用红黑树的原因：当链表长度>8时替代链表来**提升查询速度**到O(logn)
  
  链表长度<8时仍然使用链表是因为构造树也需要资源



# 运算符

- [Java运算符](https://baijiahao.baidu.com/s?id=1659125201403697638&wfr=spider&for=pc)
- [原码、反码、补码 详解](https://zhuanlan.zhihu.com/p/91967268)

