4月22日周总结 (3分)  
&emsp;&ensp;从11天前的Java引用到今天的学习内容做个总结，学习内容不是很多断了一次。  
&emsp;&ensp;RedBlackTree -> Enum -> TreeMap -> IdentityHashMap -> WeakHashMap         

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
    
