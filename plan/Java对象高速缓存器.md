### Java对象引用+ReferenceQueue实现Java对象的高速缓存  
Java对象的强、软、弱和虚引用(使程序能更加灵活地控制对象的生命周期)：  
1.强引用（StrongReference）:最普遍的引用，对象具有强引用，内存空间不足，JVM宁愿抛出OutOfMemoryError错误，GC绝不会回收它。  
2.软引用（SoftReference）:如果对象只具有软引用，内存空间足够，GC不会回收；内存空间不足，就会回收这些对象的内存。软引用可实现内存敏感的高速缓存。  
3.弱引用（WeakReference：相对于软引用的区别是就算内存空间足够，GC遇见弱引用对象也会回收。由于GC是一个较低优先级的线程，不会很快发现弱引用。  
&emsp;&emsp;弱引用与软引用可以和一个引用队列（ReferenceQueue）联合使用，如果该引用所引用的对象被GC回收，JVM会把这个引用加入到与之关联的引用队列。  
4.虚引用（PhantomReference）：用来跟踪对象被GC回收前的活动，虚引用必须和引用队列 （ReferenceQueue）联合使用。当垃圾回收器准备回收一个对象时，如果发现它有虚引用，就会在回收对象的内存之前，把这个虚引用加入到与之关联的引用队列中。  
  
Java对象可及性的判断：   
&emsp;&emsp;◆单条引用路径可及性判断:在这条路径中，最弱的一个引用决定对象的可及性   
&emsp;&emsp;◆多条引用路径可及性判断:几条路径中，最强的一条的引用决定对象的可及性   
  
使用软引用构建敏感数据的缓存（关键在于JVM回收软可及对象是在虚拟机抛出OutOfMemoryError之前）：  
&emsp;&emsp;SoftReference特点是它的一个实例保存对一个Java对象的软引用，该软引用的存在不妨碍垃圾收集线程对该Java对象的回收。也就是说，一旦SoftReference保存了对一个Java对象的软引用后，在垃圾线程对这个Java对象回收前，SoftReference类所提供的get()方法返回Java对象的强引用。另外，一旦垃圾线程回收该Java对象之后，get()方法将返回null。  
&emsp;&emsp;MyObject aRef = new  MyObject();  
&emsp;&emsp;SoftReference aSoftRef=new SoftReference(aRef);  
当我们结束aReference对这个MyObject实例的强引用:aRef = null之后，这个MyObject对象成为软可及对象，JVM回收软可及对象是在虚拟机抛出OutOfMemoryError之前，而且优先回收长时间不用的软可及对象，刚刚使用过的“新”软可反对象会被虚拟机尽可能保留。回收这些对象之前，我们可以通过: MyObject anotherRef=(MyObject)aSoftRef.get(); 重新获得对该实例的强引用。  
  
使用ReferenceQueue清除失去了软引用对象的SoftReference：   
SoftReference对象除了具有保存软引用的特殊性之外，也具有Java对象的一般性。当软可及对象被回收之后，虽然这个SoftReference对象的get()方法返回null,但这个SoftReference对象已经不再具有存在的价值，需要一个适当的清除机制，避免大量SoftReference对象带来的内存泄漏。在java.lang.ref包里还提供了ReferenceQueue。如果在创建SoftReference对象的时候，使用了一个ReferenceQueue对象作为参数提供给SoftReference的构造方法。在任何时候，我们都可以调用ReferenceQueue的poll()方法来检查是否有它所关心的非强可及对象被回收。如果队列为空，将返回一个null,否则该方法返回队列中前面的一个Reference对象。利用这个方法，我们可以检查哪个SoftReference所软引用的对象已经被回收。于是我们可以把这些失去所软引用的对象的SoftReference对象清除掉。  
&emsp;&emsp;ReferenceQueue queue = new  ReferenceQueue();  
&emsp;&emsp;SoftReference  EmployeeRef=new  SoftReference(aMyObject, queue);  
&emsp;&emsp;SoftReference ref = null;  
&emsp;&emsp;while ((ref = (EmployeeRef) q.poll()) != null) {  
&emsp;&emsp;   // 清除ref  
&emsp;&emsp;}  
  
使用弱引用构建非敏感数据的缓存（全局Map造成的内存泄漏，用WeakHashMap修复SocketManager。）：  
无意识对象保留最常见的原因是使用Map将元数据与临时对象（transient object）相关联。假定一个对象具有中等生命周期，比分配它的那个方法调用的生命周期长，但是比应用程序的生命周期短，如客户机的套接字连接。需要将一些元数据与这个套接字关联，如生成连接的用户的标识。在创建Socket时是不知道这些信息的，并且不能将数据添加到Socket对象上，因为不能控制Socket类或者它的子类。这时，典型的方法就是在一个全局Map中存储这些信息，如下面的SocketManager类所示：使用一个全局Map将元数据关联到一个对象。在 SocketManager 中防止泄漏很容易，只要用 WeakHashMap 代替 HashMap 就行了。（这里假定SocketManager不需要线程安全）。当映射的生命周期必须与键的生命周期联系在一起时，可以使用这种方法。  
public class SocketManager {  
&emsp;&emsp;private Map<Socket,User> m = new WeakHashMap<Socket,User>();  
&emsp;&emsp;public void setUser(Socket s, User u) {  
&emsp;&emsp;&emsp;&emsp;m.put(s, u);  
&emsp;&emsp;}  
&emsp;&emsp;public User getUser(Socket s) {  
&emsp;&emsp;&emsp;&emsp;return m.get(s);  
&emsp;&emsp;}  
}