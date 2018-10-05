参考博客 https://blog.csdn.net/songxinjianqwe/article/details/78824851

调试Demo，github：https://github.com/StaticWalk/spring-framework-4.3.0/tree/master/spring-demo/src/main/java/com/xxy/ioc    
IoC(Inversion of Control)控制反转，在最初的java对象之间的引用需要对象主动去绑定去控制其他对象为自己用，现在由
spring通过IoC容器BeanFactory来控制对象的生命周期和对象之间的关系，IoC是运行在系统中通过DI(依赖注入)动态向某个对象
提供所需的对象。    
spring的两种容器：BeanFactory ApplicationContext(BeanFactory子类，更高级的容器实现)，底层实现是一个Map   

Bean的实例化 -> Bean的

### 实例
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
### Bean的注册   
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
### bean的加载   
bean的加载是根据beanDefinition实例化bean的过程，可以认为getBean方法就是对bean的加载，getBean方法是缓存化的。bean注册里finishBeanFactoryInitialization中的getBean的执行流程不同于main方法中applicationContext.getBean的执行流程。   
Spring通过反射机制利用bean的class属性指定实现类来实例化bean。   
Spring提供了一个FactoryBean的工厂类接口，用户可以通过实现该接口定制实例化bean的逻辑。    
```angularjs
//FactoryBean用户定制
public interface FactoryBean<T> {
// 返回bean示例，如果isSingleton()返回true，那么该实例会放到Spring容器中单例缓存池中
   T getObject() throws Exception;
   Class<?> getObjectType();
   boolean isSingleton();
}

//ObjectFactor的Spring使用
public interface ObjectFactory<T> {
   T getObject() throws BeansException;
}

FactoryBean： 
  这个接口使你可以提供一个复杂的逻辑来生成Bean。它本质是一个Bean，但这个Bean不是用来注入到其它地方
像Service、Dao一样使用的，它是用来生成其它Bean使用的。实现了这个接口后，Spring在容器初始化时，把
实现这个接口的Bean取出来，使用接口的getObject()方法来生成我们要想的Bean。当然，那些生成Bean的业务
逻辑也要写getObject()方法中。 
ObjectFactory： 
  它的目的也是作为一个工厂，来生成Object（这个接口只有一个方法getObject()）。这个接口一般被用来，包
装一个factory，通过个这工厂来返回一个新实例（prototype类型）。这个接口和FactoryBean有点像，
但FactoryBean的实现是被当做一个SPI（Service Provider Interface）实例来使用在BeanFactory里面；
ObjectFactory的实现一般被用来注入到其它Bean中，作为API来使用。就像ObjectFactoryCreatingFactoryBean
的例子，它的返回值就是一个ObjectFactory，这个ObjectFactory被注入到了Bean中，在Bean通过这个接口的实例，
来取得我们想要的Bean。 
  总的来说，FactoryBean和ObjectFactory都是用来取得Bean，但使用的方法和地方不同，FactoryBean被配置好
后，Spring调用getObject()方法来取得Bean，ObjectFactory配置好后，在Bean里面可以取得ObjectFactory实例
，需要我们手动来调用getObject()来取得Bean。

```

```angularjs
FactoryBean                                                              ----用户定制
ObjectFactory                                                            ----Spring使用
AbstractBeanFactory.getBean
doGetBean
1)getSingleton(beanName)                                                 ----借助缓存或者singletonFactories
2)getSingleton(beanName,ObjectFactory)                                   ----从头创建单例bean(通过ObjectFactory的Object实例化bean)
  2.1)beforeSingletonCreation                                            ----记录加载状态
  2.2)afterSingletonCreation                                             ----清除辅助加载状态
  2.3)addSingleton                                                       ----结果记录至缓存
3)createBean                                                             ----创建单例或者多例的bean
  3.1)AbstractBeanDefinition.prepareMethodOverrides                      ----决定实例化策略->反射或者CGLIB
    3.1.1)prepareMethodOverride
  3.2)resolveBeforeInstantiation                                         ----避免创建已经代理过的bean
    3.2.1)applyBeanPostProcessorBeforeIntantiation                       ----实例化前的后置处理器应用
    3.2.2)applyBeanPostProcessorAfterIntantiation                      
                    ----实例化后的后置处理器应用，在bean的初始化后尽可能保证将注册的后处理器的postProcessAfterInitialization方法应用
                    到该bean中，如果返回的bean不为空，那么不再经历普通bean的创建过程。 
  3.3)doCreateBean                                                       ----创建常规bean
    3.3.1)createBeanInstance                                             ----实例化bean
      3.3.1.1)instantiateUsingFactoryMethod                              ----调用工厂方法实例化
      3.3.1.2)autowireContructor                                         ----有参数的构造方法实例化
        3.3.1.2.1)InstantiationStrategy.instantiate                      ----
      3.3.1.3)instantiateBean                                            ----无参数的构造方法的实例化
    3.3.2)getEarlyBeanReference                                          ----应用后处理器
    3.3.3)polulateBean                                                   ----属性值注入
      3.3.3.1)autowireByName                                             ----按名获取待注入属性
      3.3.3.2)autowireByType                                             ----按类型获取待注入属性
        3.3.3.2.1)DefaultListableBeanFactory.resolveDependency           ----寻找类型匹配
          3.3.3.2.1.1)doResolveDependency                                ----
      3.3.3.3)applyPropertValues                                         ----注入属性值
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

总结：ioc中的bean操作分两步，bean注册 -> bean加载，beanFactory全程作为bean的孵化中心，需要了解下工厂模式（是什么为什么怎么）    
bean的注册：   
1. 解析XML文件(XML -> Resource -> InputStream -> Document)注册BeanDefinition    
2. 解析文件中的标签分默认标签/自定义标签,(1.通过BeanDefinitionUri找到Hander/Class,2.从叫parses的解析Map找出解析器)    
3. 通过doScan()1找到所有需要管理的bean对应的beanDefinitions(1.递归拿到包下所有的class文件并抽象为Resource ，2.读取所有的class文件,3.逐个判断是否是需要的bean)，doScan2将beanDefinition注册记录到BeanFactory：DefaultListableBeanFactory.registerBeanDefinition --beanDefinitionMap.put(beanName,beanDefinition)     
4. 在后面的finishBeanFactoryInitialization会部分实例化Bean:通过getBean()方法初始化非lazy-load的singleton的bean，它能达到bean进行加载并缓存。    

bean的加载：   













