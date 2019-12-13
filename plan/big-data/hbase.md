[https://juejin.im/post/5c666cc4f265da2da53eb714]
Hbase NoSQL分布式存储的数据库，不支持传统的rdbms的sql查询语言
特点：
* 强读写一致，适合高速的计算聚合
* 自动分片，通过region分散在集群中，行数增长后region自适应切分和再分配
* 自动的故障转移
* 集成Hadoop/HDFS,开箱即用，不用太麻烦的衔接
* 块缓存，布隆过滤器，高效的列查询优化

hbase使用场景
* 数据库量要足够多，十亿以及百亿行数据。几百万行的数据量推荐rdbms
* hdfs集群节点五个起，否则影响性能

```

zookeeper----------------
  -                       RegionServer -----------    
  -                       RegionServer ----------- HDFS
  -                       RegionServer -----------
Master---------------------

```
Zookeeper 分布式协调，RegionServer注册自己信息到zk中   
HDFS是Hbase运行的底层文件系统   
RegionServer数据节点，存储数据   
Master RegionServer要实时向Master报告信息。   
Master监听全局region的运行情况，控制rs的故障转移和切分   
    
     
建表指定表名称和列簇名：   
create 'test','cf'      
添加数据：        
put 'test','row1','cf:a','value1'         
查询数据：      
scan 'test' //全局扫描       
get 'test,'row1' //根据行关键词找数据    
删除：   
//1.先禁止HBase业务表 2. 再执行删除操作   
disable 'test'   
drop 'test'   
   
```angular2
create 'user','info','ship';

put 'user', '524382618264914241', 'info:name', 'zhangsan'
put 'user', '524382618264914241', 'info:age',30
put 'user', '524382618264914241', 'info:height',168
put 'user', '524382618264914241', 'info:weight',168
put 'user', '524382618264914241', 'info:phone','13212321424'
put 'user', '524382618264914241', 'ship:addr','beijing'
put 'user', '524382618264914241', 'ship:email','sina@sina.com'
put 'user', '524382618264914241', 'ship:salary',3000

put 'user', '224382618261914241', 'info:name', 'lisi'
put 'user', '224382618261914241', 'info:age',24
put 'user', '224382618261914241', 'info:height',158
put 'user', '224382618261914241', 'info:weight',128
put 'user', '224382618261914241', 'info:phone','13213921424'
put 'user', '224382618261914241', 'ship:addr','chengdu'
put 'user', '224382618261914241', 'ship:email','qq@sina.com'
put 'user', '224382618261914241', 'ship:salary',5000

```
