参考博客：https://blog.csdn.net/songxinjianqwe/article/details/78826293   
10.1   
横切关注点：   
散布于应用多处的功能（影响引用多处的功能）    
面向切面编程（aspect oriented programming）:   
关注点在于怎么把横向关注点与业务逻辑相分离，实现横切关注点和他们所影响的对象之间的解耦   
应用场景：   
日志、声明式事物、安全和缓存    
AOP术语   
1、切面（aspect）   
类是对物体特征的抽象，切面就是对横切关注点的抽象      
2、连接点（joinpoint）    
被拦截到的点，因为Spring只支持方法类型的连接点，所以在Spring中连接点指的就是被拦截到的方法，实际上连接点还可以是字段或者构造器    
3、切入点（pointcut）    
对连接点进行拦截的定义    
4、通知（advice）    
所谓通知指的就是指拦截到连接点之后要执行的代码，通知分为前置、后置、异常、返回、环绕通知五类    
5、目标对象    
代理的目标对象    
6、织入（weave）    
将切面应用到目标对象并导致代理对象创建的过程    
7、引介（introduction）    
在不修改代码的前提下，引介可以在运行期为类动态地添加一些方法或字段   
AOP概述
AOP 代理可以分为两个部分：解析AOP标签和创建AOP代理。这两个部分都与IOC容器有关。如想了解AOP源码请先了解IOC源码。   
1.解析AOP标签发生在IOC的解析标签的过程，即解析自定义标签 <aop:aspectj-autoproxy />，解析结果是在BeanFactory中注册了一个名为AnnotationAwareAspectJAutoProxyCreator的bean，用于创建AOP代理。   
2.创建AOP代理发生在IOC的createtBean中，在doCreateBean之前会先调用resolveBeforeInstantiation方法，在该方法中会调用实现了BeanPostProcessor接口的后处理的postProcessAfterInstantiation方法。   
而在解析AOP标签中注册的AnnotationAwareAspectJAutoProxyCreator便实现了BeanPostProcessor接口。AnnotationAwareAspectJAutoProxyCreator会在postProcessAfterInstantiation方法中根据定义的advisor，使用JDK动态代理或CGLIB动态代理来增强bean。


