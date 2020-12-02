# 存储引擎

**总结**

| 存储引擎           | 索引   | 事务 | 叶节点存储内容 | Comment                                                      |
| ------------------ | ------ | ---- | -------------- | ------------------------------------------------------------ |
| InnoDB             | B+tree | Yes  | 真实数据       | Supports transactions, row-level locking, and foreign keys   |
| MyISAM             | B+tree | No   | 数据地址       | MyISAM storage engine                                        |
| MEMORY             | Hash   | No   |                | Hash based, stored in memory, useful for temporary tables    |
| CSV                |        | No   |                | CSV storage engine                                           |
| BLACKHOLE          |        | No   |                | /dev/null storage engine (anything you write to it disappears) |
| PERFORMANCE_SCHEMA |        | No   |                | Performance Schema                                           |
| MRG_MYISAM         |        | No   |                | Collection of identical MyISAM tables                        |
| ARCHIVE            |        | No   |                | Archive storage engine                                       |
| FEDERATED          |        | No   |                | Federated MySQL storage engine                               |



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



各数据结构作为索引的对比：

- HashMap: 哈希碰撞；太占内存；等值查询很快但是范围查询很慢；
- AVL树/红黑树：因为是二叉，树的深度会太大；旋转次数太多，尤其是AVL树；在向下traverse过程中会进行太多次IO，效率低；
- B树：记录有序；多叉树深度小（一般就3-4层）；IO也快；
- B+树：所有B树的优点；范围查询可以使用树底层双向链表；



**回表**：如果有一个索引树是使用非主键的其他attribute，那么这个B+树的叶节点应该存对应的主键。使用这个attribute进行查询会先使用这个attribute的索引树找到记录的主键，然后使用主键与主键索引树找到记录。这个过程称为回表。举例：`SELECT * FROM user WHERE name = 'wei'`，这个查询是先用name索引树找到主键id，然后用id找到整行记录。

**组合索引**：遵循最左匹配原则，一个(name, age)的组合索引，要求query中一定要有name，`WHERE age = ?`是不行的。

**索引下推** (index condition pushdown)：查询组合索引时，存储引擎会判断query中的每一个attribute是否符合（不使用下推，只会判断第一个attribute），然后返回**完全匹配**的主键。尽量减少回表的次数。



**优化器**

- Cost-based optimizer
- Rule-based optimizer



**索引匹配方式**

- 全值匹配
- 匹配最左前缀
- 匹配列前缀
- 匹配范围值
- 精准匹配某一列，并范围匹配另一列
- 只访问索引的查询

---



# MySQL syntax

[mycli](https://github.com/dbcli/mycli): A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.

```mysql
-- install mycli 
pip install -U mycli

-- connect to server, only specify hostname when needed
mycli -h localhost -u root -p ...

-- create

```

---

