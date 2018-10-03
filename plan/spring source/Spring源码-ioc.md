参考博客 https://blog.csdn.net/songxinjianqwe/article/details/78824851

调试Demo，github：https://github.com/StaticWalk/spring-framework-4.3.0/tree/master/spring-demo/src/main/java/com/xxy/ioc
IoC(Inversion of Control)控制反转，在最初的java对象之间的引用需要对象主动去绑定去控制其他对象为自己用，现在由
spring通过IoC容器BeanFactory来控制对象的生命周期和对象之间的关系，IoC是运行在系统中通过DI(依赖注入)动态向某个对象
提供所需的对象。    
spring的两种容器：BeanFactory ApplicationContext(BeanFactory子类，更高级的容器实现)，底层实现是一个Map   

Bean的实例化 -> Bean的

###实例
```angularjs
public class Main {
    public static void main(String[] args) {
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("applicationContext.xml");
        UserService userService = (UserService) applicationContext.getBean("userService");
        userService.login();
    }
}

public interface UserService {
    void login();
}

@Service("userService")
public class UserServiceImpl implements UserService{
    @Override
    public void login() {
        System.out.println("login...");
    }
}
```
applicationContext.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xsi:schemaLocation="
        http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd
        ">

    <context:component-scan
            base-package=
                    "cn.sinjinsong.ioc"/>
</beans>
```
###Bean的注册   
```angularjs  delegate代表
AbstractApplicationContext.refresh()                                     ----bean注册
 1)obtainFreshBeanFactory                                                ----创建beanFactory，解析XML
 1.1)refreshBeanFactory
 1.1.1)loadBeanDefinitions(beanFactory)                                  ----创建reader  XmlBeanDefinitionReader for the given BeanFactory
 1.1.1.1)loadBeanDefinitions(beandefinitionReader)                       ----调用reader的load
 1.1.1.1.1)XmlBeanDefinitionReader.loadBeanDefinitions                   ----解析标签
    doLoadBeanDefinitions                       
    registerBeanDefinitions
    documentReader.registerBeanDefinitions                               ----实现类是DefaultBeanDefinitionDocumentReader
    doRegisterBeanDefinitions(Element root)                              ----注册BeanDefinition
    parseBeanDefinitions(root,this.delegate)                             ----解析标签，会将默认标签和自定义标签分开解析
    parseDefaultElement/parseCustomElement                               ----解析默认/自定义标签，else的deletgate是NamespaceHandlerSupport类型
    NamespaceHandlerSupport.parse                                        ----选择
    a)findParseForElement(element, parserContext).parse(element, parserContext)
    b)ComponentScanBeanDefinitionParser.parse                            ----返回解析结果Set<BeanDefinitionHolder>然后注册组件
        1)ClassPathBeanDefinitionScanner.doScan                          ----解析注解定义的bean将其转为beanDefinition
            1.1）findCandidateComponents                                 ----doScan1找到所有需要管理的bean对应的beanDefinitions
                1.1.1)PathMatchingResourcePatternResolver.getResources   ----未筛选拿到所有的class文件并抽象为Resource文件
                    1.1.1.1)findPathMatchingResources                    ----Resource[]
                    1.1.1.1.1)doFindPathMatchingResources                ----Set<Resource>                
                    1.1.1.1.1.1)retrieveMatchingFiles                    ----((Set(Resource)Set<File>)matchingFiles存放扫描到的.class文件
                    1.1.1.1.1.1.1)doRetrieveMatchingFiles                ----递归方法
                1.1.2)CachingMetadataResourceFactory.getMetadataReader   ----读取所有刚刚拿到的class文件
                    1.1.2.1)SimpleMetadataReader.getMetadataReader       ----Metadata元数据
                1.1.3)isCandiddateComponent                              ----判断class文件是否是注册在Spring中的bean类型
                    1.1.3.1)AbstractTypeHierarchyTraversingFilter.match
            1.2)registerBeanDefinition                                   ----doScan2将beanDefinition注册记录到BeanFactory
                1.2.1)DefaultListableBeanFactory.registerBeanDefinition  ----beanDefinitionMap.put(beanName,beanDefinition)        
