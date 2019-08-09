Java8:
optional
1.Lambda表达式   函数式编程关心数据的映射，命令式在于解决问题的步骤
函数作为参数传入方法中，替代匿名内部类
2.接口引入默认方法（代han'sh码实现）和静态方法
之前默认 public abstract 不能实现代码
3.JVM新特性
    原空间Metaspace取代永久保存区PermGen(字符串常量池)
    JVM可使用内存空间默认无限制，使用本地内存
4.支持js Nashorn JavaScript
5.并行数组
并行数组排序
6.stream并行流 filter
极大得简化了集合操作、IO
创造性地支持并行处理

CAS unsafe类，原子操作类  aba 循环时间长 只能保证一个共享变量的原子操作AtomicReference
处理器汇编指令 Atomic:cmpxchg，运算中非单核处理器加lock前缀

模糊查询让索引失效：
后模糊查询不会失效，
如果使用前模糊索引的话，翻转函数reverse + like前模糊查询 + 简历反转函数索引 = 翻转函数索引

linux查找大文件指定内容：
cat info.log | grep 'target obj'
内容太多的话可 >> temp.log 暂存中间结果
最后通过more less来查看temp文件

http报文首部哪些属性：
accept:text/plain 告诉服务器客户端能接收的相应类型为纯文本数据
客户端cookie
referer:白哦是请求是从哪个url过来的
cache-control缓存控制 
Connection 连接控制 close keep-alive
Date 日期时间

什么是反射：（反射调用方法的时候会忽略权限检查，因此可能破坏封装性而导致安全问题）
程序允许运行中的Java程序获取自身的信息，并且可以操作类或者对象内部属性。
反射的核心：JVM在运行时动态加载类或调用方法/访问属性
功能：
运行时判断任意一个对象所属的类
运行时构造任意一个类的对象
在运行时判断任意一个类所具有的成员变量和方法（通过反射甚至可以调用private方法）
在运行时调用任意一个对象的方法
基本应用:
1.获得class对象 
    Class.forName(driver)
    Class klass = int.class;
    Class klass = new StringBuilder("123").getClass()
2.判断是否为某一个类的实例
    isInstance(obj)
3.反射来创建实例
   class对象的newInstance()方法来创建Class对象对应类的实例
   ```
   Class<?> c = Strieng.class;
   Object str = c.newInstance();
   ```
  根据class对象获取指定的Constructor，在调用Constructor的newInstance()来创建对应类的实例
   ```
     //获取String所对应的Class对象
     Class<?> c = String.class;
     //获取String类带一个String参数的构造器
     Constructor constructor = c.getConstructor(String.class);
     //根据构造器创建实例
     Object obj = constructor.newInstance("23333");
   ```   
4.获取方法
  getDeclaredMethods 方法返回类或接口声明的所有方法，包括公共、保护、默认（包）访问和私有方法，但不包括继承的方法。
  getMethods 方法返回某个类的所有公用（public）方法，包括其继承类的公用方法。
  getMethod(String name, Class<?>... parameterTypes)方法返回一个特定的方法，其中第一个参数为方法名称，后面的参数为方法的参数对应Class的对象
5.获取构造器信息
  通过Class类的getConstructor方法得到Constructor类的一个实例，而Constructor类有一个newInstance方法可以创建一个对象实例
6.获取类的成员变量（字段）信息
  getFileds 和 getDeclaredFields 方法用法同上
7.  
```
    Class<?> klass = methodClass.class;
        //创建methodClass的实例
        Object obj = klass.newInstance();
        //获取methodClass类的add方法
        Method method = klass.getMethod("add",int.class,int.class);
        //调用method对应的方法 => add(1,4)
        Object result = method.invoke(obj,1,4);
        System.out.println(result);
```
  