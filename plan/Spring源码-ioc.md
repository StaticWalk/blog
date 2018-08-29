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
    b)ComponentScanBeanDefinitionParser.parse
        1)ClassPathBeanDefinitionScanner.doScan                          ----解析注解定义的bean
            1.1）findCandidateComponents
                1.1.1)PathMatchingResourcePatternResolver.getResources
                    1.1.1.1)findPathMatchingResources
                    1.1.1.1.1)doFindPathMatchingResources
                    1.1.1.1.1.1)retrieveMatchingFiles
                    1.1.1.1.1.1.1)doRetrieveMatchingFiles                ----递归方法
                1.1.2)CachingMetadataResourceFactory.getMetadataReader   ----读取class文件
                    1.1.2.1)SimpleMetadataReader.getMetadataReader
                1.1.3)isCandiddateComponent
                    1.1.3.1)AbstractTypeHierarchyTraversingFilter.match
            1.2)registerBeanDefinition                                   ----将beanDefinition记录到BeanFactory
                1.2.1)DefaultListableBeanFactory.registerBeanDefinition  ----保存beanDefinition        
2)finishBeanFactoryInitialization                                        ----初始化非lazy-load且singleton的bean                        
```








