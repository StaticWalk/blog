Redis主从复制及演进
主库：读写操作  
从库：一般只读  slave-read-only
一主多从  链式主从复制
redis-cli -h ip -p 6380
> slaveof ip port
> config rewrite

复制过程：
1.复制初始化  从库向主库发起socket连接，身份认证建立连接
2.数据同步  主从开始数据同步，从库向主库psync命令，全量复制、增量复制
3.命令传播  心跳包确认链接，replconf ack offset 
    1从库汇报复制的偏移量，主节点对未同步的命令，2.判断主节点是否在线，实现最终数据一致性

复制演进： //    rdb持久化 + offset确认数据一致性 ，重连使用增量复制，增量优化
sync 第一次主从复制、短线重连都是全量复制
    主库收到从库的sync命令后，执行bgsave后台保存RDB快照，期间写命令假如缓冲队列。快照完成后发给slave，从库载入文件。
psync1 断线重连使用部分复制
info replication
    offset 复制偏移量：主从库分别维护这个字段，代表数据同步量，不同就代表数据不同步
    replcation backlog buffer ：复制积压缓冲区：FIFO定长，1M，备份最近主库发给从库的数据
    run_id redis实例id ：salve连接是获取主库id，用于断线重连
psync2 增量优化
    全量复制：
      从库提供的master_replid与master的replid不同，且不同于master的replid2，或同步速度快于master
      
        
配置redis集群
1.创建集群文件夹
2.添加6组实例，存放修改了端口、cluster-enabled的redis.conf      
3.找到src目录下的redis-trib.rb，复制到集群文件夹 
4.安装ruby脚本环境，并添加redis-version.gem到文件夹中
5.使用 ./redis-trib.rb create --replicates 1 ip:port1 ip:port2 ...
