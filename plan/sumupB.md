4月1日周总结&emsp;&ensp;(4分 )  
&emsp;&ensp;状态混乱，flag倒  
&emsp;&ensp;LinkedList -> Lambda -> BinartTree -> RedBlackTree  
&emsp;&ensp;LinkedList  
 * ArrayList 数组 优点是集合快速随机访问，缺点是根据位置索引操作元素速度慢，位置越小越慢
 * LinkedList 链表 元素操作高效，随机访问的时候效率低于ArrayList
 * LinkedList是基于双向链表，用做栈、队列、双端队列，非线程安全用于单线程，线程安全调用List list=Collections.synchronizedList(new LinkedList(...));  
 * （笔记不见了？？？）  
&emsp;&ensp;Comparator 比较选择器,
 * <T\> List<List<T\>> divder(Collection<T\> datas,Comparator<? super T> c)
 * List<List<Apple\>> byColors = divider(list, Comparator.comparing(o -> o.color));
 * 调用自定义的comparator方法要重写匿名内部类方法，延伸了jdk8新特性Lambda表达式  
&emsp;&ensp;java8新特性（Lambda,流API）
 * Lambda产生目的就是取代匿名内部类，( ) - >,是代码简单、可读、减少代码量  
 * Lambda内部变量命名越短越好，java8增加了java.util.function来支持java的函数式编程。Predicate能向API添加逻辑。  
 public static void filter(List<String> names,Predicate<String> condition){   
 &emsp;&ensp;names.stream().filter((name)->(condition.test(name))).forEach((name)->{   
 &emsp;&ensp;System.out.println(name+" ");   
 &emsp;&ensp;});}  
 lambda表达式和匿名内部类分析：
  * this关键字的指向：匿名类中的指向匿名类；lambda表达式中指向为包围该表达式的类。
  * java编译器将lambda表达式编译成类的私有方法,通过invokeDynamic字节码绑定.  
 &emsp;&ensp;Map 
  * Map是个接口存储<K,V>键值对，抽象出AbstractMap(实现了大部分Map中的API)便于其他类继承
  * NavigableMap接口继承SortedMap,有序，新增导航方法:"获取>=某个对象的键值对"
  * Map中的方法，Set<K> KeySet()保存key的set，Collection<V> values()保存value的Collection。Map.Entry是Map内部的一个接口，是一个键值对，通过Map.entrySet()来获取装Map.Entry的集合
  * AbstractMap继承Map，没有实现entrySet()方法仍是abstract修饰，继承AbstractMap需要实现entrySet()方法，key可null，key同会被后面的覆盖，迭代器遍历Iterator<Map.Entry<K,V>> i = entrySet().iterator();没有实现put(K key, V value)方法，只抛出了个异常，继承类应overwrite这个方法。不支持add(),remove()，remove(Obj key),使用correctEntry保存查出来的要删除的Entry,oldValue获得删除key的value来返回
  * SortedMap接口继承Map，有序的键值对。排序方式：自然排序，指定比较器排序(Comparator)@TestComparator.java方法内部通过传递参数key操作。
  * NavigableMap继承SortedMap:
  * 1.提供了操作键值对的方法：lowerEntry、floorEntry、cellingEntry和higherEntry方法分别返回小于、小于等于、大于等于和大于给定键的键所关联的Map.Entry对象。
  * 2.提供了操作键的方法：lowerKey、floorKey、cellingKey和higherKey方法分别返回小于、小于等于、大于等于和大于给定键的键。
  * 3.获取键值对的子集。
  * HashMap：散列表，存储键值对，实现不同步非线程安全
  * 整体结构，节点数组Node<K,V>[] table + 链表 Node<K,V> p + 红黑树,数组下标通过i = (n - 1) & hash获得。
  * put()方法:转入putVal(int hash,K key,V value,boolean onlyIfAbsent,boolean evict),key.hashCode()返回int2进制32位带符号-2147483648到2147483648，但是HashMap扩容前的数组初始大小16位,hash()"扰动函数"通过(n-1)&hash来确定table数组下标。
 &emsp;&ensp;BinaryTree  
  * 重难点，元素的删除  
      * 无子节点，节点指null，垃圾回收器自动回收该节点  
      * 一个子节点，父节点和唯一子节点相连  
      * 删除节点有两个子节点的时候，找到后继节点删除原节点：  
        * 	1.后继父节点left -> 后继节点右节点  
        * 	2.后继节点right -> 删除节点的右节点  
        * 	3.删除删除节点父节点下的删除节点，父节点 ->后继节点  
        * 	4.后继节点 ->删除节点的左节点   
        