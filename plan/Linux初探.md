视频全长6小时&emsp;&ensp; https://www.imooc.com/learn/175   
 * Linux简介   
1.Linux就是一个内核(内核版本、发行版本)，CentOS或Ubuntu只是不同的实现。类似Java中的interface接口，两种操作系统根据自己的需求来实现内核。    
2.Linux字符界面相对图形化界面有点：更适合服务器，安全稳定出错可能性小，占用系统资源少     
3.Linux中一切皆是对文件的操作，不依靠扩展名来区分文件类型，但是会有约定俗称的文件后缀
4.Linux中文件的索引通过每个文件内存中唯一的i节点号实现       
    
 * 磁盘分区和格式化    
1.磁盘分区(/dev):最多4个主分区，扩展分区(最多一个，主分区加扩展分区最多四个，包含逻辑分区)。最小单位是4KB的Block内存块     
2.格式化定义(又称逻辑格式化)：重新划分内存区，方便重新写入系统文件(给人直观体验就是清空硬盘)    
    
    
 ![icon](https://github.com/StaticWalk/blog/blob/master/images/5-4-2.png?raw=true)
 * 命令基本格式   
 -a = -all可查看隐藏文件  
 -l = 详细内容   
 -d = 目录属性   
 -h = 文件大小   
 -i = 显示文件存储节点     
``` 
    [root@localhost ~]#
```    
从左到右: 当前登陆用户(root、username) + @ + 主机名(localhost) + 当前所在目录(~ 、/root 、/tmp) + 用户身份($普通用户、#超级用户)    

``` 
   -rwxr-xr-x. 1 root root    76 5月   4 05:10 hello.sh
```    
文件权限解释(左到右)：1文件类型(七种,- 文件、l 链接文件、d 目录 ....) + 2-4所有者权限(read、write、execute) + 5-7所属组权限 + 8-10其他人权限    
     
 * 常见命令(除了同级目录，所有文件操作使用绝对地址)     
 1.mkdir -p(文件递归创建) [目录名]   
 2.cd -(返回上次目录)  ~(返回home家目录)    
 3.../ 返回上级目录    
 4.rmdir 删除空白目录 ; rm -rf [目录名] -r(删除目录) -f(force强制删除)   
 5.cp [SourceFile] [NewFile] &emsp;&ensp; -r(目录)  -p(加上文件属性) -d(如果是链接属性，复制链接属性) -a(=-pdr)  
 6.mv [SourceFile] [NewFile] &emsp;&ensp;常用来做文件改名、文件剪切    
 7.ln -s [SourceFile] [NewFile] 软链接.soft类似windows快捷方式(用一个block文件来存储原文件名称+I节点号)，硬链接.hard类似新建文件(硬链接具有自己的I节点、时间、存储空间，不能跨分区)    
 8.搜索文件(条件逻辑符-a and、-o or,复合命令执行 command1 -exec command2 {}  \;)：   
 &emsp;&ensp;locate(locate搜索文件名，反应快，查找内容在后台数据库/var/lib/mlocate ,updatedb强制更新数据库): locate [FileName]    
 &emsp;&ensp;whereis/which/whatis/whoami(查看指令，不能找文件)  -b只查找可执行文件  -m查找帮助文件          
 &emsp;&ensp;find(完全匹配，执行会遍历OS，-iname不区分大小写,condition包含 -mtime修改时间、-atime访问时间 、ctime属性改变时间 后缀+ - day或者-size后缀k M)find [area] [condition + limit]   
 &emsp;&ensp;grep(查找文件中的字符串,-v取不包含字符串，-i忽略大小写，包含匹配可正则：* 任意内容、? 一个字符、[]一个中括号内字符) &emsp;&ensp;grep "xxx"  [File]   
 &emsp;&ensp;man -f command查看帮助命令；apropos command = man -k command 查找类似关键字        
 9.压缩命令(.zip .gz .bz2 ; .tar.gz .tar.bz2 )  
  &emsp;&ensp;1).zip [FileName] [SourceName] ,应写明目标文件的后缀名；unzip来解压.zip文件    
  &emsp;&ensp;2).gzip [SourceFile] 解压后源文件会消失，-r压缩目录(目录下所有子文件会被压缩)，保留源文件方式 gzip -c [SourceFile] > [FileName] &emsp;&ensp;解压gzip -d [FileName] | gunzip [FileName]   
  &emsp;&ensp;3).bzip2 [SourceFile] 不会保留源文件，-k会保留原文件，不能压缩目录 &emsp;&ensp;大致同gzip，-k保留源文件     
  &emsp;&ensp;4).tar -cvf [FileName] [SourceName] -c打包，-v显示过程，-f指定打包后文件名，-x解压  .tar.gz(.zcvf压缩 .zxvf解压) .tar.gz(.jcvf压缩 .jxvf解压)  
        
  * Shell脚本   
  ```
#!/bin/bash

#this is a program
echo -e "\e[1;34m hello,xiongxiaoyu \e[0m"
```
  1.所有.sh文件开头是 #!/bin/bash
  2.启动方式：
 &emsp;&ensp;1)chomd 755 FileName.sh (chmod + 三位权限，读4、写2、执行1 )，给.sh文件赋予执行权限然后通过 ./FileName.sh执行    
 &emsp;&ensp;2)bash FileName.sh  通过Bash调用执行脚本   
    
 * 实用快捷方式   
 ctrl + c 强制停止命令    
 ctrl + l 清空屏幕   
 ctrl + a 将游标移动到行首   
 ctrl + e 将光标移动到行尾
 ctrl + u 删除光标以前的内容    
 ctrl + z 命令后台运行    
 ctrl + r 查找历史运行命令   
 history [option] (查看历史使用过的命令，-w刷新到历史命令保存文件~/.bash_history)
 
 
 
   
[//]:这是注释
