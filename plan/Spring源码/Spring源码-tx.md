参考博客：https://blog.csdn.net/songxinjianqwe/article/details/78827469    
10.14   
调试Demo，github：https://github.com/StaticWalk/spring-framework-4.3.0/tree/master/spring-demo/src/main/java/com/xxy/transaction    
Transaction概述：   
Spring Transaction事物功能模块依赖于Spring的AOP模块，由Spring tx模块实现。功能实现两部分，解析事物标签 + 创建事物代理。   
解析事物标签类似AOP的标签解析，<tx:annatation driven />标签会注册InfrastructureAdvisorAutoProxyCreator类和三个bean
(TransactionInterceptor和AnnotationTransactionAttributeSource这两个会注入BeanFactoryTransactionAttributeSourceAdvisor
这个bean实现了Advisor用于对事务方法进行增强)，只要类或方法实现了@Transaction接口，就会被加入到interceptor chain,对原方
法进行事务加强。   
而InfrastructureAdvisorAutoProxyCreator作为一个 AbstractAutoProxyCreator，会在getBean时调用其postProcessAfterInstantiation
方法创建事务代理。创建事务代理是对事务方法前后添加 开启、回滚、提交事务的功能，主要依赖于TransactionInterceptor来增强事务功能。   
事务介绍：   
声明式事务：管理建立在AOP之上的。其本质是对方法前后进行拦截，然后在目标方法开始之前创建或者加入一个事务，在执行完目标方法之后根据
执行情况提交或者回滚事务。声明式事务最大的优点就是不需要通过编程的方式管理事务，这样就不需要在业务逻辑代码中掺杂事务管理的代码，
只需在配置文件中做相关的事务规则声明(或通过基于@Transactional注解的方式)，便可以将事务规则应用到业务逻辑中。 
显然声明式事务管理要优于编程式事务管理，这正是spring倡导的非侵入式的开发方式。    
声明式事务管理使业务代码不受污染，一个普通的POJO对象，只要加上注解就可以获得完全的事务支持。和编程式事务相比
，声明式事务唯一不足地方是，后者的最细粒度只能作用到方法级别，无法做到像编程式事务那样可以作用到代码块级别。
但是即便有这样的需求，也存在很多变通的方法，比如，可以将需要进行事务管理的代码块独立为方法等等。     
解析事务标签：  
```angularjs
AnnotationDrivenBeanDefinitionParser.parse()              类似AOP标签解析，不同标签需要一个对应的BeanDefinitionParser解析器
    AopAutoProxyConfigurer.configureAutoProxyCreator()    注册了一个creator和三个支撑起整个事务功能的bean
    AopNamespaceUtils.registerAutoProxyCreatotIfNecessary()    
    AopConfigUtils.registerAutoProxyCreatorIfNecessary()
    BeanFactoryTransactionAttributeSourceAdvisor() 用于对事务方法进行增强
    与IOC的衔接
        InfrastructureAdvisorAutoProxyCreator.postProcessAfterInstantiation
            canApply 判断bean是否需要添加事务增强
                matches() 匹配方法
                    AnnotationTransactionAttributeAttributeSource,getTransactionAttribute 获取事务属性，封装
                        computeTransactionAttribute 提取事务注解
                            TransactionAnnotationParser.parseTransactionAnnotation 解析注解
    
```




