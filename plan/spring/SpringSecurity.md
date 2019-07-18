[http://wiki.jikexueyuan.com/project/spring-security/]
大部分 Spring Security 常用的功能：
* Web/Http安全：实现filter和相关的service bean来实现框架的认证机制。受保护的url将用户导入认证界面或错误界面
* 业务对象和方法的安全：控制方法的访问权限
* AuthenticationManager（默认实现ProviderManager.class，维护一个AuthenticationProvider列表处理请求）：处理来自框架其他部分的认证请求接口，一个接口方法authenticate 
* AuthenticationProvider（AuthenticationManager通过它来认证用户的）：
    默认使用DaoAuthenticationProvider.class
        认证的时候需要使用UserDetailsService来获取用户的信息UserDetails（一般需要自己实现这个类，增添一些自定义信息 uuas中的AuthenticationUser）
    改变认证方式，实现自己的AuthenticationProvider   
    改变获取用户信息的来源，可以实现 UserDetailsService  jdbcDaoImpl、InMemoryUserDetailsManager、、、
* UserDetailsService：跟 AuthenticationProvider 关系密切，用来获取用户信息的 
* AccessDecisionManager：为 Web 或方法的安全提供访问决策。会注册一个默认的，但是我们也可以通过普通 bean 注册的方式使用自定义的 AccessDecisionManager 

* SecurityContextHolder：用来保存SecurityContext   SecurityContextHolderStrategy三种策略：全局、threadLocal、子线程使用父线程变量
    threadLocal用于每个线程需要自己的独立的实例
* SecurityContext：包含当前访问用户的详细信息，通过UserDetailsService获取
默认strategy下，SecurityContextHolder 将使用 ThreadLocal 来保存 SecurityContext，这也就意味着在处于同一线程中的方法中我们可以从 ThreadLocal 中获
取到当前的 SecurityContext。因为线程池的原因，如果我们每次在请求完成后都将 ThreadLocal 进行清除的话，那么我们把 SecurityContext 存放在 
ThreadLocal 中还是比较安全的。这些工作 Spring Security 已经自动为我们做了，即在每一次 request 结束后都将清除当前线程的 ThreadLocal。
* Authentication对象：在系统交互中，SpringSecurity会为我们创建相应的Authentication对象，然后赋值给当前的SecurityContext对象
