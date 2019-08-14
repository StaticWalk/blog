* 什么是Dubbo
基于Java的高性能RPC分布式服务框架

* 为什么要用Dubbo
内部使用Netty、Zookeeper保证高性能高可用性，
将核心业务抽取出来，作为独立服务，逐渐形成稳定的服务中心，提升
业务复用灵活扩展，分布式架构可以承受更大规模的并发流量

* Dubbo和SpringCloud的区别
1.Dubbo使用RPC也可以HTTP RESTFul；SpringCloud使用HTTP RESTFul
2.Dubbo组件只有服务注册中心、服务监控
SpringCloud还支持断路器、服务网关、分布式配置、服务跟踪、消息总线、数据流、批量任务

* dubbo支持什么协议，推荐使用哪种
dubbo://(支持)  rmi hessian http webservice thrift memcached redis rest

* dubbo需要web容器吗
不需要，会增加复杂性浪费资源

* dubbo内置哪几种服务容器
Spring Container
Jetty Container
Log4j Container
只是一个Main方法，用于加载一个简单的Spring容器，用于暴露服务

* Dubbo中的节点角色
Provider 暴露服务的服务提供方
Consumer 调用远程服务的服务消费方
Registry 服务注册和发现的注册中心
Monitor 统计服务的调用次数和调用时间的监控中心
Container 服务运行容器

* 默认的注册中心，其他选择
默认zk，还有redis Multicast Simple但不推荐

* 有哪些配置方式
Spring配置、JavaApi配置方式

* 核心配置有哪些
dubbo:service 服务配置
dubbo:reference 引用配置
dubbo:protocol 协议配置




