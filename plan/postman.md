form-data\multipart
表单提交，可以上传文件也可以是键值对，最后会组装为一条信息
当上传的字段是文件时，会Content-Type来表名文件类型，content-disposition，用来说明字段的一些信息

x-www-form-urlencoded
会将表单内的数据转换为键值对，比如,name=java&age = 23

raw 
支持任何格式的文本 text json xml html 

binary
只能上传二进制数据，通常用来上传文件，无键值一次只能上传一个文件

form-data 文件、键值对、最后是一条信息
urlencoded 只能键值对，上传的时候会被分开 & &