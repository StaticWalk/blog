Bean分类： singleton prototype request session globalsession
singleton:这个bean在SpringContainer中有且一个，容器默认的生命周期级别
prototype:每次调用这个bean都会得到一个新实例
request、session、globalSession:在ApplicationContext中存在，
生命周期对等HTTP中Request Session Application

Spring Bean上下文的生命周期
1.实例化一个Bean，new
#GenericBeanDefinition

2.IOC注入，填充属性

3.实现了BeanNameAware接口，调用setBeanName(String beanid)，配置文件中的Bean的id
#通过Bean的引用来获取Bean的Id

4.实现了BeanFactoryAware接口，调用setBeanFactory(),传递Spring工厂本身
#用来获取Spring容器，如Bean通过Spring容器发布事件，需要指定注入的BeanFactory参数

5.实现了ApplicationContextAware接口，setApplicationContext(ApplicationContext)方法，
	传入Spring上下文
#把应用上下文 自己作为参数传入，目的类似4，获取Spring容器

6.关联了BeanPostProcessor接口的话，调用postProcessBeforeInitialization(Object ,String)
#对创建成功后的Bean进行增强或修改，在Bean初始化结束后会调用After方法，可以实现缓存技术

7.调用InitializingBean的afterPropertiesSet()
Bean在Spring配置文件中配置了init-method属性会调用配置中定制的初始化方法
#作用同7，都是在Bean全部属性设置成功后执行的初始化方法

8.关联了BeanPostProcessor接口的话，调用postProcessAfterInitialization(Object ,String)
#作用同6，Bean初始化结束后执行after方法，都是对Bean进行增强或者修改

：： Bean的创建完成 准备就绪，single形式存在，通过bean的id对实例进行调用

9.Bean的清理，如果实现DisposableBean 一次性 ，调用destory()
如果配置了destroy-method属性，调用定制的销毁方式
#执行需要在Bean销毁前进行的操作

1.加载Bean的方式都是通过Xml配置文件
2.ApplicationContext和BeanFacotry相比，更适合系统，提供了更多的扩展功能
	1.Bean没有完全注入ApplicationContext会在初始化的时候就加载并且检查，
		BeanFacotry加载后，会在你第一次调用GetBean方法才会抛出异常
	2.ApplicationContext接口是BeanFactory接口派生出来的，提供了BF的所有功能
		是面向框架的工作方式对上下文进行分层和实现继承
	3.BeanFactory不支持AOP、WEB应用插件

