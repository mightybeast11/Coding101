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

- 磁盘页：16K

- B+树的非叶节点存的就是每条记录的primary key。叶节点存储的直接就是键值对。

  如果没有主键，就是用唯一键。

  如果没有唯一键，就会自动生成一个6位row_id（对用户不可见）



**MyISAM**

- 用3个文件存储：.frm存结构 .MYI存地址 .MYD存数据

---



# 索引

数据库是存在**磁盘**上的，索引要考虑磁盘的读取效率。



各数据结构作为索引的对比：

- HashMap: 哈希碰撞；太占内存；等值查询很快但是范围查询很慢；
- AVL树/红黑树：因为是二叉，树的深度会太大；旋转次数太多，尤其是AVL树；在向下traverse过程中会进行太多次IO，效率低；
- B树：记录有序；多叉树深度小（一般就3-4层）；IO也快；
- B+树：所有B树的优点；范围查询可以使用树底层双向链表；



**聚集索引**：叶结点是数据。一张表**有且只有一个**聚集索引。

**普通索引**：叶结点是主键。也叫二级索引，或辅助索引。

**回表**：先使用普通索引找到对应的主键。然后使用主键与聚集索引树找到数据。这个过程称为回表。举例：`SELECT * FROM user WHERE name = 'wei'`，这个查询是先用name索引树找到主键id，然后用id找到整行记录。

**组合索引**：遵循最左匹配原则，一个(name, age)的组合索引，要求query中一定要有name，`WHERE age = ?`是不行的。

**索引覆盖**：使用普通索引时，需要查询的结果正好（是普通索引用到的attribute+主键），那就无需回表。这个现象叫索引覆盖。

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



**索引失效**

- `LIKE %j%`：前面的百分号代表任意长度值，索引失去意义。
- 精准匹配某一列，并范围匹配另一列，匹配第三列时会失效。

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

