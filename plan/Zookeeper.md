分布式协调服务
集群间用于在自身间协调，并通过同步技术维护共享数据，

命名服务：按名称标识集群中的节点，类DNS
配置管理：加入节点的最近的和最新的系统配置信息
集群管理：实时得在集群和节点状态中加入/离开节点
选举算法：选举一个节点作为协调目的leader
锁定和同步服务：修改数据的同时锁定数据 --在连接其他分布式应用程序时进行自动故障恢复
 
1.Architecture架构
 Client 连接服务器重定向、心跳keepalive
 Server 
 Ensemble 服务器组，最少3个
 Leader 连接节点失败后执行自动恢复
 Follower 跟随leader指令的服务器节点
 
 2.层次命名空间 
 znode 
 版本号：当相关联的数据发生变化的时候，对应的版本号会增加
 操作控制列表：ACL访问znode的认证机制，管理znode的读取和写入操作
 时间戳：创建和修改znode所经历的时间
 数据长度：一个节点可以存1M的数据
 节点类型
 持久节点：创建客户端断开后仍然存在，默认
 临时节点：创建客户端
 顺序节点：/mya --> /mya0000000001  十位序列号
 
 3.Session 会话
 会话id、心跳
 会话中的请求按照FIFO执行，客户端链接到服务器，会向客户端分配会话id
 
 4.Watchs 监视
 客户端读取znode时设置watches，watches会向注册的客户端发送任何znode更改的通知

leader选举
* 所有节点创建相同路径 /app/leader_election/guid_序号、临时节点
* zk集合将十位序列号添加到路径
* 最小数字节点为leader，其余follower
* follower节点监视下一个最小数字的znode
* leader关闭，临时节点消失，下一个follower通过监视器获取leader移除的通知
* 下一个f检查是否存在更小数字node，无自己成leader，否则，转移leader
 