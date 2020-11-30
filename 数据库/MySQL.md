| 存储引擎           | 索引   |
| ------------------ | ------ |
| InnoDB             | B+tree |
| MyISAM             | B+tree |
| MEMORY             | Hash   |
| BLACKHOLE          |        |
| PERFORMANCE_SCHEMA |        |
| MRG_MYISAM         |        |
| ARCHIVE            |        |
| FEDERATED          |        |



# 数据库索引

数据库是存在**磁盘**上的，索引要考虑磁盘的读取效率。

如果我们考虑内存的索引，那速度等因素就不是问题，内存读取非常快。



各数据结构作为索引：

- HashMap: 哈希碰撞，太占内存，等值查询很快但是范围查询很慢
- 二叉树/红黑树：因为是二叉，树的深度会太大，在向下traverse过程中会进行太多次IO，效率低
- B树：多叉树深度小，IO也快
- B+树：范围查询可以使用树底层链表



# InnoDB

- 索引：B+树
- 用2个文件存储：.frm存结构 .ibd存索引与数据
- 磁盘页：16K



## MyISAM

- 索引：B+树
- 用3个文件存储：.frm存结构 .MYI存索引 .MYD存数据