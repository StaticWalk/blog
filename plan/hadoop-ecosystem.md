hbase[https://blog.csdn.net/nsrainbow/article/details/38758375]
分布式，面向列 开源数据库
用法：
面向列 每一条数据由行和列确定的 ky 
创建表的时候需要指定列名（至少一项）
列簇：多条数据组成检索逻辑的一行
检索关键词： 
startRow  limit条数 
TIMESTAMP 使用时间来精确定位数据
多版本，每个列簇允许两个版本数据
TTL过期