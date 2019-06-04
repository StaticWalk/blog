参考文章[https://segmentfault.com/a/1190000011668299],
[https://blog.csdn.net/forezp/article/details/73017664]

特点：
1.Eureka Server提供注册，服务注册表存储所有可用的服务节点的信息，
2.Eureka Client是Java客户端，内置轮询算法的负载均衡器
3.Client发的心跳30s,超时90s
4.Server之前通过复制方式完成数据的同步
5.Client可以访问本地的缓存表，即使server都挂掉了，仍可以利用缓存中的信息消费其他的API

Eureka Server 
```angular2
2019-06-03 09:54:40.273  INFO 11184 --- [           main] o.s.c.support.DefaultLifecycleProcessor  : Starting beans in phase 0
2019-06-03 09:54:40.273  INFO 11184 --- [           main] c.n.e.EurekaDiscoveryClientConfiguration : Registering application unknown with eureka with status UP
2019-06-03 09:54:40.274  INFO 11184 --- [      Thread-30] o.s.c.n.e.server.EurekaServerBootstrap   : Setting the eureka configuration..
2019-06-03 09:54:40.274  INFO 11184 --- [      Thread-30] o.s.c.n.e.server.EurekaServerBootstrap   : Eureka data center value eureka.datacenter is not set, defaulting to default
2019-06-03 09:54:40.274  INFO 11184 --- [      Thread-30] o.s.c.n.e.server.EurekaServerBootstrap   : Eureka environment value eureka.environment is not set, defaulting to test
2019-06-03 09:54:40.282  INFO 11184 --- [      Thread-30] o.s.c.n.e.server.EurekaServerBootstrap   : isAws returned false
2019-06-03 09:54:40.283  INFO 11184 --- [      Thread-30] o.s.c.n.e.server.EurekaServerBootstrap   : Initialized server context
2019-06-03 09:54:40.287  INFO 11184 --- [      Thread-30] e.s.EurekaServerInitializerConfiguration : Started Eureka Server
2019-06-03 09:54:40.371  INFO 11184 --- [           main] s.b.c.e.t.TomcatEmbeddedServletContainer : Tomcat started on port(s): 8761 (http)
2019-06-03 09:54:40.371  INFO 11184 --- [           main] c.n.e.EurekaDiscoveryClientConfiguration : Updating port to 8761
2019-06-03 09:54:40.375  INFO 11184 --- [           main] c.t.eurekasvr.EurekaServerApplication    : Started EurekaServerApplication in 11.742 seconds (JVM running for 13.116)
```
先看日志
EurekaServerBootstrap
EurekaServerInitializerConfiguration 中开启一个线程调用start()来初始化 EurekaServer
DefaultLifecycleProcessor 的doStart方法调用了 bean.start();

通过@EnableEurekaServer注解验证思路：
1.@EnableEurekaServer中import了@EurekaServerConfiguration(里面很多有全局的注释Bean Context Init Server)
EurekaServerConfiguration中包含的Bean:
eurekaServerBootstrap
eurekaServerContext.initialize（DefaultEurekaServerContext.java）//主要的执行初始化逻辑
peerEurekaNodes.start() //每10分钟执行一次服务集群数据同步
peerAwareInstanceRegistry.init（PeerAwareInstanceRegistryImpl.java） //初始化响应缓存、心跳阈值定时任务、远程客户端
eurekaController
2.@EurekaServerConfiguration中import了@EurekaServerInitializerConfiguration

peerAwareInstanceRegistry.OpenForTraffic() // 设置与Server的续约时间每分钟2次，更新Server状态为上电状态
EurekaDiscoveryClientConfiguration.onApplicationEvent() //设置Server的运行端口

总结：
1、初始化Eureka环境，Eureka上下文；
2、初始化EurekaServer的缓存
3、启动了一些定时任务，比如充值心跳阈值定时任务，清理失效节点定时任务；
4、更新EurekaServer上电状态，更新EurekaServer端口；


EurekaClient如何注册到EurekaServer
```angular2
public class InstanceRegistry extends PeerAwareInstanceRegistryImpl
		implements ApplicationContextAware {
``` 
ApplicationResource.addInstance() // 处理HTTP请求服务
InstanceRegistry.register //通过 ApplicationContext 发布了一个事件 EurekaInstanceRegisteredEvent 服务注册事件
PeerAwareInstanceRegistryImpl.register // 将注册方信息填入注册表（续约时间、名字、数据同步）
AbstractInstanceRegistry.register（super） //将注册表放到内存中gMap维护，定时更新注册表和更新缓存
PeerAwareInstanceRegistryImpl.replicateToPeers // 在服务节点之间同步信息
