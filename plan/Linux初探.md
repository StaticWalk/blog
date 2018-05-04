视频全长6小时&emsp;&ensp; https://www.imooc.com/learn/175   
 * Linux简介   
1.Linux就是一个内核(内核版本、发行版本)，CentOS或Ubuntu只是不同的实现。类似Java中的interface接口，两种操作系统根据自己的需求来实现内核。    
2.Linux字符界面相对图形化界面有点：更适合服务器，安全稳定出错可能性小，占用系统资源少     
3.Linux中一切皆是对文件的操作，不依靠扩展名来区分文件类型，但是会有约定俗称的文件后缀    
    
 * 磁盘分区和格式化    
1.磁盘分区(/dev):最多4个主分区，扩展分区(最多一个，主分区加扩展分区最多四个，包含逻辑分区)。最小单位是4KB的Block内存块     
2.格式化定义(又称逻辑格式化)：重新划分内存区，方便重新写入系统文件(给人直观体验就是清空硬盘)    
    
    
   ![icon](https://github.com/StaticWalk/blog/blob/master/images/5-4-2.png?raw=true)
 * 命令基本格式   
 -a = -all  
 -l = 详细内容   
 -d = 目录属性   
 -h = 文件大小   
 -i = 显示文件存储节点     
``` 
    [root@localhost ~]#
```    
从左到右: 当前登陆用户(root、username) + @ + 主机名(localhost) + 当前所在目录(~ 、/root 、/tmp) + 用户身份($普通用户、#超级用户)    

   



   
   
[//]:这是注释