2)finishBeanFactoryInitialization                                        ----初始化非lazy-load且singleton的bean(会加载部分的bean)   
  2.1)ConfigurableListableBeanFactory.preInstantiateSingletons           ----DefaultListableBeanFactory.preInstantiateSingletons,getBean()会缓存已经加载过、单例的bean，AbstracBeanFactory中的mergedBeanDefinitions存放缓存合并过的beanDefinition
                                                                                      
```
###bean的加载   
bean的加载是根据beanDefinition实例化bean的过程，可以认为getBean方法就是对bean的加载，getBean方法是缓存化的。finishBeanFactoryInitialization中的getBean的执行流程不同于main方法中applicationContext.getBean的执行流程。
```angularjs
FactoryBean                                                              ----用户定制
ObjectFactory                                                            ----Spring使用
AbstractBeanFactory.getBean
doGetBean
1)getSingleton(beanName)                                                 ----借助缓存或者singletonFactories
2)getSingleton(beanName,ObjectFactory)                                   ----从头创建单例bean
  2.1)beforeSingletonCreation                                            ----记录加载状态
  2.2)afterSingletonCreation                                             ----清除加载状态
  2.3)addSingleton                                                       ----结果记录至缓存
3)createBean                                                             ----创建单例或者多例的bean
  3.1)AbstractBeanDefinition.prepareMethodOverrides                      ----决定实例化策略->反射或者CGLIB
    3.1.1)prepareMethodOverride
  3.2)resolveBeforeInstantiation                                         ----可能会创建代理过的bean
    3.2.1)applyBeanPostProcessorBeforeIntantiation                       ----实例化前的后处理器应用
    3.2.2)applyBeanPostProcessorAfterIntantiation                        ----实例化后的后处理器应用
  3.3)doCreateBean                                                       ----创建常规bean
    3.3.1)createBeanInstance                                             ----实例化bean
      3.3.1.1)instantiateUsingFactoryMethod                              ----工厂方法实例化
      3.3.1.2)autowireContructor                                         ----有参数的构造方法实例化
        3.3.1.2.1)InstantiationStrategy.instantiate                      ----
      3.3.1.3)instantiateBean                                            ----无参数的构造方法的实例化
    3.3.2)getEarlyBeanReference                                          ----
    3.3.3)polulateBean                                                   ----
      3.3.3.1)autowireByName                                             ----
      3.3.3.2)autowireByType                                             ----
        3.3.3.2.1)DefaultListableBeanFactory.resolveDependency           ----
          3.3.3.2.1.1)doResolveDependency                                ----
      3.3.3.3)applyPropertValues                                         ----
    3.3.4)initializeBean                                                 ----调用init-method方法
      3.3.4.1)invokeAwareMethods                                         ----
      3.3.4.2)BeanPostProcessor                                          ----
      3.3.4.3invokeInitMethods                                           ----激活自定义的init方法
        3.3.4.1)invokeCustomInitMethod                                   ----
    3.3.5)getSingleton(beanName,allowEarlyReference)                     ----
    3.3.6)registerDisposableBeanIfNecessary                              ----注册DisposableBean
4)getObjectForBeanInstance                                               ----从bean实例中获取对象
  4.1)getObjectFromFactoryBean                                           ----从FactoryBean中解析bean
    4.1.1)doGetObejectFromFactoeyBean                                    ----
```

总结：ioc中的bean操作分两步，bean注册 -> bean加载，beanFactory作为bean的全程孵化中心，需要了解下工厂模式（是什么为什么怎么）    
bean的注册：   
1. 解析XML文件(XML -> Resource -> InputStream -> Document)注册BeanDefinition    
2. 解析文件中的标签分默认标签/自定义标签,(1.通过BeanDefinitionUri找到Hander/Class,2.从叫parses的解析Map找出解析器)    
3. 通过doScan()1找到所有需要管理的bean对应的beanDefinitions(1.递归拿到包下所有的class文件并抽象为Resource ，2.读取所有的class文件,3.逐个判断是否是需要的bean)，doScan2将beanDefinition注册记录到BeanFactory：DefaultListableBeanFactory.registerBeanDefinition --beanDefinitionMap.put(beanName,beanDefinition)     
4. 在后面的finishBeanFactoryInitialization会部分实例化Bean:通过getBean()方法初始化非lazy-load的singleton的bean，它能达到bean进行加载并缓存。    

bean的加载：   












