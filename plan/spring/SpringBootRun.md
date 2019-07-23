SpringBoot将Spring应用的启动流程进行了一个“模板化”操作
SpringApplication.run(XXX.class,args)进行一站式启动

* 开始
收集各种条件和回调接口，ApplicationContextInitializer、ApplicationListener
* 通过started()
创建并准备Environment
* 通告environmentPrepared
创建并初始化ApplicationContext,设置Environment,加载配置等
* 通告contextPrepared() 通过contextLoader()
调用ApplicationContext的refresh()方法，完成最终程序启动
* 执行ApplicationRunner和CommandLineRunner,通告finished()结束

