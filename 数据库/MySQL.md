# 总结

| 存储引擎           | 索引   | 叶节点存储内容 |
| ------------------ | ------ | -------------- |
| InnoDB             | B+tree | 真实数据       |
| MyISAM             | B+tree | 数据地址       |
| MEMORY             | Hash   |                |
| BLACKHOLE          |        |                |
| PERFORMANCE_SCHEMA |        |                |
| MRG_MYISAM         |        |                |
| ARCHIVE            |        |                |
| FEDERATED          |        |                |



**InnoDB**

- 用2个文件存储：.frm存结构 .ibd存索引与数据

- **聚簇索引**：地址与数据合并存放（.ibd）

- 磁盘页：16K

- B+树的非叶节点存的就是每条记录的primary key。叶节点存储的直接就是键值对。

  如果没有主键，就是用唯一键。

  如果没有唯一键，就会自动生成一个6位row_id（对用户不可见）



**MyISAM**

- 用3个文件存储：.frm存结构 .MYI存地址 .MYD存数据
- **非聚簇索引**：地址与数据分开存放（.MYI and .MYD）

---



# 索引

数据库是存在**磁盘**上的，索引要考虑磁盘的读取效率。

如果我们考虑内存的索引，那速度等因素就不是问题，内存读取非常快。



各数据结构作为索引的对比：

- HashMap: 哈希碰撞，太占内存，等值查询很快但是范围查询很慢
- 二叉树/红黑树：因为是二叉，树的深度会太大，在向下traverse过程中会进行太多次IO，效率低
- B树：多叉树深度小，IO也快
- B+树：范围查询可以使用树底层链表



**回表**：如果有一个索引树是使用非主键的其他attribute，那么这个B+树的叶节点应该存对应的主键。使用这个attribute进行查询会先使用这个attribute的索引树找到记录的主键，然后使用主键与主键索引树找到记录。这个过程称为回表。举例：`SELECT * FROM user WHERE name = 'wei'`，这个查询是先用name索引树找到主键id，然后用id找到整行记录。

---



# MySQL commands

```mysql
-- connect to a server
mysql -u root -p


```

