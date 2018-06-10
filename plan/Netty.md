Netty学习整理&emsp;&ensp;https://www.zhihu.com/question/24322387/answer/282001188 &emsp;&ensp; https://blog.csdn.net/linuu      
Netty可以实现HTTP服务器、FTP服务器，UDP服务器，RPC服务器，WebSocket服务器，Redis的Proxy服务器，MySQL的Proxy服务器等等   
传统的HTTP服务器原理：    
1.创建一个ServerSocket，监听并绑定一个端口   
2.一系列客户端来请求这个端口   
3.服务器使用Accept，获得一个来自客户端的Socket连接对象  
4.启动一个新线程处理连接   
&emsp;&ensp;1.读Socket，得到字节流   
&emsp;&ensp;2.解码协议，得到Http请求对象   
&emsp;&ensp;3.处理Http请求，得到一个结果，封装成一个HttpResponse对象   
&emsp;&ensp;4.编码协议，将结果序列化字节流   
&emsp;&ensp;5.写Socket，将字节流发给客户端   
5.继续循环步骤3   
服务器类型区分取决于编码解码协议，HTTP服务器的编码解码协议是HTTP协议   
可以通过Netty定制编码解码协议来实现自己的特定协议服务器。   
Netty是基于Java NIO技术封装的一套框架，较使用Java原生API更简单的去开发应用       
NIO(NoneBlocking IO)非阻塞IO，代表IO多路复用，通过事件机制。   
```angular2html
    while true {
        events = takeEvents(fds)  // 获取事件，如果没有事件，线程就休眠
        for event in events {
            if event.isAcceptable {
                doAccept() // 新链接来了
            } elif event.isReadable {
                request = doRead() // 读消息
                if request.isComplete() {
                    doProcess()
                }
            } elif event.isWriteable {
                doWrite()  // 写消息
            }
        }
    }
```  

Netty异步编程模型建立在回调和Future之上，不同事件处理分发给不同处理器处理    
方便开发者对应用逻辑处理更加独立于网络的操作
      
Netty组件和设计     
1)Netty的架构设计和技术点      
&emsp;&ensp;技术层面，Netty是构建于Java的NIO基于异步事件驱动的框架，能够在高负载的情况保证应用的性能和可扩展性     
&emsp;&ensp;架构层面，Netty包含了很多的设计模式来使得应用程序的逻辑处理与网络层的处理解耦，在简化代码的同时，保证了代码的最大的可测试性，模块化性，和最大的可重复利用性     
2)Channel、EventLoop和ChannelFuture     
&emsp;&ensp;1）Channel-------关键字：Sockets     
&emsp;&ensp;&emsp;&ensp;interface Channel          
&emsp;&ensp;2）EventLoop-------关键字：控制流，多线程，并发     
&emsp;&ensp;&emsp;&ensp;Thread--EventLoop--Channels,所有I/O操作是异步的，操作结果不会立即返回     
&emsp;&ensp;3）ChannelFuture-------关键字：异步通知     
&emsp;&ensp;&emsp;&ensp;Netty提供了ChannelFuture，它的addListener()方法注册一个channelFutureListener来通知操作是否被完成了     
3)ChannelHandler和ChannelPipeline     
&emsp;&ensp;ChannelHandler作为服务容器来处理输入输出数据的业务逻辑，ChannelIn/OutboundHandler可以用来实现接收和发出数据并按照业务逻辑处理数据     
&emsp;&ensp;ChannelPipeline提供了ChannelHandler链的容器，定义了这个链中数据的输入输出传播方式的API，ChannelHandler被装载到ChannelPipeline的规则：     
&emsp;&ensp;&emsp;&ensp;1）一个ChannelInitializer被注册到ServerBootStraping上     
&emsp;&ensp;&emsp;&ensp;2）当ChannelInitializer的initChannel方法被调用的时候，ChannelInitializer会装载自定义的一些ChannelHandler到管道上     
&emsp;&ensp;&emsp;&ensp;3）ChannelInitializer将它自己从ChannelPipeline上移除     
&emsp;&ensp;Encoders and Decoders         
4)Bootstrap     
&emsp;&ensp;server端监听连接，ServerBootstrap绑定连接,使用两个EventLoopGroup     
&emsp;&ensp;&emsp;&ensp;---与ServerChannel相关的EventLoopGroup会分配一个EventLoop,这个EventLoop负责创建channel来处理新连接的连接请求，连接建立成功，第二个EventLoopGroup会为每一个新创建的channel分配一个对象的EventLoop     
&emsp;&ensp;client端建立连接，Bootstrap连接远程主机，一个EventLoopGroup     


ChannelHandler,ChannelHandlerContext,ChannelPipeline:
    一个ChannelPipeline可以有多个ChannelHandle实例，ctx是handler和pipe之间的桥梁
        
















