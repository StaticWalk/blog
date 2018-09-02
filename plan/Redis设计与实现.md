## 《Redis设计与实现》总结
  
### 目录

* [数据结构与对象](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#数据结构与对象)
    * [简单动态字符串](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#简单动态字符串)
        * [SDS定义](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#SDS定义)
        * [SDS和C字符串的区别](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#SDS和C字符串的区别)
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#SDS和C字符串的区别)
    * [链表](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#链表)
        * [链表与链表节点的实现](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#链表与链表节点的实现)
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#链表与链表节点的实现)
    * [字典](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#字典)
        * [字典的实现](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#字典的实现)
        * [哈希算法](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#哈希算法)
        * [哈希冲突](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#哈希冲突)
        * [rehash/渐进式rehash](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#rehash/渐进式rehash)
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#哈希冲突)
    * [跳跃表](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#跳跃表)
        * [跳跃表的实现](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#跳跃表的实现)
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#跳跃表的实现)
    * [整数集合](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#整数集合)
        * [整数集合的实现](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#整数集合的实现)
        * [升级](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#升级)
        * [降级](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#降级)
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#降级)
    * [压缩列表](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#压缩列表)
        * [压缩列表的构成](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#压缩列表的构成)
        * [压缩列表节点的构成](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#压缩列表节点的构成)
        * [连锁更新](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#连锁更新)
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#连锁更新)
    * [对象](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#对象)
        * [对象的类型与编码](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#对象的类型与编码)
        * [字符串对象](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#字符串对象)
        * [列表对象](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#列表对象)
        * [哈希对象](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#哈希对象)
        * [集合对象](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#集合对象)
        * [有序集合对象](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#有序集合对象)
        * [类型检查与命令多态](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#类型检查与命令多态)
        * [内存回收](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#内存回收)
        * [对象共享](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#对象共享)
        * [对象空转时长](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#对象空转时长)
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#对象空转时长) 
* [单机数据库](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#单机数据库)    
    * [数据库](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#数据库)    
        * [服务器中的数据库](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#服务器中的数据库)    
        * [键过期](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#键过期)    
        * [删除策略](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#删除策略)          
    * [RDB持久化](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#RDB持久化)    
        * [RDB文件的创建与载入](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#RDB文件的创建与载入)    
        * [RDB文件结构](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#RDB文件结构)    
        * [分析RDB文件](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#分析RDB文件)    
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#分析RDB文件)    
    * [AOF持久化](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#AOF持久化)    
        * [AOF持久化的实现](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#AOF持久化的实现)    
        * [AOF文件的载入与数据还原](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#AOF文件的载入与数据还原)    
        * [AOF重写](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#AOF重写)    
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#AOF重写)    
    * [事件](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#事件)    
        * [文件事件](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#文件事件)    
        * [时间事件](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#时间事件)    
        * [事件的调度和执行](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#事件的调度和执行)    
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#事件的调度和执行)    
    * [客户端](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#客户端)    
        * [客户端属性](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#客户端属性)    
        * [客户端的创建和关闭](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#客户端的创建和关闭)    
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#客户端的创建和关闭)    
    * [服务器](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#服务器)    
        * [命令请求过程](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#命令请求过程)    
        * [serverCron函数](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#serverCron函数)    
        * [初始化服务器](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#初始化服务器)    
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#初始化服务器)    
* [多级数据库的实现](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#多级数据库的实现)   
    * [复制](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#复制)    
        * [旧版复制功能](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#旧版复制功能)    
        * [新版复制功能](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#新版复制功能)    
        * [部分重同步的实现](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#部分重同步的实现)    
        * [PSYNC命令和复制](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#PSYNC命令和复制)    
        * [心跳检查](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#心跳检查)    
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#心跳检查)    
    * [Sentinel](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#Sentinel)    
        * [启动并初始化Sentinel](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#启动并初始化Sentinel)    
        * [获取主从服务器信息](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#获取主从服务器信息)    
        * [向主从服务器发送信息](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#向主从服务器发送信息)    
        * [接收主从服务器的频道信息](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#接收主从服务器的频道信息)    
        * [检测主观下线状态](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#检测主观下线状态)    
        * [检查客观下线状态](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#检查客观下线状态)    
        * [选举领头Sentinel](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#选举领头Sentinel)    
        * [故障转移](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#故障转移)    
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#故障转移)    
    * [集群](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#集群)    
        * [节点和槽指派](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#节点和槽指派)    
        * [集群执行命令](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#集群执行命令)    
        * [重新分片](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#重新分片)    
        * [ASK错误](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#ASK错误)    
        * [复制与故障转移](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#复制与故障转移)    
        * [要点总结](https://github.com/StaticWalk/blog/blob/master/plan/Redis设计与实现.md#复制与故障转移)    
  

## 数据结构与对象
### 简单动态字符串
#### SDS定义
Redis基于C语言，但没有使用C语言传统字符串('\0'为结尾)，使用简单动态字符串(simple dynamic string)为默认字符串表示。   
除了保存数据库中字符串值外，还被用做缓冲区：AOF持久化中的缓冲区和客户端状态的输入缓冲区。
```angularjs
struct sdshdr{
    
    //记录buf数组中已经使用的数量
    //SDS字符串保存的字符串的长度
    int len;
    
    //记录buf数组中未使用的数量
    int free;
    
    //字节数组，保存字符串
    char buf[];
    
}
```
    
#### SDS和C字符串的区别   

* len属性，常数复杂度获取字符串长度
* SDS记录自身长度，空间分配策略能杜绝缓冲区溢出
* 修改字符串长度N次最多需要执行N次内存重分配
    * 空间预分配：afterModLen > 1M ? afterModLen+1M+1byte : 2*afterModLen+1byte
    * 惰性空间释放：不会主动回收用free记录SDS缩短后多余的空字节，需要手动回收
* 二进制安全(可以保存文本或者二进制数据)，SDS使用len属性的值而非操控字符串来判断结束

#### 要点总结   
SDS更灵活，优点除开后面的aof和client的缓冲区，对比C语言字符串见上

### 链表

#### 链表与链表节点的实现
```angularjs

typedef struct listNode{
    
    //前置节点
    struct listNode *prev;
    
    //后置节点
    struct listNode *next;
    
    //节点的值
    void *value;
    
}listNode;

typedef struct list{
    
    //表头节点
    listNode *head;
    
    //表尾节点
    listNode *tail;
    
    //链表所包含的节点数量
    unsigned long len;
    
    //节点值复制函数
    void *(*dup) (void *ptr)
    
    //节点值释放函数
    void *(*free) (void *ptr)
    
    //节点值对比函数
    void *(*match) (void *ptr,void *key)

}list;
  
```   

&emsp;&emsp;双端：链表带有头尾指针，获取某个节点的前后节点复杂度O(1)   
&emsp;&emsp;无环：表头节点*prev和表尾节点*next指向NULL，链表访问时NULL为终点   
&emsp;&emsp;带表头和表尾指针   
&emsp;&emsp;带链表长度计数器 list.len   
&emsp;&emsp;多态：value * 保存值，可以指定数据类型   

#### 要点总结    
链表的使用范围在列表键、发布与订阅、慢查询、监视器。

### 字典

#### 字典的实现

```angularjs

字典的实现hashtable
typedef struct dictht{
    
    //哈希表数组
    dictEntry **table;
    
    //哈希表大小
    unsigned long size;
    
    //哈希表大小掩码=size-1，用于计算索引值
    unsigned long sizemark;
    
    //该哈希表已有节点数
    unsigned long used;
    
}dictht;

字典节点
typedef struct dictEntry{
    
    //键
    void *key;
   
    //值
    void *union{
        void *val;
        uint64_tu64;
        ini64_ts64;
    }v;
    
    //指向下一个哈希节点，形成链表来解决hash冲突
    struct dictEntry *next;
    
}dictEntry;

字典
typedef struct dict{
    
    //类型特定函数
    dictType *type;
    
    //私有数据
    void *privdata;
    
    //哈希表
    dictht ht[3];
    
    //rehash索引
    //当rehash不进行时，值为-1
    int rehashidx;
    
}

```

#### 哈希算法    
index = hash&dict->ht[0].sizemask    
     
#### 哈希冲突   
链地址法，就是常说的链表数组(hashmap采用了这个方式并采取了红黑树优化)     
再哈希法，将得到的index再次计算得到新值

#### rehash/渐进式rehash    
当哈希表保存的键值对增多，为了控制loadFactory，程序需要对哈希表大小进行调整    
对哈希表ht\[0]进行rehash步骤：
    * 1)新建一个哈希表并分配空间，大小取决于ht\[0].used
        * 扩展操作：ht[1].size是大于ht\[0].used*2的最小二次幂
        * 收缩操作：ht[1].size是大于ht\[0].used的最小二次幂
    * 2)将保存在ht\[0]中的所有键值对重新计算索引rehash到ht\[1]上
    * 3)在所有ht\[0]键值对迁移到ht\[1]后，释放ht\[0]，将ht\[1]设置为ht\[0]  
      
&emsp;&emsp;渐进式rehash让字典同时持有ht\[0]和ht\[]，通过rehashidx来记录rehash的进行，rehash完成之后置-1
#### 要点总结   
&emsp;&emsp;在渐进式rehash中的CRUD进行在两个哈希表上面的，执行期间新加的数据会被直接加到ht\[1]中。

### 跳跃表
#### 跳跃表的实现
```angularjs

typedef struct zskiplistNode{
    
    //层()
    struct zskiplistLevel{
        
        //前进指针,指向表尾用于从表头节点向表尾节点方向访问节点
        struct zskiplistNode *forward;
        
        //跨度(如果指向NULL，跨度为0)
        unsigned int span;
    }level[];//数组大小(1-32)随机生成
    
    //后退指针
    struct zskiplistNode *backforwd;
    
    //分值
    double score;
    
    //成员对象
    robj *obj;
 
}zskiplistNode;

typedef struct zskiplist{
    
    //表头节点和表尾节点
    struct zskiplistNode *header, *tail;
    
    //表中节点的数量
    unsigned long length;
    
    //表中层数最大的节点的层数
    int level;
}

```
 ![icon](https://github.com/StaticWalk/blog/blob/master/images/redis01.jpg?raw=true)

#### 要点总结  

* 跳跃表是有序集合的底层实现之一
* Redis跳跃表实现由zskiplist和zskiplistNode两个结构组成
* 同一跳跃表多个节点可以包含相同分值，但节点成员对象必须唯一
* 节点排序按照先分值再成员对象大小

### 整数集合
#### 整数集合的实现
```angularjs

整数集合
typedef struct intset{
    
    //编码方式属性值：INTSET_ENC_INT16、INTSET_ENC_INT32、INTSET_ENC_INT64 
    uint32_t encoding;
    
    //集合包含的元素数量
    uint32_t length;
    
    //保存元素的数组
    int8_t contents[];
    
}intset;

```

#### 升级
当encoding类型为16位，length=3的整数集合要加入一个32位的整数时，此时整数集合就需要升级：
* 1)根据新的类型长度和新的集合元素数量，对底层数组进行空间重分配。
* 2)在扩充后的内存中，先添加需要加入的整数到96-127位
* 3)32-47位到64-95位、16-31位到32-63位、0-15位搭配0-31位
* 4)最后讲encoding属性改为INTSET_ENC_INT32

#### 降级
* 不支持
    
#### 要点总结
&emsp;&emsp;升级的好处是提升了整数集合的灵活性，另一个是尽可能得节约了空间


### 压缩列表
* 压缩列表的构成
* 压缩列表节点的构成
* 连锁更新
#### 要点总结

###对象
* 对象的类型与编码
* 字符串对象
* 列表对象
* 哈希对象
* 集合对象
* 有序集合对象
* 类型检查与命令多态
* 内存回收
* 对象共享
* 对象空转时长
#### 要点总结



## 单机数据库


### 数据库
#### 服务器中的数据库
```angularjs

struct redisServer{
    
    //数组保存服务器中所有数据库，通过select dbnum来切换目标数据库
    redisDB *db;
    
    //数据库数目
    int dbnum;
}

struct redisClient
    
    //慎用多数据库，除了-cli客户端都不会返回目标数据库号码
    //通过select num来切换使用的数据库
    redisDB *db;
    
}redisClient;


typedef struct redisDB{
    
    //数据库键空间，保存所有数据库中键值对
    dict *dict;//会看上面的dict是啥
    
    //过期字典保存键的过期时间
    dict *expires;
    
    //两个字典指向相同的键对象，不会出现浪费空间的重复对象
}redisDB:

```

#### 键过期
```angularjs

EXPIRE/PEXPIRE key  5     ---设置键过期ms/s

TIME             ---拿到当前系统UNIX时间戳

EXPIREAT/PEXPIREAT key 13565648     ---到指定时间删除键ms/s

PERSIST key      ---取消一个键的过期时间

TTL key   ---按秒返回键的剩余生存时间

PTTL key     ---按毫秒返回键的剩余生存时间

`````
#### 删除策略
* 定时删除：使用定时器定时删除，CPU时间不友好；redis自身不是很好支持时间事件   
* 惰性删除：取出键的时候才进行过期检验，内存不友好   
* 定期删除：定时删除 + 惰性删除，要控制好频率和时长  

### RDB持久化
#### RDB文件的创建与载入   
Redis是内存数据库，在服务器进程退出之后，需要对服务器中的数据库状态进行持久化。    
RDB文件是压缩过的二进制文件，Redis也可以通过这个文件还原数据库状态。
AOF文件更新频率高于RDB文件，服务器在两种持久化方式都开启时会优先工作前者。
```angularjs

生成RDB文件的两个方法

def SAVE():{
    
     #创建RDB文件
     rdbSave()
     
}


def BGSAVE():{

    #创建子进程
    pid = fork()
    
    if pid == 0:
    
        #子进程创建RDB文件
        rdbSave()
        #完成后发送信号给父进程
        singal_parent()
        
    else if  pid > 0:
        #夫进程继续处理命令，并轮询等待子进程的信号
        handle_request_and_wait_singnal()
        
    else:        
        #处理错误
        handle_fork_erroe()

}

#自动间隔性保存
save 900 1   ---设置BGSAVE的频率，900秒内save1次

```
   
#### RDB文件结构
```angularjs

#1固定大写开头字符串 2版本号 3按照数据库分别存放 4结束符号 5校验和
REDIS | db_version | databases |  EOF  | check_sum
      |   4byte    | db0 | db3 | 1byte |  8byte
      
databases部分：
1固定字符串 2数据库号 3键值对(8种类型)
SELECTDB | db_number | key_value_paris  
         |           | TYPE|key|value  /   EXPIRETIME_MS|ms|TYPE|key|value 

对value编码的细节自己去看书吧，太难COPY了！
```
#### 分析RDB文件
```angularjs


127.0.0.1:6379> flushall
OK
127.0.0.1:6379> setex msg 10086 "hello"
OK
127.0.0.1:6379> save
OK

#退出-cli在bin目录下查看rdb文件
[root@VM_77_51_centos bin]# od -c dump.rdb
0000000   R   E   D   I   S   0   0   0   8 372  \t   r   e   d   i   s
0000020   -   v   e   r 005   4   .   0   .   2 372  \n   r   e   d   i
0000040   s   -   b   i   t   s 300   @ 372 005   c   t   i   m   e 302
0000060   *   [   ?   [ 372  \b   u   s   e   d   -   m   e   m 302   (
0000100 256  \v  \0 372 016   r   e   p   l   -   s   t   r   e   a   m
0000120   -   d   b 300 377 372  \a   r   e   p   l   -   i   d   (   f
0000140   1   5   9   1   9   1   7   3   0   b   8   b   3   e   f   b
0000160   f   a   b   c   5   7   4   d   2   4   a   4   4   a   4   7
0000200   c   8   6   c   f   3   2 372  \v   r   e   p   l   -   o   f
0000220   f   s   e   t 300  \0 372  \f   a   o   f   -   p   r   e   a
0000240   m   b   l   e 300  \0 377   E   \ 231   ,   c 244   B 275
0000257

这是我的数据库没有开启RDB持久化

```


#### 要点总结
### AOF持久化
#### AOF持久化的实现
#### AOF文件的载入与数据还原
#### AOF重写
#### 要点总结

### 事件
#### 文件事件
#### 时间事件
#### 事件的调度和执行
#### 要点总结

### 客户端
#### 客户端属性
#### 客户端的创建和关闭
#### 要点总结

### 服务器
#### 命令请求过程
```angularjs

struct redisServer{
    
    //AOF缓冲区
    sds aof_buf;
    
}

AOF重写伪代码：

def aof_rewrite(new_aof_file_name):{
    
    
    f = create_file(new_aof_file_name)
    
    for db in redisServer.db
        
        if db.is_empty():continue
        
        f.write_commmand("SELECT0"+db.id)
        
            for key in db:
            
                if key.is_expired() : continue
                
                if key.type == String:
                    rewrite_string(key) 
                elif key.type == List:
                    rewrite_list(key) 
                elif key.type == Hash:
                    rewrite_hash(key)                        
                elif key.type == Set:
                    rewrite_set(key)     
                elif key.type == SortedSet:
                    rewrite_sorted_set(key)       
    
}



```

#### serverCron函数
#### 初始化服务器
#### 要点总结


##多级数据库的实现
### 复制
#### 旧版复制功能
#### 新版复制功能
#### 部分重同步的实现
#### PSYNC命令和复制
#### 心跳检查
#### 要点总结   
* Redis2.8以前的复制功能不能搞笑处理短线重复制问题，版本后引入了重同步功能可以解决这个问题
* 部分重同步通过复制偏移量、复制挤压缓存区、服务器运行ID三部分实现
* 复制操作刚开始时，从服务器会成为主服务器的客户端，向主服务器请求执行复制操作，复制后期，主从服务器互成对方的客户端
* 主想从传播命令来更新从服务器的状态，从要向主发送命令进行心跳检测和命令丢失检测


### Sentinel
#### 启动并初始化Sentinel
#### 获取主从服务器信息
#### 向主从服务器发送信息
#### 接收主从服务器的频道信息
#### 检测主观下线状态
#### 检查客观下线状态
#### 选举领头Sentinel
#### 故障转移
#### 要点总结    
* Sentinel是运行在特殊模式下的Redis服务器,使用与普通模式下不同的命令。
* Sentinel读取用户指定的配置文件，为每个被监视的主服务器创建相应实例结构，创建与主服务器的连接
    * 命令连接：用于向主服务器发送命令请求
    * 订阅连接：用于接收指定频道的消息
* Sentinel通过向主服务器发送INFO来获取从属服务器的地址信息，并为他们创建实例结构，并创建命令、订阅连接
* 通常，Sentinel向被监视的主从服务器 次/10s发送INFO命令，当主服务器下线或Sentinel对主服务器故障转移时，Sentinel对从服务器的INFO确认 次/1s
* 对监视同一主从服务器的多个Sentinel来说，次/2s向被监视服务器的_sentinel_:hello频道发送信息来告知其他Sentinel自己的存在
* Sentinel之间通过被监视服务器的_sentinel_:hello频道发送信息和命令连接
* Sentinel与主从服务器之间有命令连接和订阅连接，Sentinel之间只有命令连接
* Sentinel每秒一次向实例(主从服务器+其他Sentinel)发送PING，检测实例是否在线，实例在指定时长内没回复会被主观下线
* Sentinel将一个主服务器主管下线后会向其他Sentinel询问，如果票数足够，就会将该服务器客观下线并进行故障转移

### 集群
#### 节点和槽指派
#### 集群执行命令
#### 重新分片
#### ASK错误
#### 复制与故障转移
#### 要点总结    
* 集群搭建直接看博客吧 https://www.cnblogs.com/leechenxiang/p/5441126.html