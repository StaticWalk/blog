[http://wiki.jikexueyuan.com/project/spring-security/]
大部分 Spring Security 常用的功能：
* Web/Http安全：实现filter和相关的service bean来实现框架的认证机制。受保护的url将用户导入认证界面或错误界面
* 业务对象和方法的安全：控制方法的访问权限
* AuthenticationManager（默认实现ProviderManager.class，维护一个AuthenticationProvider列表处理请求）：处理来自框架其他部分的认证请求接口，一个接口方法authenticate 
* AuthenticationProvider（AuthenticationManager通过它来认证用户的）：
    默认使用DaoAuthenticationProvider.class
        认证的时候需要使用UserDetailsService来获取用户的信息UserDetails（一般需要自己实现这个类，增添一些自定义信息 uuas中的AuthenticationUser）
    改变认证方式，实现自己的AuthenticationProvider   
    改变用户信息的来源，可以实现 UserDetailsService  jdbcDaoImpl、InMemoryUserDetailsManager、、、
* UserDetailsService：跟 AuthenticationProvider 关系密切，用来获取用户信息的
* AccessDecisionManager：为 Web 或方法的安全提供访问决策。会注册一个默认的，但是我们也可以通过普通 bean 注册的方式使用自定义的 AccessDecisionManager
* 
