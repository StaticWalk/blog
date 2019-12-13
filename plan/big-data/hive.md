Hive是建立在hadoop上的数据仓库，提供了一系列工具用来查询和分析数据，   
提供的执行SQL的接口，用来操作存储在HDFS上的数据。  
使用sql提交MapReduce任务到hadoop集群   
 hive = 数据仓库 -> OLAP  
应用场景：  
高时延(需要通过MapReduce来执行用户提交的请求)   
大数据（构建在HDFS）   
离线数据（提交job和scheduler资源开销很大）    
hive体系结构
```
               JDBC + ODBC     
Client   UI    ThriftServer         /
                                    /  元数据
        驱动（Driver）              /  MateStore
编译器      优化器       执行器      / 
Compiler    Optimizer    Executor   /
                \/
                \/
             hadoop生态系统
           （hadoop Ecosystem）
```
元数据：通常存储在RDBMS（Mysql、Derby），包含表名、表列、分区、表的类型、数据存储路径等信息。    
驱动：Hive驱动在收到HiveSQL之后，创建会话来启动语句的执行，并监控执行的生命周期，把执行过程中产生的元数据进行存储。
编译器：对HiveSQL转化成AST，转化为可执行的计划。
优化器：拆分任务（mapreduce前的数据转化）
执行器：编译和优化之后，执行器将执行任务，对hadoop的作业（job）进行跟踪和交互，并调度需要运行的任务。
用户接口：用户通过JDBC、ODBC链接到Hive Server

Hive与传统RDBMS区别：
执行引擎：MapReduce - Executor
处理数据规模：海量 - 小
数据格式：用户定义 - 系统决定
可扩展性：高 - 低
数据存储：HDFS - 本地文件系统（Local FS）

HAProxy介绍：提供高可用性、负载均衡以及既有TCP和HTTP应用的代理软件

```angular2

  HAProxy   HAProxy     <--  Client | Client 
                       metaStorw
 Hive   Hive   Hive      --> Mysql
          |
          \/
        Hadoop
 DataNode   DataNode   DataNode 
 
```
HAProxy:代理客户端请求，负载均衡到hive上
Hive：提交任务到集群中
