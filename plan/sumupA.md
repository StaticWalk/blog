3月25日一周总结  
&emsp;&ensp;先是了解了下抽象类定义，看了下AbstractCollection,AbstractList：  
抽象类不能实例化（Java规定），视觉上的抽象类实例化其实是创建了一个匿名内部类子类；  
继承实现一个抽象类，必须根据所需功能重写实现抽象类中的方法；   
抽象类本身和被继承的类都有一个protected()无参构造器；   
AbstractCollection中实现了一个私有类Itr；  
Object类常用做集合类中toArray的转化类型；  
&emsp;&ensp;transient关键字(不序列化某个变量)：  
1.变量被transient修饰后，该多项不是处对象持久化的一部分，序列化后不能再度获取；  
2.transient只修饰变量，不修饰方法和类改类应实现Serializable（所有内容会被自动序列化），Externalizable（内容需要手工序列化）接口，也不能修饰本地变量；  
3.被transient关键字修饰的变量和静态变量均不能被序列化；  
4.在实现的Externalizable序列化接口中，不手动序列化的话，transient无效；  
5.反序列化的static稀释变量的值是JVM中对应的static变量值；  
&emsp;&ensp;ArrayDeque:  
  * ArrayDeque是一个双端队列，支持首尾两端的操作
  * ArrayDeque不是线程安全的，不能存取null元素，系统通过某位置是否为null来判断元素的存在
  * transient关键字 短暂的,在实现了Serializable接口的类中，在不需要序列化的属性前添加，该属性不会被序列化
  *	LinkedList内部实现使用了node节点链接前后元素(长处在于中间节点的增删操作为o(1))
  *	vector方法加了synchronized修饰(同步，将带来性能的损耗)，Stack继承了vector
  *	ArrayDeque底层是单纯的数字操作，性能更强，但是无同步处理，存在并发问题。
  *	allocateElements(),最大容量扩容，巧妙运用二进制移位，全程只有一个变量。
  * doubleCapacity(),容量翻倍，再来一组相同数据接在尾部。
  * isEmpty(),size(),pollFirst(),pollLast():
  * arraydeque实现双端队列用了循环数组,存在tail<head的情况，要用&(elements.length-1)转正值
  * length必须是2的幂指数，当tail<head，取(tail-head)补码&(elements.length-1)可求得size
  *	addLast()在tail=length-1的时候会扩容，"elements[tail] = e"可以执行  
 &emsp;&ensp;ArrayList:  
  *	动态数组，容量自动增长,类似于c语言动态内存申请。非线程安全，只能用于单线程，
  *	多线程通过Collection.synchronizedList(List l)返回一个线程安全的ArrayList类，或者使用concurrent并发包下的CopyOnWriteArrayList类。
  *	Serializable接口，支持序列化，能序列化传输；RandomAccess接口，支持通过下标序号的快速随机访问；Cloneable接口，能被克隆。
  *	void grow(int minCapacity),容量增长，minCapacity是最小需要扩容，
  * 1.容量x1.5;	2.判断够不够minCapacity，不够取minCapacity;	3.对比MAX_ARRAY_SIZE(Integer.MAX_VALUE-8),hugeCapacity()检查溢出，返回MAX或者Integer.MAX_VALUE;4.Array.copyOf(),<T> T[] copyOf(T[] original, int newLength)
  * void trimToSize(),缩小容量,调整当前容量为实际元素个数
 &emsp;&ensp;Vector:  
  * 基于数组实现，动态数组容量能自动增长；多数方法加入了同步语句，相对线程安全可用于多线程环境实际使用中不是线程安全的，在迭代中调用元素操作的方法实质操作的iterator中的方法，是不能进行synchronized同步的。
  * 大体上和ArrayList差不多，多数方法加入了synchronized同步语句来同步线程，但仍然引入modCount来避免迭代的时候线程交替操作元素，Vector中元素的处理分为是否为null，其中允许元素为null
  * 测试vector四种遍历方法的效率
  * Iterator > RandomAccess > For2 > Enumeration
  * 其中的Enumeration早于Iterator出现，方法：boolean hasMoreElements(),Object nextElement()
  *	 Enumeration迭代器只能遍历Vector、Hashtable这种古老的集合，因此通常不要使用它，除非在某
  *	 些极端情况下，不得不使用Enumeration，否则都应该选择Iterator迭代器。
 &emsp;&ensp;modCount:  
  * modify count修改次数，记录ArrayList,LinkedList,HashMap等非线程安全类的内部增删改实现
  * ArrayList的remove(int index),remove(O o),remove(int fromIndex,int toIndex),add会修改掉modCount的值
  * ArrayList实现的hasNext(),return cursor!=size();当remove()后cursor=1,size()=0,外部陷入死循环，next()中引入modCount通过checkForComodification，判断满足i>=size,抛出ConcurrentModificationException()。
  * 非线程安全的集合操作中，避免一个线程正在迭代遍历被另外的线程修改这个列表的结构，引入了
  * ConcurrentModificationException。异常原因和解决办法：
  * 1.异常出现的原因：调用list.remove()方法导致modCount和expectedModCount的值不一致。
  * 2.单线程下的解决办法：使用迭代器自带的iterator.remove()删除元素
  * 3.多线程下的解决办法：1）在使用iterator迭代的时候使用synchronized或者Lock进行同步；　2）使用并发容器CopyOnWriteArrayList代替ArrayList和Vector