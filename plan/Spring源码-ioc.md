参考博客 https://blog.csdn.net/songxinjianqwe/article/details/78824851

IoC(Inversion of Control)控制反转，在最初的java对象之间的引用需要对象主动去绑定去控制其他对象为自己用，现在由
spring通过IoC容器BeanFactory来控制对象的生命周期和对象之间的关系，IoC是运行在系统中通过DI(依赖注入)动态向某个对象
提供所需的对象。    
spring的两种容器：BeanFactory ApplicationContext(BeanFactory子类，更高级的容器实现)，底层实现是一个Map   
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
```angularjs
AbstractApplicationContext.refresh()                                     ----bean注册
 1)obtainFreshBeanFactory                                                ----创建beanFactory，解析XML
 1.1)refreshBeanFactory
 1.1.1)loadBeanDefinitions(beanFactory)                                  ----创建reader
 1.1.1.1)loadBeanDefinitions(beandefinitionReader)                       ----调用reader的load
 1.1.1.1.1)XmlBeanDefinitionReader.loadBeanDefinitions                   ----解析标签
    doLoadBeanDefinitions
    registerBeanDefinitions
    documentReader.registerBeanDefinitions
    doRegisterBeanDefinitions
    parseBeanDefinitions
    parseDefaultElement/parseCustomElement                               ----解析默认/自定义标签
    NamespaceHandlerSupport.parse
    a)findParseForElement
    b)ComponentScanBeanDefinitionParser.parse                            ----返回解析结果Set<BeanDefinitionHolder>然后注册组件
        1)ClassPathBeanDefinitionScanner.doScan                          ----解析注解定义的bean
            1.1）findCandidateComponents
                1.1.1)PathMatchingResourcePatternResolver.getResources   ----Resource[]
                    1.1.1.1)findPathMatchingResources                    ----Resource[]
                    1.1.1.1.1)doFindPathMatchingResources                ----Set<Resource>                
                    1.1.1.1.1.1)retrieveMatchingFiles                    ----((Set(Resource)Set<File>)matchingFiles存放扫描到的.class文件
                    1.1.1.1.1.1.1)doRetrieveMatchingFiles                ----递归方法
                1.1.2)CachingMetadataResourceFactory.getMetadataReader   ----读取class文件
                    1.1.2.1)SimpleMetadataReader.getMetadataReader
                1.1.3)isCandiddateComponent
                    1.1.3.1)AbstractTypeHierarchyTraversingFilter.match
            1.2)registerBeanDefinition                                   ----将beanDefinition记录到BeanFactory
                1.2.1)DefaultListableBeanFactory.registerBeanDefinition  ----beanDefinitionMap.put(beanName,beanDefinition)        
2)finishBeanFactoryInitialization                                        ----初始化非lazy-load且singleton的bean(会加载部分的bean)   
  2.1)ConfigurableListableBeanFactory.preInstantiateSingletons           ----DefaultListableBeanFactory.preInstantiateSingletons,getBean()会缓存已经加载过、单例的bean 
                                                                                      
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








