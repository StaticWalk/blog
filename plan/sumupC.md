4月22日周总结 (3分)  
&emsp;&ensp;从11天前的Java引用到今天的学习内容做个总结，学习内容不是很多断了一次。  
&emsp;&ensp;RedBlackTree -> Enum -> TreeMap -> IdentityHashMap -> WeakHashMap -> Volatile + JMM -> Synchronized -> Lock -> 并发集合 -> HashMap死循环 -> 并发队列 -> Asyn  

&emsp;&ensp;RedBlackTree
 * 红黑树是为了能保证O(logN)平衡二叉树(AVLTree)的实现，树中每个节点左边后代数目大致等于右边后代数目
 * 二叉树在插入有序数据后会退化成链表，原快速、插入和删除数据能力丧失。
 * 基于二叉树的增加和删除后，各有一步修树恢复平衡性的操作。
 * 基本操作：添加，删除和旋转。平衡性修正：变色 > 左旋 > 右旋   
     
&emsp;&ensp;Enum
 * 枚举类型会和类类型一样被单独定义成一个单独的class文件
 * JVM"解释执行"只能支持class文件，需要将代码编译成"字节码".class文件
 * IDEA中没有看到单独的class文件，可能是1.8之后改进了
 * class文件中enum会被剖离成static enum包含枚举类型
 * 自带compareTo()返回序列号差值self.ordinal - other.ordinal  
    
&emsp;&ensp;EnumMap   
 * 是一个专门和枚举类型结合形成Map的key-value键值对结构，内存实现是数组结构的Map实现。
 * key不能null，value可以null（实际maskNull后,以Null存在数据库中）
 * 线程安全包装 Map<EnumKey, V> m = Collections.synchronizedMap(new EnumMap<EnumKey, V>());   
   
&emsp;&ensp;TreeMap   
 * fast-fail快速失败机制(iterator方法返回的迭代器是fast-fail)  
 1.Java集合的一种错误检测机制，用于检测程序错误。     
 2.多线程情况对集合进行结构上的更改操作(modCount改变导致modCount!=expectedModCount)   
 * TreeMap使用两个比较器，首选应定义几天Comparator(“动态绑定”，更灵活),否则默认Comparable(和具体类绑定的，“静态绑定”)
 * 插入和删除顺序是通过比较器对key的比较决定的，不需要key覆写hashCode方法和equals方法除重
 * TreeMap的查询、插入、删除效率均没有HashMap高，一般只有要对key排序(比较器的用处)时才使用TreeMap
 * TreeMap的key不能为null，而HashMap的key可以为null   
 ! ! TreeSet和HashSet二者分别是基于TreeMap和HashMap实现，只是对应的节点中只有key，没有value
     
&emsp;&ensp;IdentityHashMap   
 * 只有全等key才相等，出现key-value冲突时，不是利用(链地址法)链表解决是(再哈希法)继续计算下一个索引,nextKeyIndex()往后找(i+2<len?i+2:0)  前面的空内存？？
 * 2整数次幂容量Object[],偶数存key，奇数存value，index=((h<<1)-(h<<8))&(len-1)哈希方法出来的都是偶数
 * capacity扩容操作中两处判断2/3Min<(最大二次幂)<Max/3，二进制最高位其余位全部补0.方法是按位取或
 * 依然引入modCount来记录线程安全情况
 * equals() 1.o属于IdentityHashMap,containsMapping逐一比较 2.o属于Map,entrySet().equals(m.entrySet())返回true就可以 3.o==this   
      
&emsp;&ensp;WeakHashMap   
 * 弱引用队列关联map数组中存储的数据，类似hashmap使用链表解决hash冲突,该类可实现缓存，内存紧张时可避免占用大量内存，销毁不用过时对象
 * 必须和引用队列使用，Entry对象和ReferenceQueue关联，Entry是弱引用对象  Entry中的hash方式是通过键值hash或 Objects.hashCode(k)^Objects.hashCode(v)
 * expungeStaleEntries()：遍历引用队列中保存的已回收弱引用对象：map数组清除原有引用，只保留还未回收的弱引用对象；queue.poll()弹出弱引用对象。   
 * 两层循环，1循环遍历引用队列的值，2遍历map数组，map一旦发现相同引用删除，更新map数组长度
    
&emsp;&ensp;Volatile&emsp;&ensp;https://github.com/StaticWalk/jdk8/blob/master/src/ect/TestVolatile.java
 * 并发编程三个概念(并发程序要想正确地执行，必须要保证原子性(银行转账问题)、可见性(t1:i++;t2:j=i)以及有序性(指令重排序))!!!
 * JMM(Java Memory Model)规定：程序中的变量是在内存中的，当线程需要使用该变量时，要把该变量复制所在CPU的工作内存(高速缓存)中，CPU通过高速缓存拿到变量，修改后还给高速缓存。程序执行完毕后，内存再同步高速缓存中的值。   
 * JMM中，当一个变量在多个CPU中都存在缓存（一般在多线程编程时出现），可能存在缓存不一致的问题。解决方法：   
 1.通过在总线加LOCK#锁的方式:CPU和其他部件通信通过总线进行的，在总线加LOCK锁能阻塞其他CPU对其他部件的访问(内存)，使得只能有一个CPU使用这个变量的内存。  ???相当于多CPU单线程，效率低下   
 2.缓存一致性协议：Intel的MESI协议，保证了每个缓存中使用的共享变量是一致的，核心思想：当CPU写数据时，如果操作变量是共享变量(其他CPU也存在该变量副本)，会发出信号通知其他CPU将该变量的缓存行置无效状态，当其他CPU读取这个变量时，发现自己缓存中改缓存行是无效的，便再次从内存中读取。  
 * JMM:JVM规范中试图定义一张Java内存模型来屏蔽各硬件平台和操作系统的内存访问差异，达到让Java程序的跨平台内存访问效果的一致性。为了更好的执行性能，JMM没有限制执行引擎对CPU的寄存器和高速缓存的使用，也没有限制编译器对指令的重排序。   
 1.原子性：Java内存模型只保证了基本读取和赋值是原子性操作，如果要实现更大范围操作的原子性，可以通过synchronized和Lock来实现   
 2.可见性：一个共享变量被volatile修饰时，它会保证修改的值会立即被更新到主存，当有其他线程需要读取时，它会去内存中读取新值。通过synchronized和Lock也能够保证可见性，synchronized和Lock能保证同一时刻只有一个线程获取锁然后执行同步代码，并且在释放锁之前会将对变量的修改刷新到主存中。   
 3.有序性：指令重排序不会影响单线程程序进行，会影响多线程并发执行的正确性，通过volatile关键字来保证一定的“有序性”（具体原理在下一节讲述）。另外可以通过synchronized和Lock来保证有序性，synchronized和Lock保证每个时刻是有一个线程执行同步代码，相当于是让线程顺序执行同步代码。  
    
&emsp;&ensp;Synchronized(对并发的理解采取的是 看书 + demo + 博客)    
 * 线程的基本概念(线程表示一条单独的执行流，它有自己的程序执行计数器，有自己的栈)   
 1.线程创建(extends Thread、implements Runnable)之后，操作系统会为它非配资源。(进程拥有资源，线程共享资源)   
 2.基本属性和方法(id和name、优先级、状态、daemon线程(整个程序只有daemon 程序退出)、sleep()、yield()、join())

 
 