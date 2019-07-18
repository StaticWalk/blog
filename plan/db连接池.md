性能测试[https://www.tuicool.com/articles/qayayiM]    
druid自我评价[https://github.com/alibaba/druid/wiki/Druid%E8%BF%9E%E6%8E%A5%E6%B1%A0%E4%BB%8B%E7%BB%8D]    
      
推荐博文[https://www.cnblogs.com/xingzc/p/6073730.html]     
      
1.性能方面 hikariCP>druid>tomcat-jdbc>dbcp>c3p0 。hikariCP的高性能得益于最大限度的避免锁竞争。    
[https://github.com/brettwooldridge/HikariCP/wiki/Down-the-Rabbit-Hole]
* 字节码精简：优化代码，直到编译后的字节码最少，这样，CPU缓存可以加载更多的程序代码
* 优化代理和拦截器：减少代码，例如HikariCP的Statement proxy只有100行代码，只有BoneCP的十分之一
* 自定义数组类型（FastStatementList）代替ArrayList：避免每次get()调用都要进行range check，避免调用remove()时的从头到尾的扫描  
    可以看看[https://github.com/brettwooldridge/HikariCP/blob/dev/src/main/java/com/zaxxer/hikari/util/FastList.java]
* 自定义集合类型（ConcurrentBag）：提高并发读写的效率
    [https://github.com/brettwooldridge/HikariCP/blob/dev/src/main/java/com/zaxxer/hikari/util/ConcurrentBag.java]
    * A lock-free design无锁设计 cas
    * ThreadLocal caching线程本地缓存 threadLocal
    * Queue-stealing队列窃取 SynchronousQueue   
    * Direct hand-off optimizations直接移交优化

2.druid功能最为全面，安全防止sql，监控，稳定性，统计数据较为全面，具有良好的扩展性。    
可查看druid自评    
3.可开启prepareStatement缓存，对性能会有大概10%的提升。    
druid的说法是连接池的瓶颈在PSCache,但性能测试中开启psCache只上浮了10%。    