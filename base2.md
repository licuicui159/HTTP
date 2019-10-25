IO网络编程
==========================

-----------

[TOC]

## Linux 操作系统及其组成

1. 操作系统的作用

操作系统（OS）是管理计算机硬件与软件资源的计算机程序，同时也是计算机系统的内核与基石。操作系统需要处理如管理与配置内存、决定系统资源供需的优先次序、控制输入设备与输出设备、操作网络与管理文件系统等基本事务。操作系统也提供一个让用户与系统交互的操作界面。

2. Linux操作系统组成

 一个典型的Linux操作系统组成为：Linux内核，文件系统，命令行shell，图形界面和桌面环境，并包各种工具和应用软件。

 * Linux内核: Linux操作系统的核心代码
  
 * 文件系统：通常指称管理磁盘数据的系统，可将数据以目录或文件的型式存储。每个文件系统都有自己的特殊格式与功能

 * shell命令： 接收用户命令，然后调用相应的应用程序，并根据用户输入的指令来反馈给用户指定的信息。

![Linux](img/linux.jpg)

## shell命令

### 文件操作命令

* linux下的目录结构

![Linux](img/linux_fs.jpg)

| 作用 | 命令 |
| --- | --- |
| 切换工作目录 | cd |
| 查看文件 | ls  ，  ls -l ，  ls -a |
| 复制文件 | cp  -r |
| 移动文件 | mv |
| 删除文件 | rm  -rf  ， rmdir |
| 创建文件夹| mkdir -p |
| 创建文件| touch |
| 查看文件内容| cat |


## IO 

1. 定义

>在内存中存在数据交换的操作认为是IO操作,比如和终端交互 ,和磁盘交互，和网络交互等

2. 程序分类

>* IO密集型程序：在程序执行中有大量IO操作，而cpu运算较少。消耗cpu较少，耗时长。

>* 计算密集型程序：程序运行中计算较多，IO操作相对较少。cpu消耗多，执行速度快，几乎没有阻塞。

## 文件

文件是保存在持久化存储设备(硬盘、U盘、光盘..)上的一段数据。从格式编码角度分为文本文件（打开后会自动解码为字符）、二进制文件(视频、音频等)。在Python里把文件视作一种类型的对象，类似之前学习过的其它类型。

### 字节串（bytes）

在python3中引入了字节串的概念，与str不同，字节串以字节序列值表达数据，更方便用来处理二进程数据。因此在python3中字节串是常见的二进制数据展现方式。

* 普通的ascii编码字符串可以在前面加b转换为字节串，例如：b'hello'
* 字符串转换为字节串方法 ：str.encode()
* 字节串转换为字符串方法 : bytes.decode() 


### 文件读写

对文件实现读写的基本操作步骤为：打开文件，读写文件，关闭文件

***代码实现：  day4/file_open.py***

```
"""
file_open.py
文件打开方式训练
"""

# 打开文件
try:
    """
    文本文件既可以使用文本方式打开,也能使用二进进制方式打开
    二进制文件如果使用文本方式打开,读写时会报错
    """
    # f = open('text.py','r') # 只读方式
    # f = open('text.py','w') # 只写方式
    f = open('text.py','a') # 追加方式
except Exception as e:
    print(e)

# 读写文件

# 关闭文件
f.close()
```

***代码实现：  day4/file_read.py***

```
"""
file_read.py
文件读取演示
"""

# 打开文件
f = open('1.jpg','rb')

# 读操作

while True:
    # 到文件结尾时会读出空字串
    data = f.read(16)
    # 到文件结尾跳出循环
    if not data:
        break
    print("读取到的数据:",data)

# 每次读取一行内容
# data = f.readline(6)
# print("一行内容:",data)
# data = f.readline()
# print("一行内容:",data)

# 将内容读取到一个列表
# 参数表达的是读取到该字符数所在的行
# data = f.readlines(28)
# print(data)

# 文件对象可迭代,每次一行
# for line in f:
#     print(line)


# 关闭
f.close()
```

***代码实现：  day4/file_write.py***

```
"""
file_write.py
文件写操作演示
"""

f = open('text','w')
# f = open('text','ab')

# 写操作
# f.write(b"hello,diegui\n") # 如果希望换行则自己添加
# f.write("哎呀,干啥".encode())

# 写入列表内容
l = ['hello world\n','哈哈哈\n']
f.writelines(l)


f.close()
```

### 文件拷贝

```
"""
编写一个文件拷贝程序,将一个文件拷贝一份,重新取另外一个名字(自定).
      文件可能是文本,也可能是二进制
"""

filename = input("文件:")

fr = open(filename,'rb')
fw = open("备份-"+filename,'wb')

while True:
    # 循环读取
    data = fr.read(1024)
    if not data:  # 文件结束
        break
    fw.write(data)

fr.close()
fw.close()
```



1. 打开文件

```python
file_object = open(file_name, access_mode='r', buffering=-1)
功能：打开一个文件，返回一个文件对象。
参数：file_name  文件名；
     access_mode  打开文件的方式,如果不写默认为‘r’ 
          文件模式                        操作
              r                    以读方式打开 文件必须存在
              w                    以写方式打开
                                   文件不存在则创建，存在清空原有内容 
              a                    以追加模式打开 
              r+                   以读写模式打开 文件必须存在
              w+                   以读写模式打开文件
                                   不存在则创建，存在清空原有内容
              a+                   以读写模式打开 追加模式
              rb                   以二进制读模式打开 同r
              wb                   以二进制写模式打开 同w
              ab                   以二进制追加模式打开 同a
              rb+                  以二进制读写模式打开 同r+
              wb+                  以二进制读写模式打开 同w+
              ab+                  以二进制读写模式打开 同a+
     buffering  1表示有行缓冲，默认则表示使用系统默认提供的缓冲机制。
返回值：成功返回文件操作对象。
```


1. 读取文件

>read([size])
>功能： 来直接读取文件中字符。
>参数： 如果没有给定size参数（默认值为-1）或者size值为负，文件将被读取直至末尾，给定size最多读取给定数目个字符（字节）。
>返回值： 返回读取到的内容
>
>* 注意：文件过大时候不建议直接读取到文件结尾，读到文件结尾会返回空字符串。

>readline([size])
>功能： 用来读取文件中一行
>参数： 如果没有给定size参数（默认值为-1）或者size值为负，表示读取一行，给定size表示最多读取制定的字符（字节）。
>返回值： 返回读取到的内容

>readlines([sizeint])
>功能： 读取文件中的每一行作为列表中的一项
>参数： 如果没有给定size参数（默认值为-1）或者size值为负，文件将被读取直至末尾，给定size表示读取到size字符所在行为止。
>返回值： 返回读取到的内容列表


>文件对象本身也是一个可迭代对象，在for循环中可以迭代文件的每一行。
```python
for line in f:
     print(line)
```

3. 写入文件

>write(string)
>功能: 把文本数据或二进制数据块的字符串写入到文件中去
>参数：要写入的内容
>返回值：写入的字符个数
>
>* 如果需要换行要自己在写入内容中添加\n

>writelines(str_list)
>功能：接受一个字符串列表作为参数，将它们写入文件。
>参数: 要写入的内容列表

4. 关闭文件

打开一个文件后我们就可以通过文件对象对文件进行操作了，当操作结束后使用close（）关闭这个对象可以防止一些误操作，也可以节省资源。

>file_object.close()

5. with操作

python中的with语句使用于对资源进行访问的场合，保证不管处理过程中是否发生错误或者异常都会执行规定的“清理”操作，释放被访问的资源，比如有文件读写后自动关闭、线程中锁的自动获取和释放等。

with语句的语法格式如下：

```python
with context_expression [as obj]:
    with-body
```

通过with方法可以不用close(),因为with生成的对象在语句块结束后会自动处理，所以也就不需要close了，但是这个文件对象只能在with语句块内使用。

```python
with open('file','r+') as f:
    f.read()
```

>注意
>> 1. 加b的打开方式读写要求必须都是字节串
>> 2. 无论什么文件都可以使用二进制方式打开，但是二进制文件使用文本方式打开读写会出错

### 其他操作

#### 刷新缓冲区

缓冲:系统自动的在内存中为每一个正在使用的文件开辟一个缓冲区，从内存向磁盘输出数据必须先送到内存缓冲区，再由缓冲区送到磁盘中去。从磁盘中读数据，则一次从磁盘文件将一批数据读入到内存缓冲区中，然后再从缓冲区将数据送到程序的数据区。

刷新缓冲区条件：

1. 缓冲区被写满
2. 程序执行结束或者文件对象被关闭
3. 行缓冲遇到换行
4. 程序中调用flush()函数

***代码实现：  day4/buffer.py***

```
"""
buffer.py
缓冲区演示
"""

# f = open('test','w',1) # 行缓冲
f = open('test','w')

while True:
    data = input(">>")
    if not data:
        break
    f.write(data + '\n')
    f.flush()  # 主动刷新缓冲

f.close()
```



>flush()
该函数调用后会进行一次磁盘交互，将缓冲区中的内容写入到磁盘。

#### 文件偏移量

***代码实现：  day4/seek.py***

```
"""
seek.py  文件偏移量

注意: 1. open打开文件会重置文件偏移量
     2. 读写操作使用的是一个偏移量值
     3. seek操作文件偏移量一般是以二进制打开
"""

f = open("test",'wb+')

f.write(b"Hello world")
# f.close()
#
# f = open('test','r')

print("偏移量:",f.tell()) # 获取文件偏移量

f.seek(-5,2)  # 将文件偏移量定位到开头

data = f.read()
print(data)

f.close()
```



1. 定义
>打开一个文件进行操作时系统会自动生成一个记录，记录中描述了我们对文件的一系列操作。其中包括每次操作到的文件位置。文件的读写操作都是从这个位置开始进行的。

2. 基本操作
   
>tell()
功能：获取文件偏移量大小

>seek(offset[,whence])
>功能:移动文件偏移量位置
>参数：offset  代表相对于某个位置移动的字节数。负数表示向前移动，正数表示向后移动。
>     whence是基准位置的默认值为 0，代表从文件开头算起，1代表从当前位置算起，2 代表从文件末尾算起。
>
>* 必须以二进制方式打开文件时基准位置才能是1或者2

#### 文件描述符

1. 定义
>系统中每一个IO操作都会分配一个整数作为编号，该整数即这个IO操作的文件描述符。

2. 获取文件描述符
   
>fileno()
通过IO对象获取对应的文件描述符


### 文件管理函数

1. 获取文件大小  
>os.path.getsize(file)

2. 查看文件列表  
>os.listdir(dir)

3. 查看文件是否存在
>os.path.exists(file)

4. 判断文件类型
>os.path.isfile(file)

5. 删除文件
>os.remove(file)


## 网络编程基础

计算机网络功能主要包括实现资源共享，实现数据信息的快速传递。
	
### OSI七层模型

>制定组织： ISO（国际标准化组织）

>作用：使网络通信工作流程标准化

>应用层 ： 提供用户服务，具体功能有应用程序实现
>表示层 ： 数据的压缩优化加密
>会话层 ： 建立用户级的连接，选择适当的传输服务
>传输层 ： 提供传输服务 
>网络层 ： 路由选择，网络互联 
>链路层 ： 进行数据交换，控制具体数据的发送
>物理层 ： 提供数据传输的硬件保证，网卡接口，传输介质

>优点 
>1. 建立了统一的工作流程
>2. 分部清晰，各司其职，每个步骤分工明确
>3. 降低了各个模块之间的耦合度，便于开发


### 四层模型（TCP/IP模型）

背景 ： 实际工作中工程师无法完全按照七层模型要求操作，逐渐演化为更符合实际情况的四层

![TCP/IP模型](img/1_tcpip模型.png)

#### 数据传输过程

1. 发送端由应用程序发送消息，逐层添加首部信息，最终在物理层发送消息包。
2. 发送的消息经过多个节点（交换机，路由器）传输，最终到达目标主机。
3. 目标主机由物理层逐层解析首部消息包，最终到应用程序呈现消息。
   

![TCP/IP模型](img/1_TCP.png)

#### 网络协议

>在网络数据传输中，都遵循的规定，包括建立什么样的数据结构，什么样的特殊标志等。


### 网络基础概念

* IP地址
>功能：确定一台主机的网络路由位置

>查看本机网络地址命令： ifconfig

>结构
>>IPv4  点分十进制表示 172.40.91.185 每部分取值范围0--255
>>IPv6  128位 扩大了地址范围


* 域名
>定义： 给网络服务器地址起的名字

>作用： 方便记忆，表达一定的含义

>ping [ip] : 测试和某个主机是否联通

* 端口号（port）
>作用：端口是网络地址的一部分，用于区分主机上不同的网络应用程序。

>特点：一个系统中的应用监听端口不能重复

>取值范围： 1 -- 65535
>>1--1023  系统应用或者大众程序监听端口
>>1024--65535 自用端口


## 传输层服务

### 面向连接的传输服务（基于TCP协议的数据传输）

1. 传输特征 ： 提供了可靠的数据传输，可靠性指数据传输过程中无丢失，无失序，无差错，无重复。
   
2. 实现手段 ： 在通信前需要建立数据连接，通信结束要正常断开连接。

> 三次握手（建立连接）
>>客户端向服务器发送消息报文请求连接
>>服务器收到请求后，回复报文确定可以连接
>>客户端收到回复，发送最终报文连接建立

![](img/1_三次握手.png)
					
>四次挥手（断开连接）
>>主动方发送报文请求断开连接
>>被动方收到请求后，立即回复，表示准备断开
>>被动方准备就绪，再次发送报文表示可以断开
>>主动方收到确定，发送最终报文完成断开

![](img/1_四次挥手.png)


3. 适用情况 ： 对数据传输准确性有明确要求，传数文件较大，需要确保可靠性的情况。比如：网页获取，文件下载，邮件收发。


### 面向无连接的传输服务（基于UDP协议的数据传输）

1. 传输特点 ： 不保证传输的可靠性，传输过程没有连接和断开，数据收发自由随意。

2. 适用情况 ： 网络较差，对传输可靠性要求不高。比如：网络视频，群聊，广播


***面试要求***
* OSI七层模型介绍一下，tcp/ip模型是什么？
* tcp服务和udp服务有什么区别？
* 三次握手和四次挥手指什么，过程是怎样的？


## socket套接字编程

### 套接字介绍

1. 套接字 ： 实现网络编程进行数据传输的一种技术手段

2. Python实现套接字编程：import  socket

3. 套接字分类
>流式套接字(SOCK_STREAM): 以字节流方式传输数据，实现tcp网络传输方案。(面向连接--tcp协议--可靠的--流式套接字)

>数据报套接字(SOCK_DGRAM):以数据报形式传输数据，实现udp网络传输方案。(无连接--udp协议--不可靠--数据报套接字)


### tcp套接字编程

#### 服务端流程

![](img/1_TCP_Server.png)
***代码实现：day5/tcp_server.py***

```
"""
tcp_server.py  tcp套接字服务端流程
重点代码

注意: 功能性代码,注重流程和函数使用
"""

import socket

# 创建tcp套接字对象
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',9999))

# 设置监听
sockfd.listen(5)

# 等待处理客户端连接请求
print("Waiting for connect...")
connfd,addr = sockfd.accept()
print("Connect from",addr)

# 消息收发
data = connfd.recv(1024)
print("Receive:",data.decode())
n = connfd.send(b"Thanks")
print('Send %d bytes'%n)

# 关闭套接字
connfd.close()
sockfd.close()

```



1. 创建套接字

```python
sockfd=socket.socket(socket_family=AF_INET,socket_type=SOCK_STREAM,proto=0)
功能：创建套接字
参数：  socket_family  网络地址类型 AF_INET表示ipv4
	socket_type  套接字类型 SOCK_STREAM(流式)  SOCK_DGRAM(数据报)
	proto  通常为0  选择子协议
返回值： 套接字对象
```
2. 绑定地址

>本地地址 ： 'localhost' , '127.0.0.1'
>网络地址 ： '172.40.91.185'
>自动获取地址： '0.0.0.0'

![](img/address.png)

```python
sockfd.bind(addr)
功能： 绑定本机网络地址
参数： 二元元组 (ip,port)  ('0.0.0.0',8888)
```

3. 设置监听

```python
sockfd.listen(n)
功能 ： 将套接字设置为监听套接字，确定监听队列大小
参数 ： 监听队列大小
```
4. 等待处理客户端连接请求

```python
connfd,addr = sockfd.accept()
功能： 阻塞等待处理客户端请求
返回值： connfd  客户端连接套接字
         addr  连接的客户端地址
```
5. 消息收发

```python
data = connfd.recv(buffersize)
功能 : 接受客户端消息
参数 ：每次最多接收消息的大小
返回值： 接收到的内容

n = connfd.send(data)
功能 : 发送消息
参数 ：要发送的内容  bytes格式
返回值： 发送的字节数
```

6. 关闭套接字

```python
sockfd.close()
功能：关闭套接字
```

#### 客户端流程

***代码实现：day5/tcp_client.py***

```
"""
tcp_client.py  tcp套接字客户端流程
重点代码

注意: 和服务端配合,使用同样的套接字
"""

from socket import *

# 创建tcp套接字
sockfd = socket() # 默认值

# 连接服务器
server_addr = ('127.0.0.1',9999) # 服务器地址
sockfd.connect(server_addr)

# 先发后收
msg = input("Msg:")
sockfd.send(msg.encode()) #字节串
data = sockfd.recv(1024)
print("From server:",data.decode())

sockfd.close()


```

![](img/1_TCP_Client.png)
		  
1. 创建套接字
>注意:只有相同类型的套接字才能进行通信

2. 请求连接

```python
sockfd.connect(server_addr)
功能：连接服务器
参数：元组  服务器地址
```

3. 收发消息
>注意： 防止两端都阻塞，recv send要配合

4. 关闭套接字


#### tcp 套接字数据传输特点

>* tcp连接中当一端退出，另一端如果阻塞在recv，此时recv会立即返回一个空字串。

>* tcp连接中如果一端已经不存在，仍然试图通过send发送则会产生BrokenPipeError

>* 一个监听套接字可以同时连接多个客户端，也能够重复被连接

#### 网络收发缓冲区

1. 网络缓冲区有效的协调了消息的收发速度
2. send和recv实际是向缓冲区发送接收消息，当缓冲区不为空recv就不会阻塞。
	
#### tcp粘包

>原因：tcp以字节流方式传输，没有消息边界。多次发送的消息被一次接收，此时就会形成粘包。

>影响：如果每次发送内容是一个独立的含义，需要接收端独立解析此时粘包会有影响。

>处理方法
>>1. 人为的添加消息边界
>>2. 控制发送速度


### UDP套接字编程

#### 服务端流程

![](img/2_UDP_Server.png)

***代码实现：day6/udp_server.py***

```
"""
udp_server.py  udp套接字服务端流程
重点代码
"""

from socket import *

# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1',8888)
sockfd.bind(server_addr)

# 循环收发消息
while True:
    data,addr = sockfd.recvfrom(1024)
    print("Msg from %s: %s"%(addr,data.decode()))
    sockfd.sendto(b'Thanks',addr)

# 关闭套接字
sockfd.close()
```

​	  

1. 创建数据报套接字
```python
sockfd = socket(AF_INET,SOCK_DGRAM)
```
2. 绑定地址

```python
sockfd.bind(addr)
```

3. 消息收发

```python		    
data,addr = sockfd.recvfrom(buffersize)
功能： 接收UDP消息
参数： 每次最多接收多少字节
返回值： data  接收到的内容
	addr  消息发送方地址

n = sockfd.sendto(data,addr)
功能： 发送UDP消息
参数： data  发送的内容 bytes格式
	addr  目标地址
返回值：发送的字节数
```

4. 关闭套接字
```python
sockfd.close()
```
#### 客户端流程

![](img/2_UDP_Client.png)

***代码实现：day6/udp_client.py***

```
"""
udp_client.py udp客户端
重点代码
"""

from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环收发消息
while True:
    data = input("Msg>>")
    if not data: # 退出
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("From server:",msg.decode())

sockfd.close()
```



1. 创建套接字

2. 收发消息

3. 关闭套接字

#### tcp/udp区别

---------------
>
>>1. 流式套接字是以字节流方式传输数据，数据报套接字以数据报形式传输
>>2. tcp套接字会有粘包，udp套接字有消息边界不会粘包
>>3. tcp套接字保证消息的完整性，udp套接字则不能
>>4. tcp套接字依赖listen accept建立连接才能收发消息，udp套接字则不需要
>>5. tcp套接字使用send，recv收发消息，udp套接字使用sendto，recvfrom
---------------------

### socket套接字属性

***代码实现：day6/sock_attr.py***

【1】 sockfd.type  套接字类型

【2】 sockfd.family 套接字地址类型

【3】 sockfd.getsockname() 获取套接字绑定地址

【4】 sockfd.fileno() 获取套接字的文件描述符

【5】 sockfd.getpeername() 获取连接套接字客户端地址

【6】 sockfd.setsockopt(level,option,value)
		功能：设置套接字选项
		参数： level  选项类别   SOL_SOCKET
			option 具体选项内容
			value  选项值



![](img/2_setsockopt.png)



## struct模块进行数据打包

***代码实现：day6/struct_recv.py***

```
"""
 udp完成 ,从客户端输入学生信息,循环录入

          学号:
          姓名: 不会超过16字节
          年龄:
          分数: 保留一位小数

          将信息发送给服务端,在服务端写入到一个文件里,
          每个学生信息占一行
"""

from socket import *
import struct

# 与客户端格式一直
st = struct.Struct("i16sif")

#udp套接字
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('127.0.0.1',8888))

# 打开一个保存信息的文件
f = open('student.txt','a')

while True:
    data,addr = s.recvfrom(1024)
    # (1,b'Lily',14,94.5)
    data = st.unpack(data)

    # 写入文件
    info = "%d  %-10s  %d  %.1f\n"%data
    f.write(info)
    f.flush()

f.close()
s.close()

```

***代码实现：day6/struct_send.py***

```
import struct
from socket import *

# 设置数据结构
st = struct.Struct("i16sif")

# 创建udp套接字
s = socket(AF_INET,SOCK_DGRAM)
ADDR = ('127.0.0.1',8888)

while True:
    print("===========================")
    id = int(input("学号:"))
    name = input("姓名:").encode()
    age = int(input("年龄:"))
    score = float(input("得分:"))
    # 将数据打包
    data = st.pack(id,name,age,score)
    s.sendto(data,ADDR) # 发送给服务端

s.close()



```



1. 原理： 将一组简单数据进行打包，转换为bytes格式发送。或者将一组bytes格式数据，进行解析。
2. 接口使用

```python
Struct(fmt)
功能: 生成结构化对象
参数：fmt  定制的数据结构

st.pack(v1,v2,v3....)
功能: 将一组数据按照指定格式打包转换为bytes
参数：要打包的数据
返回值： bytes字节串

st.unpack(bytes_data)
功能： 将bytes字节串按照指定的格式解析
参数： 要解析的字节串
返回值： 解析后的内容

struct.pack(fmt,v1,v2,v3...)
struct.unpack(fmt,bytes_data)
```

> 说明： 可以使用struct模块直接调用pack unpack。此时这两函数第一个参数传入fmt。其他用法功能相同

![](C:/Users/lvze/Desktop/%E8%AF%BE%E7%A8%8B%E4%B8%8B%E5%8F%91/IO%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B/img/4_struct.png)



### HTTP传输

#### HTTP协议 （超文本传输协议）

1. 用途 ： 网页获取，数据的传输

2. 特点
>* 应用层协议，传输层使用tcp传输
>* 简单，灵活，很多语言都有HTTP专门接口
>* 无状态，协议不记录传输内容
>* http1.1 支持持久连接，丰富了请求类型

3. 网页请求过程

>1.客户端（浏览器）通过tcp传输，发送http请求给服务端
>2.服务端接收到http请求后进行解析
>3.服务端处理请求内容，组织响应内容
>4.服务端将响应内容以http响应格式发送给浏览器
>5.浏览器接收到响应内容，解析展示

![](img/2_网站访问.png)
    
#### HTTP请求（request）

***代码实现：day6/http_test.py***

```
"""
http请求响应演示
"""

from socket import *

# tcp服务端
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # 端口立即重用
s.bind(('127.0.0.1',8000))
s.listen(5)

c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096).decode()
print(data)  # http请求

html = """HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello World</h1>
"""
c.send(html.encode())

c.close()
s.close()
```

***代码实现：day7/http_server.py***

```
"""
编写一个http服务端程序
     如果浏览器的请求内容 /
     响应码为  200  OK,将index.html内容作为响应内容

     如果浏览器的请求是其他的
     响应码为  404  Not Found  内容为 "Sorry.."
"""
from socket import *

# 与客户端交互
def handle(connfd):
    # 获取http请求
    data = connfd.recv(4096).decode()
    request_line = data.split('\n')[0] # 请求行
    info = request_line.split(' ')[1] # 请求内容
    # 看一下请求内容是不是/
    if info == '/':
        with open('index.html') as f:
            # 组织http响应
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += '\r\n'
            response += f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += '\r\n'
        response += "<h1>Sorry...</h1>"
    # 发送给浏览器
    connfd.send(response.encode())

# 搭建网络
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8000))
    sockfd.listen(3)
    while True:
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
        # 处理客户端请求
        handle(connfd)

main()
```

#### **查单词代码**

使用udp完成,在客户端循环的输入单词,得到单词解释.知道摁回车退出查询. 可以满足同时启动多个客户端一起查询

***udp_word_server.py***

```
"""
使用udp完成,在客户端循环的输入单词,得到单词解释.知道摁回车退出查询. 可以满足同时启动多个客户端一起查询
"""


from socket import *

# 查找单词
def find_word(word):
    # 打开文件
    f = open('dict.txt')

    for line in f:
        w = line.split(' ')[0]
        # 遍历的单词已经大于目标,说明找不到了
        if w > word:
            break
        elif w == word:
            f.close()
            return line
    f.close()
    return "没有找到该单词"



# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1',8888)
sockfd.bind(server_addr)

# 循环收发消息
while True:
    word,addr = sockfd.recvfrom(1024)
    # 得到单词解释
    data = find_word(word.decode())

    sockfd.sendto(data.encode(),addr)

# 关闭套接字
sockfd.close()
```

***udp_word_client.py***

```
"""
udp_client.py udp客户端
重点代码
"""

from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环收发消息
while True:
    data = input("Word>>")
    if not data: # 退出
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print(msg.decode())

sockfd.close()
```

#### 写日志代码

```
"""
运行程序时,写一个日志文件,格式如下

 1. Fri Aug 30 17:57:45 2019
 2. Fri Aug 30 17:57:46 2019
 3. Fri Aug 30 17:57:47 2019
 4. Fri Aug 30 17:57:48 2019
 5. Fri Aug 30 17:57:58 2019

每隔一秒写依次,每个时间占一行
当程序终止运行,重写启动的时候,序列号能够衔接
"""

import time

f = open('log.txt','a+')


f.seek(0) # 将文件偏移量放到最开始

n = len(f.readlines())

while True:
    n += 1
    time.sleep(1)
    s = "%d. %s\n"%(n,time.ctime())
    f.write(s)
    f.flush() # 刷新缓存

```



* 请求行 ： 具体的请求类别和请求内容

```
	GET         /        HTTP/1.1
	请求类别   请求内容     协议版本
```

请求类别：每个请求类别表示要做不同的事情 

```		
		GET : 获取网络资源
		POST ：提交一定的信息，得到反馈
		HEAD ： 只获取网络资源的响应头
		PUT ： 更新服务器资源
		DELETE ： 删除服务器资源
		CONNECT
		TRACE ： 测试
		OPTIONS ： 获取服务器性能信息
```

* 请求头：对请求的进一步解释和描述
```
Accept-Encoding: gzip
```
* 空行
* 请求体: 请求参数或者提交内容

#### http响应（response）

1. 响应格式：响应行，响应头，空行，响应体

* 响应行 ： 反馈基本的响应情况

```	    
HTTP/1.1     200       OK
版本信息    响应码   附加信息
```

响应码 ： 
```
1xx  提示信息，表示请求被接收
2xx  响应成功
3xx  响应需要进一步操作，重定向
4xx  客户端错误
5xx  服务器错误
```
* 响应头：对响应内容的描述
```		    
Content-Type: text/html
```

* 响应体：响应的主体内容信息



并发编程
==========================

## 多任务编程

1. 意义： 充分利用计算机CPU的多核资源，同时处理多个应用程序任务，以此提高程序的运行效率。

2. 实现方案 ：多进程 ， 多线程


## 进程（process）

### 进程理论基础

1. 定义 ： 程序在计算机中的一次运行。

>* 程序是一个可执行的文件，是静态的占有磁盘。
>* 进程是一个动态的过程描述，占有计算机运行资源，有一定的生命周期。


2. 系统中如何产生一个进程
   【1】 用户空间通过调用程序接口或者命令发起请求
   		【2】 操作系统接收用户请求，开始创建进程
   		【3】 操作系统调配计算机资源，确定进程状态等
   		【4】 操作系统将创建的进程提供给用户使用

![](/home/tarena/下载/11/并发编程/img/linux.png)
		

3. 进程基本概念

* cpu时间片：如果一个进程占有cpu内核则称这个进程在cpu时间片上。

* PCB(进程控制块)：在内存中开辟的一块空间，用于存放进程的基本信息，也用于系统查找识别进程。

* 进程ID（PID）： 系统为每个进程分配的一个大于0的整数，作为进程ID。每个进程ID不重复。

  >Linux查看进程ID ： ps -aux

* 父子进程 ： 系统中每一个进程(除了系统初始化进程)都有唯一的父进程，可以有0个或多个子进程。父子进程关系便于进程管理。

>查看进程树： pstree

* 进程状态

  - 三态  
    就绪态 ： 进程具备执行条件，等待分配cpu资源
    运行态 ： 进程占有cpu时间片正在运行
    等待态 ： 进程暂时停止运行，让出cpu

![](/home/tarena/下载/11/并发编程/img/4_3态.png)


  - 五态 (在三态基础上增加新建和终止)
    新建 ： 创建一个进程，获取资源的过程
    	终止 ： 进程结束，释放资源的过程

![](/home/tarena/下载/11/并发编程/img/4_5态.png)

  - 状态查看命令 ： ps -aux  --> STAT列

>S 等待态
>R 执行态
>Z 僵尸

>`+` 前台进程
>l   有多线程的

* 进程的运行特征
  【1】 多进程可以更充分使用计算机多核资源
  【2】 进程之间的运行互不影响，各自独立
  【3】 每个进程拥有独立的空间，各自使用自己空间资源

>面试要求
>
>>1. 什么是进程，进程和程序有什么区别
>>2. 进程有哪些状态，状态之间如何转化


## 基于fork的多进程编程

### fork使用

***代码示例：day7/fork.py***

```
"""
fork.py  fork进程演示1
"""

import os
from time import sleep

# 创建子进程
pid = os.fork()
if pid < 0:
    print("Create process failed")
elif pid == 0:
    # 子进程执行部分
    sleep(3)
    print("The new process")
else:
    # 父进程执行部分
    sleep(2)
    print("The old process")

print("Fork test over") #　父子进程都执行
```

***代码示例：day7/fork1.py***

```
"""
fork1.py  fork进程演示示例
"""

import os
from time import sleep

print("============================")
a = 1

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child process")
    print("a = ",a) # 从父进程空间获取的a
    a = 10000 # 修改自己空间的a
else:
    sleep(1)
    print("Parent process")
    print('a:',a)

print("all a = ",a) # 父子进程都执行
```



> pid = os.fork()
> 	功能： 创建新的进程
> 	返回值：整数，如果创建进程失败返回一个负数，如果成功则在原有进程中返回新进程的PID，在新进程中返回0

>注意
>
>>* 子进程会复制父进程全部内存空间，从fork下一句开始执行。
>>* 父子进程各自独立运行，运行顺序不一定。
>>* 利用父子进程fork返回值的区别，配合if结构让父子进程执行不同的内容几乎是固定搭配。
>>* 父子进程有各自特有特征比如PID PCB 命令集等。
>>* 父进程fork之前开辟的空间子进程同样拥有，父子进程对各自空间的操作不会相互影响。

### 进程相关函数

***代码示例：day7/get_pid.py***

```
"""
获取进程PID号
"""
import os
import time

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    time.sleep(1) # 子进程孤儿
    print("Child PID:",os.getpid())
    print("Get parent PID:",os.getppid())
else:
    time.sleep(30)
    print("Get child PID:",pid)
    print("Parent PID:",os.getpid())
```

***代码示例：day7/exit.py***

```
import os,sys

# os._exit(1)
sys.exit("进程退出")

print("exit test")
```



>os.getpid()
>		功能： 获取一个进程的PID值
>		返回值： 返回当前进程的PID 

>os.getppid()
>		功能： 获取父进程的PID号
>		返回值： 返回父进程PID

>os._exit(status)
>		功能: 结束一个进程
>		参数：进程的终止状态

>sys.exit([status])
>		功能：退出进程
>		参数：整数 表示退出状态
>					字符串 表示退出时打印内容

### 孤儿和僵尸

1. 孤儿进程 ： 父进程先于子进程退出，此时子进程成为孤儿进程。

>特点： 孤儿进程会被系统进程收养，此时系统进程就会成为孤儿进程新的父进程，孤儿进程退出该进程会自动处理。

```
from time import sleep
import os

def f1():
    for i in range(3):
        sleep(2)
        print("写代码")

def f2():
    for i in range(2):
        sleep(4)
        print("测代码")

pid = os.fork()
if pid == 0:  # 一级子进程
    p = os.fork()
    if p == 0:  # 二级子进程
        f1()
else:
    os.wait()
    f2()  # 父进程事件
```



2. 僵尸进程 ： 子进程先于父进程退出，父进程又没有处理子进程的退出状态，此时子进程就会称为僵尸进程。

>特点： 僵尸进程虽然结束，但是会存留部分PCB在内存中，大量的僵尸进程会浪费系统的内存资源。

```
# signal  信号方法处理僵尸进程

import os
import signal

# 信号处理僵尸
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

# 创建子进程
pid = os.fork()
if pid < 0:
    print("Create process failed")
elif pid == 0:
    # 子进程执行部分
    print("Child process:",os.getpid())
else:
    # 父进程执行部分
    print("Process process")
    while True:
        pass
```



3. 如何避免僵尸进程产生


* 使用wait函数处理子进程退出

  ***代码示例：day7/wait.py***
  
  ```
  """
  wait.py  处理僵尸进程方法
  """
  
  import os
  from time import sleep
  
  pid = os.fork()
  if pid < 0:
      print("Error")
  elif pid == 0:
      print("Child process:",os.getpid())
      sleep(2)
      os._exit(3) # 进程退出
  else:
      pid,status = os.wait() # 阻塞等待回收子进程
      print("pid:",pid)
      print("status:",os.WEXITSTATUS(status))
      while True: # 让父进程不退出
          pass
  ```
  
  

```		
pid,status = os.wait()
功能：在父进程中阻塞等待处理子进程退出
返回值： pid  退出的子进程的PID
	status  子进程退出状态

```


* 创建二级子进程处理僵尸

  ***代码示例：day7/child.py***

  ```
  
  ```
  
  【1】 父进程创建子进程，等待回收子进程
  【2】 子进程创建二级子进程然后退出
  【3】 二级子进程称为孤儿，和原来父进程一同执行事件


* 通过信号处理子进程退出
  			

>原理： 子进程退出时会发送信号给父进程，如果父进程忽略子进程信号，则系统就会自动处理子进程退出。

>方法： 使用signal模块在父进程创建子进程前写如下语句 ：

```python
import signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
```

>特点 ： 非阻塞，不会影响父进程运行。可以处理所有子进程退出


### 群聊聊天室 

>功能 ： 类似qq群功能
>【1】 有人进入聊天室需要输入姓名，姓名不能重复
>【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
>【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
>【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
>【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx

```
"""
chat room
env: python3.6
socket udp & fork exc
"""

from socket import *
import os, sys

# 全局变量：很多封装模块都要用或者有特定含义的变量
HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)

# 存储用户 {name:address}
user = {}

# 处理用户登录
def do_login(s,name,addr):
    if name in user or '管理员' in name:
        s.sendto("用户名存在".encode(),addr)
        return
    else:
        s.sendto(b'OK',addr) # 可以进入
    # 通知其他人
    msg = "\n欢迎 %s 加入群聊"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr # 加入字典

# 处理聊天
def do_chat(s,name,text):
    msg = "\n%s : %s"%(name,text)
    for i in user:
        # 不发送自己
        if i != name:
            s.sendto(msg.encode(),user[i])

# 处理退出
def do_quit(s,name):
    msg = "\n%s 退出了群聊"%name
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    del user[name] # 删除用户

# 循环获取客户端请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ',2)
        # 根据不同的请求类型，执行不同的事件
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)
        elif tmp[0] == 'C':
            do_chat(s,tmp[1],tmp[2])
        elif tmp[0] == 'Q':
            do_quit(s,tmp[1])

# 搭建网络
def main():
    # udp网络
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        # 管理员消息处理
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员 "+ msg
            s.sendto(msg.encode(),ADDR)
    else:
        do_request(s) # 接收客户端请求

if __name__ == '__main__':
    main()
```

```
"""
chat room  客户端
发送请求，展示结果
"""
from socket import *
import os,sys

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 发送消息
def send_msg(s,name):
    while True:
        try:
            text = input(">>")
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip() == 'quit':
            msg = "Q " + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

# 接收消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(4096)
        # 收到exit接收进程结束
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+'\n>>',end='')

# 搭建网络
def main():
    s = socket(AF_INET,SOCK_DGRAM)

    # 进入聊天室
    while True:
        name = input("请输入昵称:")
        msg = "L " + name
        s.sendto(msg.encode(),ADDR)
        # 接收反馈
        data,addr = s.recvfrom(128)
        if data == b'OK':
            print("您已进入聊天室")
            break
        else:
            print(data.decode())

    # 已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)

if __name__ == '__main__':
    main()
```



##  multiprocessing 模块创建进程

### 进程创建方法

***代码示例：day8/process1.py***

```
"""
multiprocessing 模块创建进程
1. 编写进程执行函数
2. 创建进程对象
3. 启动进程
4. 回收进程
"""

import multiprocessing as mp
from time import sleep

a = 1

# 进程函数
def fun():
    print("开始一个进程")
    sleep(3)
    global a
    print("a:",a)
    a = 10000
    print("进程结束")

# 创建进程对象
p = mp.Process(target = fun)
p.start() # 启动进程

sleep(2)
print("父进程也干点事")

p.join() # 回收进程

print("=======================")
print("a = ",a)


'''
p = os.fork()
if pid == 0:
    fun()
else:
    os.wait()
'''
```

***代码示例：day8/process2.py***

```
"""
同时创建多个子进程
"""

from multiprocessing import Process
from time import sleep
import os

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),'--',os.getpid())

def th2():
    # a = input()   # 不能使用标准输入
    sleep(2)
    print("睡觉")
    print(os.getppid(),'--',os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),'--',os.getpid())

things = [th1,th2,th3]
jobs = []
for th in things:
    p = Process(target = th)
    jobs.append(p) # 列表存储一下进程对象
    p.start()

for i in jobs:
    i.join()

```

***代码示例：day8/process3.py***

```
"""
进程函数传参
"""

from multiprocessing import Process
from time import *

# 带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

# p = Process(target=worker,args=(2,'Levi'))
p = Process(target=worker,args=(2,),
            kwargs={'name':'Levi'})
p.start()
p.join()


```

1.  流程特点 
    【1】 将需要子进程执行的事件封装为函数
    【2】 通过模块的Process类创建进程对象，关联函数
    【3】 可以通过进程对象设置进程信息及属性
    【4】 通过进程对象调用start启动进程
    【5】 通过进程对象调用join回收进程

2.  基本接口使用

```python
Process()
功能 ： 创建进程对象
参数 ： target 绑定要执行的目标函数 
	args 元组，用于给target函数位置传参
	kwargs 字典，给target函数键值传参
```

```python
p.start()
功能 ： 启动进程
```

>注意:启动进程此时target绑定函数开始执行，该函数作为子进程执行内容，此时进程真正被创建

```python
p.join([timeout])
功能：阻塞等待回收进程
参数：超时时间
```

>注意
>
>>* 使用multiprocessing创建进程同样是子进程复制父进程空间代码段，父子进程运行互不影响。
>>* 子进程只运行target绑定的函数部分，其余内容均是父进程执行内容。
>>* multiprocessing中父进程往往只用来创建子进程回收子进程，具体事件由子进程完成。
>>* multiprocessing创建的子进程中无法使用标准输入

3. 进程对象属性

***代码示例：day8/process_attr.py***

```
"""
进程对象属性
"""
from multiprocessing import Process
import time

def tm():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)

p = Process(target=tm,name = "Tedu")

p.daemon = True # 父进程退出子进程随之退出

p.start()
time.sleep(2)
print("Name:",p.name)
print("PID:",p.pid)  # 进程PID
print("is alive:",p.is_alive())
```



>p.name  进程名称

>p.pid   对应子进程的PID号

>p.is_alive() 查看子进程是否在生命周期

>p.daemon  设置父子进程的退出关系  
>
>>* 如果设置为True则子进程会随父进程的退出而结束
>>* 要求必须在start()前设置
>>* 如果daemon设置成True 通常就不会使用 join()

### 自定义进程类

***代码示例：day8/myProcess.py***

```
"""
自定义进程类
"""
from multiprocessing import Process

# 自定义类
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__() # 加载父类init

    def f1(self):
        print("步骤1")

    def f2(self):
        print("步骤2")

    def run(self):
        self.f1()
        self.f2()

p = MyProcess(2)
p.start() # 执行run，作为一个子进程执行
p.join()
```



1. 创建步骤
   【1】 继承Process类
   【2】 重写`__init__`方法添加自己的属性，使用super()加载父类属性
   【3】 重写run()方法

2. 使用方法
   【1】 实例化对象
   【2】 调用start自动执行run方法
   【3】 调用join回收线程


###  进程池实现

***代码示例：day8/pool.py***

```
"""
进程池使用示例
"""

from multiprocessing import Pool
from time import sleep,ctime

# 进程池执行事件
def worker(msg):
    sleep(2)
    print(ctime(),'--',msg)

# 创建进程池
pool = Pool(4)

# 添加时间
for i in range(10):
    msg = "Tedu %d"%i
    pool.apply_async(func=worker,args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
```



1.  必要性
    【1】 进程的创建和销毁过程消耗的资源较多
    【2】 当任务量众多，每个任务在很短时间内完成时，需要频繁的创建和销毁进程。此时对计算机压力较大
    【3】 进程池技术很好的解决了以上问题。

2.  原理

>创建一定数量的进程来处理事件，事件处理完进	程不退出而是继续处理其他事件，直到所有事件全都处理完毕统一销毁。增加进程的重复利用，降低资源消耗。


3. 进程池实现

【1】 创建进程池对象，放入适当的进程

```python	  
from multiprocessing import Pool

Pool(processes)
功能： 创建进程池对象
参数： 指定进程数量，默认根据系统自动判定
```

【2】 将事件加入进程池队列执行

```python
pool.apply_async(func,args,kwds)
功能: 使用进程池执行 func事件
参数： func 事件函数
      args 元组  给func按位置传参
      kwds 字典  给func按照键值传参
返回值： 返回函数事件对象
```

【3】 关闭进程池

```python
pool.close()
功能： 关闭进程池
```

【4】 回收进程池中进程

```
pool.join()
功能： 回收进程池中进程

```


##  进程间通信（IPC）

1. 必要性： 进程间空间独立，资源不共享，此时在需要进程间数据传输时就需要特定的手段进行数据通信。


2. 常用进程间通信方法

>管道  消息队列  共享内存  信号  信号量  套接字 


###  管道通信(Pipe)

***代码示例：day9/pipe.py***

```
"""
pipe.py 管道通信

注意： 管道对象需在父进程中创建，子进程从父进程中获取
"""

from multiprocessing import Process,Pipe

# 创建管道
# False单向管道 fd1->recv  fd2->send
# 不要在一个进程中同时使用fd1 fd2
fd1,fd2 = Pipe(False)

def app1():
    print("启动app1,请登录，（可以使用app2）")
    print("向app2发请求")
    fd1.send("app1需要：用户名，头像") # 写管道
    data = fd1.recv()
    print("Oh yeah",data)

def app2():
    data = fd2.recv() # 读管道
    print("app1请求:",data)
    fd2.send({'name':'Han','image':'有'})

p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()


```



1. 通信原理

>在内存中开辟管道空间，生成管道操作对象，多个进程使用同一个管道对象进行读写即可实现通信

2. 实现方法

```python
from  multiprocessing import Pipe

fd1,fd2 = Pipe(duplex = True)
功能: 创建管道
参数：默认表示双向管道
如果为False 表示单向管道
返回值：表示管道两端的读写对象
	如果是双向管道均可读写
	如果是单向管道fd1只读  fd2只写

fd.recv()
功能 ： 从管道获取内容
返回值：获取到的数据

fd.send(data)
功能： 向管道写入内容
参数： 要写入的数据

```

### 消息队列

***代码示例：day9/queue_0.py***

```
"""
queue_0.py  消息队列演示
注意 : 通过一个对象操作队列，满足先进先出原则
"""

from multiprocessing import Queue,Process
from time import sleep
from random import randint

# 创建消息队列
q = Queue(5)

# 请求进程
def request():
    for i in range(10):
        sleep(0.5)
        t = (randint(1,100),randint(1,100))
        q.put(t)
        print("=====================")

# 数据处理进程
def handle():
    while True:
        sleep(2)
        x,y = q.get()
        print("数据处理结果 x + y=",x + y)

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()






```

1.通信原理

>在内存中建立队列模型，进程通过队列将消息存入，或者从队列取出完成进程间通信。

2. 实现方法

```python
from multiprocessing import Queue

q = Queue(maxsize=0)
功能: 创建队列对象
参数：最多存放消息个数
返回值：队列对象

q.put(data,[block,timeout])
功能：向队列存入消息
参数：data  要存入的内容
block  设置是否阻塞 False为非阻塞
timeout  超时检测

q.get([block,timeout])
功能：从队列取出消息
参数：block  设置是否阻塞 False为非阻塞
timeout  超时检测
返回值： 返回获取到的内容

q.full()   判断队列是否为满
q.empty()  判断队列是否为空
q.qsize()  获取队列中消息个数
q.close()  关闭队列

```

### 共享内存

***代码示例：day9/value.py***

```
"""
value.py 开辟共享内存
注意: 共享内存只能有一个值
"""

from multiprocessing import Process,Value
import time
from random import randint

# 创建共享内存
money = Value('i',5000)

# 操作内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += randint(1,1000)

def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= randint(100,800)

p1 = Process(target=man)
p2 = Process(target=girl)
p1.start()
p2.start()
p1.join()
p2.join()

print("一个月余额:",money.value)





```

***代码示例：day9/array.py***

```
"""
array.py 存放一组数据
"""

from multiprocessing import Process,Array

# 共享内存，初始[1,2,3,4,5]
# shm = Array('i',[1,2,3,4,5])
# shm = Array('i',4) #共享内存，初始[0,0,0,0]
shm = Array('c',b'Hello')

def fun():
    # 迭代获取共享内存值
    for i in shm:
        print(i)
    shm[0] = b'h'

p = Process(target = fun)
p.start()
p.join()
# for i in shm:
#     print(i)
print(shm.value)  # 用于打印共享内存字节串

```



1. 通信原理：在内中开辟一块空间，进程可以写入内容和读取内容完成通信，但是每次写入内容会覆盖之前内容。

2. 实现方法

![](/home/tarena/下载/11/并发编程/img/6_ctype.png)

```python
from multiprocessing import Value,Array

obj = Value(ctype,data)
功能 ： 开辟共享内存
参数 ： ctype  表示共享内存空间类型 'i'  'f'  'c'
       data   共享内存空间初始数据
返回值：共享内存对象

obj.value  对该属性的修改查看即对共享内存读写


obj = Array(ctype,data)
功能： 开辟共享内存空间
参数： ctype  表示共享内存数据类型
      data   整数则表示开辟空间的大小，其他数据类型表示开辟空间存放的初始化数据
返回值：共享内存对象

Array共享内存读写： 通过遍历obj可以得到每个值，直接可以通过索引序号修改任意值。

* 可以使用obj.value直接打印共享内存中的字节串

```

### 信号量（信号灯集）

***代码示例：day9/sem.py***

```
"""
sem.py  信号量演示
注意: 信号量相当于资源，多个进程对数量进行控制
"""

from multiprocessing import Process,Semaphore
from time import sleep
import os

# 创建信号量
sem = Semaphore(3)

# 任务函数
def handle():
    sem.acquire() # 执行任务必须消耗一个信号量
    print("开始执行任务：",os.getpid())
    sleep(2)
    print("执行任务结束：", os.getpid())
    sem.release() # 增加一个信号量

for i in range(5):
    p = Process(target = handle)
    p.start()





```



1. 通信原理

>给定一个数量对多个进程可见。多个进程都可以操作该数量增减，并根据数量值决定自己的行为。

2. 实现方法

```python	  
from multiprocessing import Semaphore

sem = Semaphore(num)
功能 ： 创建信号量对象
参数 ： 信号量的初始值
返回值 ： 信号量对象

sem.acquire()  将信号量减1 当信号量为0时阻塞
sem.release()  将信号量加1
sem.get_value() 获取信号量数量

```

## 线程编程（Thread）

### 多线程下载文件

```
"""
模拟开启多个线程，在多资源情况下共同下载一个文件
"""
import os
from threading import Thread,Lock
from time import sleep

urls = ["/home/tarena/桌面/",
"/home/tarena/文档/",
"/home/tarena/音乐/",
"/home/tarena/下载/",
"/home/tarena/视频/",
"/home/tarena/图片/",
"/home/tarena/模板/",
]

lock = Lock() # 锁

filename = input("要下载的文件:")
explorer = []
for i in urls:
    # 判断资源库路径中文件是否存在
    if os.path.exists(i+filename):
        # 存文件路径
        explorer.append(i+filename)

num = len(explorer) # 获取有多少资源
if num == 0:
    print("没有资源")
    os._exit(0)
size = os.path.getsize(explorer[0])
block_size = size // num + 1

# 共享资源
fd = open(filename,'wb') # 下载的文件

# 下载文件
def load(path,num):
    f = open(path,'rb') # 从资源中读取内容
    seek_types = block_size * num
    f.seek(seek_types)
    size = block_size

    lock.acquire() # 上锁
    fd.seek(block_size * num)
    while True:
        # sleep(0.1)
        if size < 1024:
            data = f.read(size)
            fd.write(data)
            break
        else:
            data = f.read(1024)
            fd.write(data)
            size -= 1024
    lock.release()

n = 0  # 给每个线程分配的是第几块
jobs = []
for path in explorer:
    t = Thread(target = load,args=(path,n))
    jobs.append(t)
    t.start()
    n += 1

for i in jobs:
    i.join()



```



### 线程基本概念

1. 什么是线程
   【1】 线程被称为轻量级的进程
   【2】 线程也可以使用计算机多核资源，是多任务编程方式
   【3】 线程是系统分配内核的最小单元
   【4】 线程可以理解为进程的分支任务

2. 线程特征
   【1】 一个进程中可以包含多个线程
   【2】 线程也是一个运行行为，消耗计算机资源
   【3】 一个进程中的所有线程共享这个进程的资源
   【4】 多个线程之间的运行互不影响各自运行
   【5】 线程的创建和销毁消耗资源远小于进程
   【6】 各个线程也有自己的ID等特征

```
from thread_test import *
import threading
import time

jobs = []
tm = time.time()
for i in range(10):
    t = threading.Thread(target=io)
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()

print("multi Thread CPU:",time.time() - tm)

```

```
from thread_test import *
import multiprocessing as mp
import time

jobs = []
tm = time.time()
for i in range(10):
    p = mp.Process(target=count,args=(1,1))
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()

print("multi Process CPU:",time.time() - tm)

```



### threading模块创建线程

***代码示例：day9/thread1.py***

```
"""
thread1.py 线程基础示例
步骤： 1. 封装线程函数
      2. 创建线程对象
      3. 启动线程
      4. 回收线程
"""

import threading
from time import sleep
import os

a = 1

# 线程函数
def music():
    global a
    print("a = ",a)
    a = 10000
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:其实你太美")


# 创建线程对象
t = threading.Thread(target=music)
t.start() # 启动线程

# 主线程执行
for i in range(4):
    sleep(1)
    print(os.getpid(),"播放：大碗宽面")

t.join() # 回收线程
print("a:",a)
```

***代码示例：day9/thread2.py***

```
"""
thread2.py 线程函数参数示例
"""

from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    print("%s线程开始执行"%name)
    sleep(sec)
    print("%s执行完毕"%name)

# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,args=(2,),
               kwargs={'name':'T%d'%i})
    jobs.append(t) # 存储线程对象
    t.start()

for i in jobs:
    i.join()
```

【1】 创建线程对象

```	  
from threading import Thread 

t = Thread()
功能：创建线程对象
参数：target 绑定线程函数
     args   元组 给线程函数位置传参
     kwargs 字典 给线程函数键值传参

```

【2】 启动线程

```
 t.start()

```

【3】 回收线程

```
 t.join([timeout])

```

### 线程对象属性

***代码示例：day9/thread_attr.py***

```
"""
thread_attr.py
线程属性演示
"""

from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("进程属性设置")

t = Thread(target=fun,name="AID")

t.setDaemon(True) # 主线程退出分支线程也退出

t.start()

t.setName('Tarena')
print("Name:",t.getName())
print("is alive:",t.is_alive())
print("is daemon:",t.isDaemon())
```



>t.name 线程名称
>t.setName()  设置线程名称
>t.getName()  获取线程名称

>t.is_alive()  查看线程是否在生命周期

>t.daemon  设置主线程和分支线程的退出关系
>t.setDaemon()  设置daemon属性值
>t.isDaemon()  查看daemon属性值
>
>>daemon为True时主线程退出分支线程也退出。要在start前设置，通常不和join一起使用。


### 自定义线程类

***代码示例：day9/myThread.py***

```
from threading import Thread
from time import sleep,ctime

# 完成这个类
class MyClass(Thread):
    # 该方法可以修改，第8行不能传参数
    def __init__(self,target=None,args=(),kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args,**self.kwargs)

# ********************************
# 测试函数，该函数名称，参数都不确定。本函数只提供测试
def player(sec,song):
    for i in range(3):
        print("Playing %s : %s"%(song,ctime()))
        sleep(sec)

t = MyClass(target = player,args=(3,),
            kwargs={'song':'凉凉'})
t.start()
t.join()
```



1. 创建步骤
   【1】 继承Thread类
   【2】 重写`__init__`方法添加自己的属性，使用super()加载父类属性
   【3】 重写run()方法

2. 使用方法
   【1】 实例化对象
   【2】 调用start自动执行run方法
   【3】 调用join回收线程


## 同步互斥

### 线程间通信方法

1. 通信方法

>线程间使用全局变量进行通信


2. 共享资源争夺

* 共享资源：多个进程或者线程都可以操作的资源称为共享资源。对共享资源的操作代码段称为临界区。

* 影响 ： 对共享资源的无序操作可能会带来数据的混乱，或者操作错误。此时往往需要同步互斥机制协调操作顺序。

3. 同步互斥机制

>同步 ： 同步是一种协作关系，为完成操作，多进程或者线程间形成一种协调，按照必要的步骤有序执行操作。

![](/home/tarena/下载/11/并发编程/img/7_同步.png)

>互斥 ： 互斥是一种制约关系，当一个进程或者线程占有资源时会进行加锁处理，此时其他进程线程就无法操作该资源，直到解锁后才能操作。


![](/home/tarena/下载/11/并发编程/img/7_互斥.png)

### 线程同步互斥方法

#### 线程Event

***代码示例：day10/thread_event.py***

```
"""
event 线程互斥方法演示
"""

from threading import Thread,Event

s = None
e = Event()

def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()

t = Thread(target = 杨子荣)
t.start()

print("说对口令就是自己人")
e.wait() # 等待e被set
if s == '天王盖地虎':
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他！")

t.join()







```



```python		  
from threading import Event

e = Event()  创建线程event对象

e.wait([timeout])  阻塞等待e被set

e.set()  设置e，使wait结束阻塞

e.clear() 使e回到未被设置状态

e.is_set()  查看当前e是否被设置

```

#### 线程锁 Lock

***代码示例：day10/thread_lock.py***

```
"""
thread_lock.py
线程锁演示
"""

from threading import Thread,Lock

a = b = 0
lock = Lock()

def value():
    while True:
        lock.acquire() # 上锁
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release() # 解锁

t = Thread(target = value)
t.start()
while True:
    with lock:  # 上锁
        a += 1
        b += 1
                # 解锁
t.join()


```



```python
from  threading import Lock

lock = Lock()  创建锁对象
lock.acquire() 上锁  如果lock已经上锁再调用会阻塞
lock.release() 解锁

with  lock:  上锁
...
...
	 with代码块结束自动解锁

```

### 死锁及其处理

1. 定义

>死锁是指两个或两个以上的线程在执行过程中，由于竞争资源或者由于彼此通信而造成的一种阻塞的现象，若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁。

![](/home/tarena/下载/11/并发编程/img/死锁.jpg)

2. 死锁产生条件

***代码示例: day10/dead_lock.py***

```
"""
死锁情形模拟
"""
from threading import Thread,Lock
from time import sleep

# 账户类
class Account:
    def __init__(self,_id,balance,lock):
        self.id = _id  # id
        self.balance = balance  # 存款
        self.lock = lock # 维护锁

    # 取钱
    def withdraw(self,amount):
        self.balance -= amount
    # 存钱
    def deposit(self,amount):
        self.balance += amount
    # 查看余额
    def get_balance(self):
        return self.balance

# 生成两个账户
Tom = Account('Tom',12000,Lock())
Abby = Account('Abby',9000,Lock())

# 转账  账户金额变动需要先上锁
def transfer(from_,to,amount):
    if from_.lock.acquire():
        from_.withdraw(amount) # from_账户钱减少
        sleep(0.1)
        if to.lock.acquire():
            to.deposit(amount) # to 存钱
            to.lock.release()
        from_.lock.release()
    print("%s给%s转了%d元"%(from_.id,to.id,amount))

t1 = Thread(target=transfer,args=(Tom,Abby,4000))
t2 = Thread(target=transfer,args=(Abby,Tom,1500))
t1.start()
t2.start()
t1.join()
t2.join()
print("Tom:",Tom.get_balance())
print("Abby:",Abby.get_balance())



```



>死锁发生的必要条件
>
>>* 互斥条件：指线程对所分配到的资源进行排它性使用，即在一段时间内某资源只由一个进程占用。如果此时还有其它进程请求资源，则请求者只能等待，直至占有资源的进程用毕释放。
>>* 请求和保持条件：指线程已经保持至少一个资源，但又提出了新的资源请求，而该资源已被其它进程占有，此时请求线程阻塞，但又对自己已获得的其它资源保持不放。
>>* 不剥夺条件：指线程已获得的资源，在未使用完之前，不能被剥夺，只能在使用完时由自己释放,通常CPU内存资源是可以被系统强行调配剥夺的。
>>* 环路等待条件：指在发生死锁时，必然存在一个线程——资源的环形链，即进程集合{T0，T1，T2，···，Tn}中的T0正在等待一个T1占用的资源；T1正在等待T2占用的资源，……，Tn正在等待已被T0占用的资源。

>死锁的产生原因
>
>>简单来说造成死锁的原因可以概括成三句话：
>>
>>* 当前线程拥有其他线程需要的资源
>>* 当前线程等待其他线程已拥有的资源
>>* 都不放弃自己拥有的资源


3. 如何避免死锁

死锁是我们非常不愿意看到的一种现象，我们要尽可能避免死锁的情况发生。通过设置某些限制条件，去破坏产生死锁的四个必要条件中的一个或者几个，来预防发生死锁。预防死锁是一种较易实现的方法。但是由于所施加的限制条件往往太严格，可能会导致系统资源利用率。



## python线程GIL

1. python线程的GIL问题 （全局解释器锁）

>什么是GIL ：由于python解释器设计中加入了解释器锁，导致python解释器同一时刻只能解释执行一个线程，大大降低了线程的执行效率。

>导致后果： 因为遇到阻塞时线程会主动让出解释器，去解释其他线程。所以python多线程在执行多阻塞高延迟IO时可以提升程序效率，其他情况并不能对效率有所提升。

>GIL问题建议
>
>* 尽量使用进程完成无阻塞的并发行为
>* 不使用c作为解释器 （Java  C#）

2. 结论 ： 在无阻塞状态下，多线程程序和单线程程序执行效率几乎差不多，甚至还不如单线程效率。但是多进程运行相同内容却可以有明显的效率提升。

## 进程线程的区别联系

### 区别联系

1. 两者都是多任务编程方式，都能使用计算机多核资源
2. 进程的创建删除消耗的计算机资源比线程多
3. 进程空间独立，数据互不干扰，有专门通信方法；线程使用全局变量通信
4. 一个进程可以有多个分支线程，两者有包含关系
5. 多个线程共享进程资源，在共享资源操作时往往需要同步互斥处理
6. 进程线程在系统中都有自己的特有属性标志，如ID,代码段，命令集等。

### 使用场景

1. 任务场景：如果是相对独立的任务模块，可能使用多进程，如果是多个分支共同形成一个整体任务可能用多线程

2. 项目结构：多种编程语言实现不同任务模块，可能是多进程，或者前后端分离应该各自为一个进程。

3. 难易程度：通信难度，数据处理的复杂度来判断用进程间通信还是同步互斥方法。


### 要求

1. 对进程线程怎么理解/说说进程线程的差异
2. 进程间通信知道哪些，有什么特点
3. 什么是同步互斥，你什么情况下使用，怎么用
4. 给一个情形，说说用进程还是线程，为什么
5. 问一些概念，僵尸进程的处理，GIL问题，进程状态


## 并发网络通信模型

### 常见网络模型

1. 循环服务器模型 ：循环接收客户端请求，处理请求。同一时刻只能处理一个请求，处理完毕后再处理下一个。

  >优点：实现简单，占用资源少
  >缺点：无法同时处理多个客户端请求

  >适用情况：处理的任务可以很快完成，客户端无需长期占用服务端程序。udp比tcp更适合循环。

2. 多进程/线程网络并发模型：每当一个客户端连接服务器，就创建一个新的进程/线程为该客户端服务，客户端退出时再销毁该进程/线程。

  > 优点：能同时满足多个客户端长期占有服务端需求，可以处理各种请求。
  > 缺点： 资源消耗较大

  > 适用情况：客户端同时连接量较少，需要处理行为较复杂情况。

3. IO并发模型：利用IO多路复用,异步IO等技术，同时处理多个客户端IO请求。

   >优点 ： 资源消耗少，能同时高效处理多个IO行为
   >缺点 ： 只能处理并发产生的IO事件，无法处理cpu计算

   >适用情况：HTTP请求，网络传输等都是IO行为。


### 基于fork的多进程网络并发模型

***代码实现: day10/fork_server.py***

```
"""
fork_server.py 基于fork多进程并发
重点代码

1. 创建监听套接字
2. 循环等待客户端连接
3. 客户端连接创建新的进程为客户端服务
4. 原进程继续等待其他客户端连接
5. 客户端退出，对应的进程也销毁
"""

from socket import *
import os
import signal

# 全局变量
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

# 客户端处理
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port 8888...")
while True:
    # 循环等待客户端连接
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt as e:
        os._exit(0)
    except Exception as e:
        print(e)
        continue
    # 创建进程
    pid = os.fork()
    if pid == 0:
        s.close()
        handle(c) # 和客户端交互
        os._exit(0) # 客户端结束后，子进程结束
    else:
        c.close()




```



#### 实现步骤

1. 创建监听套接字
2. 等待接收客户端请求
3. 客户端连接创建新的进程处理客户端请求
4. 原进程继续等待其他客户端连接
5. 如果客户端退出，则销毁对应的进程

### 基于threading的多线程网络并发

***代码实现: day10/thread_server.py***

```
"""
thread_server.py 多线程并发模型
重点代码

创建监听套接字
循环接收客户端连接请求
当有新的客户端连接创建线程处理客户端请求
主线程继续等待其他客户端连接
当客户端退出，则对应分支线程退出
"""
from socket import *
from threading import Thread
import sys

# 全局变量
HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

# 客户端处理
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

print("Listen the port 8888...")
while True:
    # 循环等待客户端连接
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except KeyboardInterrupt as e:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue

    # 创建线程
    t = Thread(target=handle,args=(c,))
    t.setDaemon(True)
    t.start()

```



#### 实现步骤

1. 创建监听套接字
2. 循环接收客户端连接请求
3. 当有新的客户端连接创建线程处理客户端请求
4. 主线程继续等待其他客户端连接
5. 当客户端退出，则对应分支线程退出


### ftp 文件服务器

***代码实现: day11/ftp***

```
"""
ftp 文件服务器 服务端
多进程/多线程并发 socket
"""
from socket import *
from threading import Thread
import sys,os
from time import sleep

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
FTP = "/home/tarena/FTP/" # 文件库位置

# 实现具体功能
class FtpServer(Thread):
    """
    查看文件列表，上传，下载，退出
    """
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            self.connfd.send("充值VIP,百万图书任你选".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)

        filelist = ""
        for file in files:
            if file[0] != '.' and \
                    os.path.isfile(FTP+file):
                filelist += file + '\n'
        self.connfd.send(filelist.encode())

        # for file in files:
        #     # 不是隐藏文件并且是普通文件
        #     if file[0] != '.' and \
        #             os.path.isfile(FTP+file):
        #         sleep(0.1)
        #         self.connfd.send(file.encode())
        # sleep(0.1)
        # self.connfd.send(b'##')

    # 下载文件
    def do_get(self,filename):
        try:
            f = open(FTP+filename,'rb')
        except Exception:
            # 文件不存在
            self.connfd.send("vip可以下载".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        f.close()

    # 上传
    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send('文件已存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接收文件
        f = open(FTP+filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    # 分配任务
    def run(self):
        while True:
            # 客户端请求
            data=self.connfd.recv(1024).decode()
            # 判断请求类型
            if not data or data == 'Q':
                return # 线程结束
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)

# 搭建网络并发模型
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    print("Listen the port 8888...")
    while True:
        # 循环等待客户端连接
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt as e:
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建线程
        t = FtpServer(c)
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
   main()
```

```
"""
ftp 文件服务 ，客户端
"""
from socket import *
import sys
from time import sleep

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 具体功能实现
class FtpClient:
    """
    实现具体功能请求
    """
    def __init__(self,sockfd):
        self.sockfd = sockfd

    # 获取文件列表
    def do_list(self):
        self.sockfd.send(b'L') # 发送请求
        # 等待回去，确认是否有文件列表
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(1024 * 1024).decode()
            print(data)

            # while True:
            #     data = self.sockfd.recv(128).decode()
            #     if data == '##':
            #         break
            #     print(data)
        else:
            print(data) # 不可以查看的原因

    # 退出
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    def do_get(self,filename):
        # 发送请求
        self.sockfd.send(('G '+filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        # 接收文件
        if data == 'OK':
            f = open(filename,'wb')
            # 循环接收内容，写入文件
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                f.write(data)
            f.close()
        else:
            print(data)

    def do_put(self,filename):
        try:
            f = open(filename,'rb')
        except Exception:
            print("文件不存在")
            return
        # 获取真正的文件名
        filename = filename.split('/')[-1]
        # 发送请求
        self.sockfd.send(('P '+filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)

# 网络大家，和终端输入命令选项
def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    # 实例化对象
    ftp = FtpClient(sockfd)

    # 循环发起请求
    while True:
        print("\n=========Command==============")
        print("*****       list        *****")
        print("*****     get  file     *****")
        print("*****     put  file     *****")
        print("*****       quit        *****")
        print("===============================")
        cmd = input("Command:")
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(' ')[-1]
            ftp.do_put(filename)
        else:
            print("请输入正确命令!")

if __name__ == '__main__':
    main()
```



1. 功能 
   【1】 分为服务端和客户端，要求可以有多个客户端同时操作。
   【2】 客户端可以查看服务器文件库中有什么文件。
   【3】 客户端可以从文件库中下载文件到本地。
   【4】 客户端可以上传一个本地文件到文件库。
   【5】 使用print在客户端打印命令输入提示，引导操作



## IO并发

### IO 分类

>IO分类：阻塞IO ，非阻塞IO，IO多路复用，异步IO等


#### 阻塞IO 

1.定义：在执行IO操作时如果执行条件不满足则阻塞。阻塞IO是IO的默认形态。

2.效率：阻塞IO是效率很低的一种IO。但是由于逻辑简单所以是默认IO行为。

3.阻塞情况：

* 因为某种执行条件没有满足造成的函数阻塞
  e.g.  accept   input   recv

* 处理IO的时间较长产生的阻塞状态
  e.g. 网络传输，大文件读写
  		

####　非阻塞IO

***代码实现: day11/block_io***

```
"""
block_io.py 非阻塞io演示
"""
from socket import *
from time import ctime,sleep

f = open('log.txt','a') # 日志文件

s = socket()
s.bind(('0.0.0.0',8888))
s.listen(5)

# 设置套接字非阻塞
# s.setblocking(False)

# 设置超时时间
s.settimeout(3)

while True:
    try:
        c,addr = s.accept()
        print("Connect from",addr)
    except (BlockingIOError,timeout) as e:
        sleep(2)
        f.write(ctime()+':'+str(e)+'\n')
    else:
        data = c.recv(1024)
        print(data)




```



1. 定义 ：通过修改IO属性行为，使原本阻塞的IO变为非阻塞的状态。

* 设置套接字为非阻塞IO

 >sockfd.setblocking(bool)
 > 功能：设置套接字为非阻塞IO
 > 参数：默认为True，表示套接字IO阻塞；设置为False则套接字IO变为非阻塞

* 超时检测 ：设置一个最长阻塞时间，超过该时间后则不再阻塞等待。

  >sockfd.settimeout(sec)
  >功能：设置套接字的超时时间
  >参数：设置的时间

### IO多路复用

1. 定义

>同时监控多个IO事件，当哪个IO事件准备就绪就执行哪个IO事件。以此形成可以同时处理多个IO的行为，避免一个IO阻塞造成其他IO均无法执行，提高了IO执行效率。

2. 具体方案

>select方法 ： windows  linux  unix
>poll方法： linux  unix
>epoll方法： linux


#### select 方法

***代码实现: day11/select_server.py***

```
"""
select tcp 服务
重点代码

1.将关注的IO放入对应的监控类别列表
2.通过select函数进行监控
3.遍历select返回值列表，确定就绪IO事件
4.处理发生的IO事件
"""

from socket import *
from select import select

# 创建监听套接字作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 设置关注列表
rlist = [s] # 等待客户端连接
wlist = []
xlist = []

# 监控IO发生
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            # 有客户端连接
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c) # 连接对象加入监控
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r) # 取消对它关注
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r)

    for w in ws:
        w.send(b'OK')
        wlist.remove(w) # 从写监控中移除


```



```python
rs, ws, xs=select(rlist, wlist, xlist[, timeout])
功能: 监控IO事件，阻塞等待IO发生
参数：rlist  列表  存放关注的等待发生的IO事件
      wlist  列表  存放关注的要主动处理的IO事件
      xlist  列表  存放关注的出现异常要处理的IO
      timeout  超时时间

返回值： rs 列表  rlist中准备就绪的IO
        ws 列表  wlist中准备就绪的IO
	xs 列表  xlist中准备就绪的IO

```

select 实现tcp服务

	【1】 将关注的IO放入对应的监控类别列表
	【2】通过select函数进行监控
	【3】遍历select返回值列表，确定就绪IO事件
	【4】处理发生的IO事件


>注意
>
>>wlist中如果存在IO事件，则select立即返回给ws
>>处理IO过程中不要出现死循环占有服务端的情况
>>IO多路复用消耗资源较少，效率较高

------------

###@@扩展: 位运算

定义 ： 将整数转换为二进制，按二进制位进行运算

运算符号： 

>		&  按位与
>				|  按位或
>				^  按位异或
>				<< 左移
>				>> 右移

```python
e.g.  14 --> 01110
      19 --> 10011

14 & 19 = 00010 = 2  一0则0
14 | 19 = 11111 = 31 一1则1
14 ^ 19 = 11101 = 29 相同为0不同为1
14 << 2 = 111000 = 56 向左移动低位补0
14 >> 2 = 11 = 3  向右移动去掉低位

```

----------------


#### poll方法

***代码实现: day12/poll_server.py***

```
"""
poll  方法实现IO多路服用
重点代码

【1】 创建套接字
【2】 将套接字register
【3】 创建查找字典，并维护
【4】 循环监控IO发生
【5】 处理发生的IO
"""

from socket import *
from select import *

# 创建套接字作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 创建poll对象
p = poll()

# 建立查找字典，通过IO对象的fileno找到对象
# 字典内容与关注IO保持一直{fileno:io_obj}
fdmap = {s.fileno():s}

# 关注s
p.register(s,POLLIN|POLLERR)

# 循环监控IO的发生
while True:
    events = p.poll()
    print(events)
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            # 添加新的关注对象，同时维护字典
            p.register(c,POLLIN)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                # 客户端退出
                p.unregister(fd) # 取消关注
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            p.register(fd,POLLOUT)
            # fdmap[fd].send(b'OK')
        elif event & POLLOUT:
            fdmap[fd].send(b'OK')
            p.register(fd, POLLIN)

```



```python
p = select.poll()
功能 ： 创建poll对象
返回值： poll对象

```


```python	
p.register(fd,event)   
功能: 注册关注的IO事件
参数：fd  要关注的IO
      event  要关注的IO事件类型
  	     常用类型：POLLIN  读IO事件（rlist）
		      POLLOUT 写IO事件 (wlist)
		      POLLERR 异常IO  （xlist）
		      POLLHUP 断开连接 
		  e.g. p.register(sockfd,POLLIN|POLLERR)

p.unregister(fd)
功能：取消对IO的关注
参数：IO对象或者IO对象的fileno

```

```python
events = p.poll()
功能： 阻塞等待监控的IO事件发生
返回值： 返回发生的IO
        events格式  [(fileno,event),()....]
        每个元组为一个就绪IO，元组第一项是该IO的fileno，第二项为该IO就绪的事件类型

```

poll_server 步骤
	   

	【1】 创建套接字
	【2】 将套接字register
	【3】 创建查找字典，并维护
	【4】 循环监控IO发生
	【5】 处理发生的IO



#### epoll方法

***代码实现: day12/epoll_server.py***

```
"""
epoll  方法实现IO多路服用
重点代码

【1】 创建套接字
【2】 将套接字register
【3】 创建查找字典，并维护
【4】 循环监控IO发生
【5】 处理发生的IO
"""

from socket import *
from select import *

# 创建套接字作为关注IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(3)

# 创建epoll对象
ep = epoll()

# 建立查找字典，通过IO对象的fileno找到对象
# 字典内容与关注IO保持一直{fileno:io_obj}
fdmap = {s.fileno():s}

# 关注s
ep.register(s,EPOLLIN|EPOLLERR)

# 循环监控IO的发生
while True:
    events = ep.poll()
    print("你有新的IO需要处理哦：",events)
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            # 添加新的关注对象，同时维护字典
            ep.register(c,EPOLLIN|EPOLLET) # 边缘触发
            fdmap[c.fileno()] = c
        # elif event & EPOLLIN:
        #     data = fdmap[fd].recv(1024).decode()
        #     if not data:
        #         # 客户端退出
        #         ep.unregister(fd) # 取消关注
        #         fdmap[fd].close()
        #         del fdmap[fd]
        #         continue
        #     print(data)
        #     ep.unregister(fd)
        #     ep.register(fd, POLLOUT)
        # elif event & POLLOUT:
        #     fdmap[fd].send(b'OK')
        #     ep.unregister(fd)
        #     ep.register(fd, POLLIN)


```



1. 使用方法 ： 基本与poll相同

   * 生成对象改为 epoll()
   * 将所有事件类型改为EPOLL类型

2. epoll特点

   * epoll 效率比select poll要高
   * epoll 监控IO数量比select要多
   * epoll 的触发方式比poll要多 （EPOLLET边缘触发）


### 协程技术

#### 基础概念

1. 定义：纤程，微线程。是允许在不同入口点不同位置暂停或开始的计算机程序，简单来说，协程就是可以暂停执行的函数。

2. 协程原理 ： 记录一个函数的上下文，协程调度切换时会将记录的上下文保存，在切换回来时进行调取，恢复原有的执行内容，以便从上一次执行位置继续执行。

3. 协程优缺点

>优点
>
>>1. 协程完成多任务占用计算资源很少
>>2. 由于协程的多任务切换在应用层完成，因此切换开销少
>>3. 协程为单线程程序，无需进行共享资源同步互斥处理

>缺点
>
>> 协程的本质是一个单线程，无法利用计算机多核资源

--------------------------------

####扩展延伸@标准库协程的实现

python3.5以后，使用标准库asyncio和async/await 语法来编写并发代码。asyncio库通过对异步IO行为的支持完成python的协程。虽然官方说asyncio是未来的开发方向，但是由于其生态不够丰富，大量的客户端不支持awaitable需要自己去封装，所以在使用上存在缺陷。更多时候只能使用已有的异步库（asyncio等），功能有限

```
import asyncio

async def fun1():
    print("Start1")
    # 遇到阻塞跳出
    await asyncio.sleep(3)
    print("end1")

async def fun2():
    print("Start2")
    # 遇到阻塞跳出
    await asyncio.sleep(2)
    print("end2")

cor1 = fun1()
cor2 = fun2()

tasks = [asyncio.ensure_future(cor1),
         asyncio.ensure_future(cor2)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
```



------------------------------

#### 第三方协程模

1.  greenlet模块

***示例代码: day12/greenlet_0.py***

```
"""
协程行为展示
"""

from greenlet import greenlet

def fun1():
    print("执行fun1")
    gr2.switch()
    print("结束fun1")
    gr2.switch()

def fun2():
    print("执行fun2")
    gr1.switch()
    print("结束fun2")

# 将函数变为协成函数
gr1 = greenlet(fun1)
gr2 = greenlet(fun2)
gr1.switch()
```



* 安装 ： sudo  pip3 install greenlet

* 函数 

```python
greenlet.greenlet(func)
功能：创建协程对象
参数：协程函数

g.switch()
功能：选择要执行的协程函数

```

2. gevent模块

***示例代码: day12/gevent_test.py***

```
"""
gevent 协成模块示例
"""
import gevent
# 导入脚本执行time模块操作
from gevent import monkey
monkey.patch_time()
from time import sleep

# 协程函数
def foo(a,b):
    print("Running foo ..",a,b)
    sleep(3)
    print("Foo again")

def bar():
    print("Running bar ..")
    sleep(2)
    print("Bar again")

# 生成协程对象
f = gevent.spawn(foo,1,2)
g = gevent.spawn(bar)
gevent.joinall([f,g]) # 阻塞等待f,g执行完
```

***示例代码: day12/gevent_server.py***

```
"""
gevent server 基于协程的tcp并发
"""
import gevent
from gevent import monkey
monkey.patch_all() # 执行脚本修改socket阻塞行为
from socket import *

def handle(c):
    while True:
        data = c.recv(1024).decode()
        if not data:
            return
        print(data)
        c.send(b'OK')

# 创建套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(5)

# 循环接收来自客户端请求
while True:
    c,addr = s.accept()
    print("Connect from",addr)
    # handle(c)  # 循环方案
    gevent.spawn(handle,c) # 协程方案

```

​				

* 安装：sudo pip3 install gevent

* 函数

```python
gevent.spawn(func,argv)
功能: 生成协程对象
参数：func  协程函数
     argv  给协程函数传参（不定参）
返回值： 协程对象

gevent.joinall(list,[timeout])
功能: 阻塞等待协程执行完毕
参数：list  协程对象列表
     timeout 超时时间

gevent.sleep(sec)
功能: gevent睡眠阻塞
参数：睡眠时间

* gevent协程只有在遇到gevent指定的阻塞行为时才会自动在协程之间进行跳转
如gevent.joinall(),gevent.sleep()带来的阻塞

```

* monkey脚本

>作用：在gevent协程中，协程只有遇到gevent指定类型的阻塞才能跳转到其他协程，因此，我们希望将普通的IO阻塞行为转换为可以触发gevent协程跳转的阻塞，以提高执行效率。

> 转换方法：gevent 提供了一个脚本程序monkey,可以修改底层解释IO阻塞的行为，将很多普通阻塞转换为gevent阻塞。

> 使用方法

>>【1】 导入monkey

			from gevent  import monkey

>>【2】 运行相应的脚本，例如转换socket中所有阻塞

			monkey.patch_socket()

>>【3】 如果将所有可转换的IO阻塞全部转换则运行all

			monkey.patch_all()

>>【4】 注意：脚本运行函数需要在对应模块导入前执行



### HTTPServer v2.0 

1. 主要功能 ：
   【1】 接收客户端（浏览器）请求
   	【2】 解析客户端发送的请求
   	【3】 根据请求组织数据内容
   	【4】 将数据内容形成http响应格式返回给浏览器

   2. 升级点 ：
      【1】 采用IO并发，可以满足多个客户端同时发起请求情况
      【2】 做基本的请求解析，根据具体请求返回具体内容，同时满足客户端简单的非网页请求情况

	【3】 通过类接口形式进行功能封装

***day12/http_server.py***

```
"""
httpserver 2.0
env: python3.6
io多路复用 http练习
"""
from socket import *
from select import select


class HTTPServer:
    def __init__(self, host='0.0.0.0', port=80, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        # select 监控列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               1)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)

    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)
        # 设置关注的IO
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist,
                                self.wlist,
                                self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    self.rlist.append(c)
                else:
                    # 有客户端发请求
                    self.handle(r)

    # 处理客户端请求
    def handle(self, connfd):
        # 接收http请求
        request = connfd.recv(4096)
        # 客户端断开处理
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return

        # 提取请求内容
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print(info)

        # 根据info情况分类
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)

    def get_html(self, connfd, info):
        if info == '/':
            # 主页
            filename = self.dir + "/index.html"
        else:
            # 其他网页
            filename = self.dir + info
        try:
            f = open(filename)
        except Exception:
            # 没有网页
            response = "HTTP/1.1 404 Not Found\r\n"
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += "<h1>Sorry</h1>"
        else:
            # 有网页
            response = "HTTP/1.1 200 OK\r\n"
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += f.read()
        finally:
            connfd.send(response.encode())

    def get_data(self, connfd, info):
        f = open(self.dir + '/timg.jpeg', 'rb')
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:image/jpeg\r\n"
        response += '\r\n'
        response = response.encode() + f.read()
        connfd.send(response)


if __name__ == '__main__':
    # 用户自己提供的内容
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = "./static"  # 网页目录

    http = HTTPServer(HOST, PORT, DIR)  # 实例化对象
    http.serve_forever()  # 启动服务
```

```
from socket import *

# 创建tcp套接字
sockfd = socket() # 默认值

# 连接服务器
server_addr = ('127.0.0.1',8888) # 服务器地址
sockfd.connect(server_addr)

# 先发后收
while True:
    msg = input("Msg:")
    if not msg:
        break
    sockfd.send(msg.encode()) #字节串
    data = sockfd.recv(1024)
    print("From server:",data.decode())

sockfd.close()



```



数据结构 
==========================

## 数据结构基本概念

### 什么是数据结构？

1. 数据

> 数据即信息的载体，是能够输入到计算机中并且能被计算机识别、存储和处理的符号总称。

2. 数据元素

> 数据元素是数据的基本单位，又称之为记录（Record）。一般数据元素由若干基本项组成。   

3. 数据结构

> 数据结构指的是数据元素及数据元素之间的相互关系，或组织数据的形式。

### 数据之间的结构关系

1. 逻辑结构

> 表示数据之间的抽象关系（如邻接关系、从属关系等），按每个元素可能具有的直接前趋数和直接后继数将逻辑结构分为“线性结构”和“非线性结构”两大类。

2. 存储结构

> 逻辑结构在计算机中的具体实现方法，分为顺序存储方法、链接存储方法、索引存储方法、散列存储方法。

### 逻辑结构（关系）

1. 特点：

* 只是描述数据结构中数据元素之间的联系规律
* 是从具体问题中抽象出来的数学模型，是独立于计算机存储器的（与机器无关）

2. 逻辑结构分类

* 线性结构

> 对于数据结构课程而言，简单地说，线性结构是n个数据元素的有序（次序）集合。
>
> > - 集合中必存在唯一的一个"第一个元素"；
> > - 集合中必存在唯一的一个"最后的元素"；
> > - 除最后元素之外，其它数据元素均有唯一的"后继"；
> > - 除第一元素之外，其它数据元素均有唯一的"前驱"。

* 树形结构（层次结构）

>树形结构指的是数据元素之间存在着“一对多”的树形关系的数据结构，是一类重要的非线性数据结构。在树形结构中，树根结点没有前驱结点，其余每个结点有且只有一个前驱结点。叶子结点没有后续结点，其余每个结点的后续节点数可以是一个也可以是多个。

* 图状结构（网状结构）

>图是一种比较复杂的数据结构。在图结构中任意两个元素之间都可能有关系，也就是说这是一种多对多的关系。

* 其他结构

>除了以上几种常见的逻辑结构外，数据结构中还包含其他的结构，比如集合等。有时根据实际情况抽象的模型不止是简单的某一种，也可能拥有更多的特征。

![逻辑结构](/home/tarena/下载/11/数据结构/img/data1.png)

### 存储结构（关系）

1. 特点：

* 是数据的逻辑结构在计算机存储器中的映象（或表示）
* 存储结构是通过计算机程序来实现的，因而是依赖于具体的计算机语言的。

2. 基础存储结构

* 顺序存储    

>顺序存储（Sequential Storage）：将数据结构中各元素按照其逻辑顺序存放于存储器一片连续的存储空间中。

* 链式存储

>链式存储（Linked Storage）：将数据结构中各元素分布到存储器的不同点，用记录下一个结点位置的方式建立它们之间的联系，由此得到的存储结构为链式存储结构。 


## 线性表

线性表的定义是描述其逻辑结构，而通常会在线性表上进行的查找、插入、删除等操作。
线性表作为一种基本的数据结构类型，在计算机存储器中的存储一般有两种形式，一种是顺序存储，一种是链式存储。

### 线性表的顺序存储

1. 定义

>若将线性表L=(a0,a1, ……,an-1)中的各元素依次存储于计算机一片连续的存储空间，这种机制表示为线性表的顺序存储结构。

2. 特点

>* 逻辑上相邻的元素 ai, ai+1，其存储位置也是相邻的；
>* 存储密度高，方便对数据的遍历查找。
>* 对表的插入和删除等运算的效率较差。

3. 程序实现

> 在Python中，list存放于一片单一连续的内存块，故可借助于列表类型来描述线性表的顺序存储结构，而且列表本身就提供了丰富的接口满足这种数据结构的运算。

```python
>>>L = [1,2,3,4]
>>>L.append(10)      #尾部增加元素
L
[1, 2, 3, 4, 10]

>>>L.insert(1,20)    #插入元素
L
[1, 20, 2, 3, 4, 10]

>>>L.remove(3)       #删除元素
L
[1, 20, 2, 4, 10]     

>>>L[4] = 30         #修改
L
[1, 20, 2, 4, 30]

>>>L.index(2)        #查找
2
```

### 线性表的链式存储

1. 定义

>将线性表L=(a0,a1,……,an-1)中各元素分布在存储器的不同存储块，称为结点，每个结点（尾节点除外）中都持有一个指向下一个节点的引用，这样所得到的存储结构为链表结构。

![链表结构](/home/tarena/下载/11/数据结构/img/data2.png)

2. 特点

>* 逻辑上相邻的元素 ai, ai+1，其存储位置也不一定相邻；
>* 存储稀疏，不必开辟整块存储空间。
>* 对表的插入和删除等运算的效率较高。
>* 逻辑结构复杂，不利于遍历。


3. 程序实现

  ***代码实现：  day1/linklist.py***

```
"""
linklist.py
功能: 使用节点作为数据元素的生成器,对数据元素之间的关系进行构建和操作

重点代码
"""

# 创建节点类
class Node:
    """
    包含一个简单的数字作为数据
    next 构建关系
    """
    def __init__(self,val,next=None):
        self.val = val  #  有用数据
        self.next = next # 节点关系

"""
1. 构建节点间关系
2. 在节点中存储数据
3. 对单链表进行节点操作
"""

# 单链表的类
class LinkList:
    """
    思路: 生成对象即表示一个单链表对象
         对象调用方法可以完成对单链表的各种操作
    """
    def __init__(self):
        """
        初始化时 创建一个无用的节点,让对象拥有该节点,以表达链表的开端
        """
        self.head = Node(None)

    # 初始化
    def init_list(self,iter):
        p = self.head
        for i in iter:
            p.next = Node(i)
            p = p.next

    # 遍历打印
    def show(self):
        p = self.head.next # 第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next   # p向后移动

    # 判断链表是否为空
    def is_empty(self):
        return self.head.next is None

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self,val):
        p = self.head
        # p 移动到最后一个节点
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_insert(self,val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 指定位置插入
    def insert(self,index,val):
        p = self.head
        # 将p移动到待插入位置的前一个
        for i in range(index):
            # 超出最大范围
            if p.next is None:
                break
            p = p.next

        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点(删除第一个val值)
    def delete(self,val):
        p = self.head
        # 确定p的位置(停留在待删除节点的前一个)
        while p.next and p.next.val != val:
            p = p.next

        # 分情况讨论
        if p.next is None:
            raise ValueError("x not in link")
        else:
            p.next = p.next.next

    # 获取节点值
    def get_value(self,index):
        if index < 0:
            raise IndexError('link index out of range')
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError('link index out of range')
            p = p.next
        return p.val



if __name__ == '__main__':
    link = LinkList()
    link.init_list(range(5))
    # link.show()
    # link.append(5)
    # link.show()
    # link.head_insert(9)
    # link.show()
    # link.insert(2,10)
    # link.show()
    # link.delete(8)
    # link.show()
    print(link.get_value(5))









# node1 = Node(1)
# link.head.next = node1
#
# node2 = Node(2)
# node1.next = node2
#
# node3 = Node(3)
# node2.next = node3






```

### 插入时间比较

```
import time
from linklist import *

# 100  time: 5.4836273193359375e-06
# 1000 time: 5.7220458984375e-06


link = LinkList()
link.init_list(range(1000000))

st = time.time()
link.insert(99999,'007')
print("time:",time.time() - st)
```

### 2个链表连接

```
from day01.linklist import *

l1 = LinkList()
l2 = LinkList()

l1.init_list([1,5,7,8,10,12,13,19])
l2.init_list([0,3,4,8,9])

# 将l2合并到l1当中
def merge(l1,l2):
    p = l1.head
    q = l2.head.next
    while p.next is not None and q is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp
    if p.next is None:
        p.next = q  # 将最后剩余的连接上


merge(l1,l2)
l1.show()

```



## 栈和队列

### 栈

1. 定义

>栈是限制在一端进行插入操作和删除操作的线性表（俗称堆栈），允许进行操作的一端称为“栈顶”，另一固定端称为“栈底”，当栈中没有元素时称为“空栈”。

2. 特点：

>* 栈只能在一端进行数据操作
>* 栈模型具有先进后出或者叫做后进先出的规律

![栈](/home/tarena/下载/11/数据结构/img/data5.png)

3. 栈的代码实现 

栈的操作有入栈（压栈），出栈（弹栈），判断栈的空满等操作。

***顺序存储代码实现： day2/sstack.py***

```
"""
sstack.py  栈模型的顺序存储
重点代码

思路:
1. 利用列表完成顺序存储,但是列表功能多,不符合栈模型特点
2. 使用类将列表封装,提供符合栈特点的接口方法
"""

# 自定义异常
class StackError(Exception):
    pass

# 顺序栈模型
class SStack:
    def __init__(self):
        # 开辟一个顺序存储的模型空间
        # 列表的尾部表示栈顶
        self._elems = []

    # 判断栈是否为空
    def is_empty(self):
        return self._elems == []

    # 入栈
    def push(self,val):
        self._elems.append(val)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        # 弹出一个值并返回
        return self._elems.pop()

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems[-1]


if __name__ == '__main__':
    st = SStack()
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
```

***链式存储代码实现： day2/lstack.py***

```
"""
lstack.py 栈的链式结构
重点代码

思路:
1. 源于节点存储数据,建立节点关联
2. 封装方法 入栈 出栈 栈空 栈顶元素
3. 链表的开头作为栈顶(不需要每次遍历)
"""

# 自定义异常
class StackError(Exception):
    pass

# 创建节点类
class Node:
    def __init__(self,val,next=None):
        self.val = val  #  有用数据
        self.next = next # 节点关系

# 链式栈
class LStack:
    def __init__(self):
        # 标记顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self,val):
        self._top = Node(val,self._top)

    def pop(self):
        if self._top is None:
            raise StackError("Stack is empty")
        value = self._top.val
        self._top = self._top.next
        return value

    def top(self):
        if self._top is None:
            raise StackError("Stack is empty")
        return self._top.val


if __name__ == '__main__':
    ls = LStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    while not ls.is_empty():
        print(ls.pop())
```

### 两个栈实现队列

```
"""
两个栈实现队列
"""
from lstack import *

class MyQueue:
    def __init__(self):
        self.en_stack = LStack()
        self.de_stack = LStack()

    def is_empty(self):
        if self.en_stack.is_empty() and \
                self.de_stack.is_empty():
            return True
        else:
            return False

    def enqueue(self,val):
        # 先将出队栈中的所有数导入到入队栈
        while not self.de_stack.is_empty():
            self.en_stack.push(self.de_stack.pop())
        self.en_stack.push(val)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Error")
        # 先将入队栈中的内容导入到出队栈
        while not self.en_stack.is_empty():
            self.de_stack.push(self.en_stack.pop())
        return self.de_stack.pop()


q = MyQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
while not q.is_empty():
    print(q.dequeue())
```

### 逆波兰表达式

```
"""
逆波兰表达式练习
"""

from sstack import *

st = SStack()

while True:
    exp = input()
    tmp = exp.split(' ')
    for i in tmp:
        if i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x + y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x - y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x * y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x / y)
        elif i == 'p':
            print(st.top()) # 查看栈顶元素
        else:
            st.push(int(i))




```



### 队列

1. 定义

>队列是限制在两端进行插入操作和删除操作的线性表，允许进行存入操作的一端称为“队尾”，允许进行删除操作的一端称为“队头”。

2. 特点：

>* 队列只能在队头和队尾进行数据操作
>* 队列模型具有先进先出或者叫做后进后出的规律

![队列](/home/tarena/下载/11/数据结构/img/data6.png)

3. 队列的代码实现 

队列的操作有入队，出队，判断队列的空满等操作。

***顺序存储代码实现： day2/squeue.py***

```
"""
squeue.py  队列的顺序存储

思路分析:
1. 基于列表完成数据的存储
2. 通过封装功能完成队列的基本行为
3. 无论那边做对头/队尾 都会在操作中有内存移动
"""

# 自定义异常
class QueueError(Exception):
    pass

# 队列操作
class SQueue:
    def __init__(self):
        self._elems = []

    # 判断队列是否为空
    def is_empty(self):
        return self._elems == []

    # 入队
    def enqueue(self,val):
        self._elems.append(val)

    # 出队
    def dequeue(self):
        if not self._elems:
            raise QueueError("Queue is empty")
        return self._elems.pop(0) # 弹出第一个数据


if __name__ == '__main__':
    sq = SQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while not sq.is_empty():
        print(sq.dequeue())







```

***链式存储代码实现： day2/lqueue.py***

```
"""
lqueue.py 链式队列
重点代码

思路分析:
1. 基于链表构建队列模型
2. 链表的头作为队头,尾作为队尾
3. 定义两个标记标记队头和队尾
4. 头和尾代表同一个无用节点时队列为空
"""

# 自定义异常
class QueueError(Exception):
    pass

# 创建节点类
class Node:
    def __init__(self,val,next=None):
        self.val = val  #  有用数据
        self.next = next # 节点关系

# 队列操作
class LQueue:
    def __init__(self):
        # front 队头  rear 队尾
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front == self.rear

    def enqueue(self,val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        # front 是指向队头节点的前一个
        self.front = self.front.next
        return self.front.val

if __name__ == '__main__':
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    while not lq.is_empty():
        print(lq.dequeue())







```

### 队列内容反转

```
"""
队列内容反转
"""

from squeue import *
from lstack import *

sq = SQueue()
ls = LStack()  # 用于中转数据

for i in range(15):
    sq.enqueue(i)

# 出队入栈
while not sq.is_empty():
    ls.push(sq.dequeue())

# 出栈入队
while not ls.is_empty():
    sq.enqueue(ls.pop())


while not sq.is_empty():
    print(sq.dequeue())


```



## 树形结构

###  基础概念 

1. 定义

>树（Tree）是n（n≥0）个节点的有限集合T，它满足两个条件：有且仅有一个特定的称为根（Root）的节点；其余的节点可以分为m（m≥0）个互不相交的有限集合T1、T2、……、Tm，其中每一个集合又是一棵树，并称为其根的子树（Subtree）。

![](/home/tarena/下载/11/数据结构/img/data7.png)


2. 基本概念 

>* 一个节点的子树的个数称为该节点的度数，一棵树的度数是指该树中节点的最大度数。

>* 度数为零的节点称为树叶或终端节点，度数不为零的节点称为分支节点。

>* 一个节点的子树之根节点称为该节点的子节点，该节点称为它们的父节点，同一节点的各个子节点之间称为兄弟节点。一棵树的根节点没有父节点，叶节点没有子节点。

>* 节点的层数等于父节点的层数加一，根节点的层数定义为一。树中节点层数的最大值称为该树的高度或深度。

![](/home/tarena/下载/11/数据结构/img/data8.png)

### 二叉树

#### 定义与特征

1. 定义

>二叉树（Binary Tree）是n（n≥0）个节点的有限集合，它或者是空集（n＝0），或者是由一个根节点以及两棵互不相交的、分别称为左子树和右子树的二叉树组成。二叉树与普通有序树不同，二叉树严格区分左孩子和右孩子，即使只有一个子节点也要区分左右。

![](/home/tarena/下载/11/数据结构/img/data9.png)

2. 二叉树的特征

* 二叉树第i（i≥1）层上的节点最多为$2^{i-1}$个。
* 深度为k（k≥1）的二叉树最多有$2^k－1$个节点。
* 在任意一棵二叉树中，树叶的数目比度数为2的节点的数目多一。

* 满二叉树 ：深度为k（k≥1）时有$2^k－1$个节点的二叉树。


#### 二叉树的遍历

>遍历 ：沿某条搜索路径周游二叉树，对树中的每一个节点访问一次且仅访问一次。

> 先序遍历： 先访问树根，再访问左子树，最后访问右子树；
> 中序遍历： 先访问左子树，再访问树根，最后访问右子树；
> 后序遍历： 先访问左子树，再访问右子树，最后访问树根；
> 层次遍历:  从根节点开始，逐层从左向右进行遍历。

#### 递归思想和实践

1. 什么是递归？

所谓递归函数是指一个函数的函数体中直接调用或间接调用了该函数自身的函数。这里的直接调用是指一个函数的函数体中含有调用自身的语句，间接调用是指一个函数在函数体里有调用了其它函数，而其它函数又反过来调用了该函数的情况。

2. 递归函数调用的执行过程分为两个阶段

>递推阶段：从原问题出发，按递归公式递推从未知到已知，最终达到递归终止条件。
>回归阶段：按递归终止条件求出结果，逆向逐步代入递归公式，回归到原问题求解。

3. 优点与缺点

>优点：递归可以把问题简单化，让思路更为清晰,代码更简洁
>缺点：递归因系统环境影响大，当递归深度太大时，可能会得到不可预知的结果

#### 递归： 求n的阶乘 

```
# def recursion(n):
#     resule = 1
#     for i in range(1,n+1):
#         resule *= i
#     return resule

# 递归函数
def recursion(n):
    # 递归的终止条件
    if n <= 1:
        return 1
    return n * recursion(n - 1)

print(recursion(3))
```



#### 二叉树的代码实现

##### 二叉树顺序存储

二叉树本身是一种递归结构，可以使用Python list 进行存储。但是如果二叉树的结构比较稀疏的话浪费的空间是比较多的。

* 空结点用None表示
* 非空二叉树用包含三个元素的列表[d,l,r]表示，其中d表示根结点，l，r左子树和右子树。

```
['A',['B',None,None
     ],
     ['C',['D',['F',None,None],
               ['G',None,None],
          ],     
          ['E',['H',None,None],
               ['I',None,None],
          ],
     ]
]
```

![](/home/tarena/下载/11/数据结构/img/bitree1.png)


##### 二叉树链式存储

***二叉树遍历： day3/bitree.py***

```
"""
bitree.py 二叉树的实现

思路分析:
1. 使用链式存储, Node表达一个节点(值,左链接,右链接)
2. 分析遍历过程
"""


# 二叉树节点
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树遍历
class Bitree:
    # 传入树根
    def __init__(self, root):
        self.root = root

    # 先序遍历
    def preOrder(self, node):
        if node is None:
            return
        print(node.val, end=' ')
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val, end=' ')
        self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val, end=' ')

    # 层次遍历
    def levelOrder(self, node):
        import day02.lqueue
        lq = day02.lqueue.LQueue()
        # 初始节点先入队,循环判断,队列不为空则出队
        # 出队元素的左右孩子分别入队
        lq.enqueue(node)
        while not lq.is_empty():
            # 出队,打印表示遍历
            node = lq.dequeue()
            print(node.val, end=' ')
            if node.left:
                lq.enqueue(node.left)
            if node.right:
                lq.enqueue(node.right)


if __name__ == '__main__':
    # B F G D H I E C A
    # 构建起一个二叉树
    b = Node('B')
    f = Node('F')
    g = Node("G")
    d = Node('D', f, g)
    h = Node('H')
    i = Node('I')
    e = Node('E', h, i)
    c = Node('C', d, e)
    a = Node('A', b, c)  # 树根

    bt = Bitree(a)

    bt.preOrder(bt.root)
    print()
    bt.inOrder(bt.root)
    print()
    bt.levelOrder(bt.root)
```




## 算法基础

### 基础概念特征

1. 定义

>算法是一个有穷规则（或语句、指令）的有序集合。它确定了解决某一问题的一个运算序列。对于问题的初始输入，通过算法有限步的运行，产生一个或多个输出。

数据的逻辑结构与存储结构密切相关:

* 算法设计:  取决于选定的逻辑结构
* 算法实现: 依赖于采用的存储结构


2. 算法的特性

* 有穷性 —— 算法执行的步骤（或规则）是有限的；
* 确定性 —— 每个计算步骤无二义性；
* 可行性 —— 每个计算步骤能够在有限的时间内完成；
* 输入 ，输出 —— 存在数据的输入和出输出

3. 评价算法好坏的方法

- 正确性：运行正确是一个算法的前提。
- 可读性：容易理解、容易编程和调试、容易维护。
- 健壮性：考虑情况全面，不容以出现运行错误。
- 时间效率高：算法消耗的时间少。
- 储存量低：占用较少的存储空间。

### 时间复杂度计算

算法效率——用依据该算法编制的程序在计算机上执行所消耗的时间来度量。“O”表示一个数量级的概念。根据算法中语句执行的最大次数（频度）来 估算一个算法执行时间的数量级。

> 计算方法：
>
> > 写出程序中所有运算语句执行的次数，进行加和
> > 如果得到的结果是常量则时间复杂度为1
> > 如果得到的结果中存在变量n则取n的最高次幂作为时间复杂度



### 排序和查找

#### 排序

排序(Sort)是将无序的记录序列（或称文件）调整成有序的序列。排序方法有很多种，下面举例说明：

* 冒泡排序

>冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

* 快速排序

>步骤:
>
>>从数列中挑出一个元素，称为 "基准"（pivot），
>>重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
>>递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

### ***冒泡排序***

```
# 冒泡
def bubble(l):
    n = len(l)
    # 循环n - 1 次,每次确定一个最大值
    for i in range(n - 1):
        # 两两比较交换
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j],l[j + 1] = l[j + 1],l[j]


l = [4,5,7,1,2,9,6,8]
bubble(l)
print(l)
```

### 快速排序

```

def sub_sort(l,low,high):
    x = l[low]  # 基准
    while low < high:
        # 如果后边的数比x大high向前走
        while l[high] > x and high > low:
            high -= 1
        l[low] = l[high]  # 比x小的往前甩
        # 如果前面的数比x小则low往后走
        while l[low] <= x and low < high:
            low += 1
        l[high] = l[low]  # 比x大的往后甩
    l[low] = x  # 将x插入最终位置
    return low  #  每一轮最终基准数确定的位置


# low : 第一个元素索引号,high: 最后一个元素索引号
"""
该写法表示希望low传一个整形,high传一个整形,返回值为None类型
但是没有强制要求必须这样做
"""
def quick(l:list,low:int,high:int)->None:
    if low < high:
        key = sub_sort(l,low,high)
        quick(l,low,key-1)
        quick(l,key+1,high)


l = [8,1,12,7,6,10,3,4,8,5,9,2,11,5,13]
quick(l,0,len(l)-1)
print(l)
```



#### 查找

查找(或检索)是在给定信息集上寻找特定信息元素的过程。

### 二分法查找

当数据量很大适宜采用该方法。采用二分法查找时，数据需是排好序的。

***二分查找代码实现： day3/search.py***

```
"""
二分查找实现
"""

# 从l中找到key的索引号
def search(l,key):
    low,high = 0,len(l) - 1

    while low <= high:
        # 中间数的索引
        mid = (low + high) // 2
        if l[mid] < key:
            low = mid + 1
        elif l[mid] > key:
            high = mid - 1
        else:
            return mid


l = [1,2,3,4,5,6,7,8,9,10,11]
print("Key index:",search(l,11))
```

## dict项目

***参考代码：project/dict***

## 功能说明

>用户可以登录和注册
>    * 登录凭借用户名和密码登录
>
>* 注册要求用户必须填写用户名，密码，其他内容自定
>* 用户名要求不能重复
>* 要求用户信息能够长期保存

>可以通过基本的图形界面print以提示客户端输入。
>
>* 程序分为服务端和客户端两部分
>* 客户端通过print打印简单界面输入命令发起请求
>* 服务端主要负责逻辑数据处理
>* 启动服务端后应该能满足多个客户端同时操作

>客户端启动后即进入一级界面，包含如下功能：登录    注册    退出

	* 退出后即退出该软件
	* 登录成功即进入二级界面，失败回到一级界面
	* 注册成功可以回到一级界面继续登录，也可以直接用注册用户进入二级界面
	

>用户登录后进入二级界面，功能如下：查单词    历史记录    注销

	* 选择注销则回到一级界面
	* 查单词：循环输入单词，得到单词解释，输入特殊符号退出单词查询状态
	* 历史记录：查询当前用户的查词记录，要求记录包含name   word   time。可以查看所有记录或者前10条均可。
	

## 项目流程

1. 确定技术点

   并发模型和网络模型
      多进程tcp 并发模型

   确定细节功能，注册要注册什么，注册后是否直接登录
      注册 ： 用户名密码， 加密存储，注册后直接登录
      历史记录 ： 最近的前10个

   一级界面，二级界面如何切换

     见 demo

2. mysql数据库设计  dict

   words ：  id    word   mean
   user :  id  name  passwd

   create table user (id int primary key auto_increment,name varchar(32) not null,passwd char(128) not null);

   hist :  id  name  word   time

   create table hist (id int primary key auto_increment,name varchar(32) not null,word varchar(32) not null,time datetime default now());


3. 结构设计，功能模块划分

   如何封装，客户端和服务端工作流程，有几个功能模块

   *  函数封装
   *  功能模块： 通信，登录，注册，查询，历史记录

4. 通信搭建

5. 注册
   客户端 ： 输入用户名密码
            发送请求
            接收反馈

   服务端 ： 接收请求，判断请求类型
            判定用户可否注册
            给客户端反馈

   登录
       客户端 : 输入用户名密码
               发送请求
               等待反馈

   服务端 ： 接收请求
            验证信息
            发送结果



   查询
       客户端 ： 输入单词
                发送请求 （套接字）
                接收结果

   服务器 ：　接收请求
   　　　　　　查找单词
   　　　　　　插入历史记录
   　　　　　　发送给客户端

   历史记录

协议 ： 登录   L
       注册   R
       查单词  Q
       历史记录  H
       退出   E

cookie：

    import  getpass
    pwd = getpass.getpass()
    功能: 隐藏输入内容


    import  hashlib
    
    hash = hashlib.md5()
    功能： 生产md5对象
    参数 ： 盐（自定义的字节串）
    
    hash.update(passwd.encode())
    功能: 进行加密处理
    参数: 密码转换为字节串
    
    new_passwd = hash.hexdigest()
    功能： 得到转换后的密码

## 服务端

```
"""
dict 服务端

* 处理业务逻辑
* 多进程并发模型
"""

from socket import *
from multiprocessing import Process
import signal,sys
from dict_db import User

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
db = User(database='dict') # 数据库操作对象

# 注册逻辑
def do_register(connfd,data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.register(name,passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'Fail')

# 登录逻辑
def do_login(connfd,data):
    tmp = data.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name, passwd):
        connfd.send(b'OK')
    else:
        connfd.send(b'Fail')

# 处理客户端各种请求
def request(connfd):
    db.create_cursor() # 每个子进程有自己的游标
    while True:
        data = connfd.recv(1024).decode() # 接受请求
        if not data or data[0] == 'E':
            sys.exit() # 退出对应的子进程
        elif data[0] == 'R':
            do_register(connfd,data)
        elif data[0] == 'L':
            do_login(connfd,data)
        elif data[0] == 'Q':
            do_query(connfd,data)
        elif data[0] == 'H':
            do_history(connfd,data)

# 搭建网络
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进场
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # 循环等待客户端链接
    print("Listen the port 8888")
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sys.exit("服务退出")
        except Exception as e:
            print(e)
            continue

        # 创建子进程
        p = Process(target=request,args=(c,))
        p.daemon = True
        p.start()

if __name__ == '__main__':
    main()












```



## 客户端

```
"""
dict 客户端

功能: 发起请求,接收结果
"""

from socket import *
import sys
import getpass

# 服务器地址
ADDR = ('127.0.0.1',8888)
s = socket()
s.connect(ADDR)

# 注册功能
def do_register():
    while True:
        name = input("User:")
        pwd = getpass.getpass()
        pwd1 = getpass.getpass("Again:")
        if pwd != pwd1:
            print("两次密码不一致！")
            continue
        if (' ' in name) or (' ' in pwd):
            print("用户名或密码不能含有空格")
            continue

        msg = "R %s %s"%(name,pwd)
        s.send(msg.encode()) # 发送请求
        data = s.recv(128).decode() # 反馈
        if data == 'OK':
            print("注册成功")
            login(name)
        else:
            print("注册失败")
        return

# 登录
def do_login():
    name = input("User:")
    passwd = getpass.getpass()

    msg = "L %s %s"%(name,passwd)
    s.send(msg.encode())  # 发请求
    data = s.recv(128).decode() # 得到反馈
    if data == 'OK':
        print("登录成功")
        login(name)
    else:
        print("登录失败")

# 登录后的二级界面
def login(name):
    while True:
        print("""
        ==============%s Query ============
          1.查单词     2.历史记录     3.注销
        ===================================
        """%name)
        cmd = input("选项(1,2,3):")
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_history(name)
        elif cmd == '3':
            return  # 二级界面结束
        else:
            print("请输入正确命令")


# 搭建网络
def main():
    while True:
        print("""
        ========== Welcome ============
          1.注册     2.登录     3.退出
        ===============================
        """)
        cmd = input("选项(1,2,3):")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            sys.exit("谢谢使用")
        else:
            print("请输入正确命令")

if __name__ == '__main__':
    main()








```

## 数据库

```
"""
数据库处理操作
"""

import pymysql
import hashlib

# 对密码进行加密处理
def jm(passwd):
    salt = "^&5#Az$"
    hash = hashlib.md5(salt.encode())  # 生产加密对象
    hash.update(passwd.encode())  # 加密处理
    return hash.hexdigest()

class User:
    def __init__(self, host='localhost',
                 port = 3306,
                 user = 'root',
                 passwd = '123456',
                 charset='utf8',
                 database=None):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.database = database
        self.connect_db()

    # 链接数据库
    def connect_db(self):
        self.db = pymysql.connect(host = self.host,
                                  port = self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  database=self.database,
                                  charset=self.charset)

    # 创建游标对象
    def create_cursor(self):
        self.cur = self.db.cursor()

    def register(self,name,passwd):
        sql = "select * from user where name=%s"
        self.cur.execute(sql, [name])
        r = self.cur.fetchone()
        # 查找到说明用户存在
        if r:
            return False

        # 插入用户名密码
        sql = "insert into user (name,passwd) \
                values (%s,%s)"
        passwd = jm(passwd) # 加密处理
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    def login(self,name,passwd):
        passwd = jm(passwd)  # 加密处理
        sql = "select * from user \
                where name=%s and passwd=%s"
        self.cur.execute(sql, [name, passwd])
        r = self.cur.fetchone()
        # 查找到则登录成功
        if r:
            return True
        else:
            return False
```



## 加密处理

```
"""
加密处理
"""

import hashlib

passwd = input(">>")

# 加盐处理
salt = "*#06#"
hash = hashlib.md5(salt.encode())  # 生产加密对象

hash.update(passwd.encode()) # 加密处理

print(hash.hexdigest()) # 获取加密码
```





## 

# HTTPServer3.0

***参考代码：project/HTTPServer3.0***

## 功能 ： 

>httpserver部分
>
>>获取http请求 
>>解析http请求
>>将请求发送给WebFrame
>>从WebFrame接收反馈数据
>>将数据组织为Response格式发送给客户端

>WebFrame部分
>
>>从httpserver接收具体请求
>>根据请求进行逻辑处理和数据处理
>>将需要的数据反馈给httpserver

>特点 
>
>>采用httpserver和应用处理分离的模式,降低了耦合度
>>采用了用户配置文件的思路
>>webframe部分采用了模拟后端框架的处理方法

>技术点
>
>>httpserver部分需要与两端建立通信
>>webFrame部分采用多路复用接收并发请求
>>数据传递使用json格式


项目结构： 

``` 
           |--httpserver --HttpServer.py (主程序)      
           |             --config (httpserver配置)   
  project--|
           |
           |
           |--WebFrame   --WebFrame.py (主程序代码)
                         --static （存放静态网页）
                         --views.py （ 应用处理程序） 
                         --urls.py （存放路由）
                         --settings （框架配置）
```

>交互数据格式协议

```
httpserver-->webframe  {method:'GET',info:'/'}

webframe-->httpserver {status:'200',data:'ccccc'}
```



项目基础及工具
==========================


## GIT简介

1. 什么是GIT

> git是一个开源的分布式版本控制系统，用于高效的管理各种大小项目和文件。

2. 代码管理工具的用途

>* 防止代码丢失，做备份
>* 项目的版本管理和控制，可以通过设置节点进行跳转
>* 建立各自的开发环境分支，互不影响，方便合并
>* 在多终端开发时，方便代码的相互传输

3. git的特点

>* git是开源的，多在*nix下使用，可以管理各种文件
>* git是分布式的项目管理工具(svn是集中式的)
>* git数据管理更多样化，分享速度快，数据安全
>* git 拥有更好的分支支持，方便多人协调

4. git安装

> sudo apt-get install git

## GIT使用

![git结构](/home/tarena/.cache/.fr-3IqI7Y/╧ю─┐╫█║╧/img/git.jpeg)

### 基本概念

* 工作区：项目所在操作目录，实际操作项目的区域
* 暂存区: 用于记录工作区的工作（修改）内容
* 仓库区: 用于备份工作区的内容
* 远程仓库: 远程主机上的GIT仓库

>注意： 在本地仓库中，git总是希望工作区的内容与仓库区保持一致，而且只有仓库区的内容才能和其他远程仓库交互。

### 初始配置

>配置命令: git config

>* 配置所有用户： git config --system [选项]
>
>> 配置文件位置:  /etc/gitconfig

>* 配置当前用户： git config --global [选项]
>
>> 配置文件位置:  ~/.gitconfig

>* 配置当前项目： git config  [选项]
>
>> 配置文件位置:  project/.git/config

1. 配置用户名

```
e.g. 将用户名设置为Tedu
sudo git config --system user.name Tedu
```

2. 配置用户邮箱

```
e.g. 将邮箱设置为lvze@tedu.cn
git config --global user.email lvze@tedu.cn
```

3. 配置编译器

```
e.g. 配置编译器为pycharm
git config core.editor pycharm

```

4. 查看配置信息

```
git config --list
```

### 基本命令

1. 初始化仓库

> git  init 
> 意义：将某个项目目录变为git操作目录，生成git本地仓库。即该项目目录可以使用git管理

2. 查看本地仓库状态

> git  status
> 说明: 初始化仓库后默认工作在master分支，当工作区与仓库区不一致时会有提示。

3. 将工作内容记录到暂存区

> git add [files..]

```
e.g. 将 a ，b 记录到暂存区
git add  a b

e.g. 将所有文件（不包含隐藏文件）记录到暂存区
git add  *
```


####@扩展延伸
在Git项目中可以通过在项目的某个文件夹下定义.gitignore文件的方式，规定相应的忽略规则，用来管理当前文件夹下的文件的Git提交行为。.gitignore 文件是可以提交到公有仓库中，这就为该项目下的所有开发者都共享一套定义好的忽略规则。在.gitignore 文件中，遵循相应的语法，在每一行指定一个忽略规则。

```
.gitignore忽略规则简单说明

file            表示忽略file文件
*.a             表示忽略所有 .a 结尾的文件
!lib.a          表示但lib.a除外
build/          表示忽略 build/目录下的所有文件，过滤整个build文件夹；

```

4.取消文件暂存记录

>  git rm --cached [file] 

5. 将文件同步到本地仓库

> git commit [file] -m [message]
> 说明: -m表示添加一些同步信息，表达同步内容

```
e.g.  将暂存区所有记录同步到仓库区
git commit  -m 'add files'
```

6. 查看commit 日志记录

> git log
> git log --pretty=oneline

7. 比较工作区文件和仓库文件差异

> git diff  [file]

8. 将暂存区或者某个commit点文件恢复到工作区

> git checkout [commit] -- [file]
>
> * --是为了防止误操作，checkout还有切换分支的作用

9. 移动或者删除文件

> git  mv  [file] [path]
> git  rm  [files]
> 注意: 这两个操作会修改工作区内容，同时将操作记录提交到暂存区。

------------------------------

### 版本控制

1. 退回到上一个commit节点

> git reset --hard HEAD^
> 注意 ： 一个^表示回退1个版本，依次类推。当版本回退之后工作区会自动和当前commit版本保持一致

2. 退回到指定的commit_id节点

> git reset --hard [commit_id]

3. 查看所有操作记录

>git reflog
>注意:最上面的为最新记录，可以利用commit_id去往任何操作位置

4. 创建标签

>标签: 在项目的重要commit位置添加快照，保存当时的工作状态，一般用于版本的迭代。

> git  tag  [tag_name] [commit_id] -m  [message]
> 说明: commit_id可以不写则默认标签表示最新的commit_id位置，message也可以不写，但是最好添加。

```
e.g. 在最新的commit处添加标签v1.0
git tag v1.0 -m '版本1'
```

5. 查看标签

>git tag  查看标签列表
>git show [tag_name]  查看标签详细信息

6. 去往某个标签节点

> git reset --hard [tag]

7. 删除标签

> git tag -d  [tag]


### 保存工作区

1.  保存工作区内容

> git stash save [message]
> 说明: 将工作区未提交的修改封存，让工作区回到修改前的状态

2. 查看工作区列表

> git stash  list
> 说明:最新保存的工作区在最上面

3. 应用某个工作区

> git stash  apply  [stash@{n}]

4. 删除工作区

> git stash drop [stash@{n}]  删除某一个工作区
> git stash clear  删除所有保存的工作区


### 分支管理

>定义: 分支即每个人在原有代码（分支）的基础上建立自己的工作环境，单独开发，互不干扰。完成开发工作后再进行分支统一合并。

1. 查看分支情况

> git branch
> 说明: 前面带 * 的分支表示当前工作分支

2. 创建分支

> git branch [branch_name]
> 说明: 基于a分支创建b分支，此时b分支会拥有a分支全部内容。在创建b分支时最好保持a分支"干净"状态。

3. 切换工作分支

> git checkout [branch]
> 说明: 2,3可以同时操作，即创建并切换分支
>
> > git checkout -b [branch_name]

4. 合并分支

> git merge [branch]

> 冲突问题是合并分支过程中最为棘手的问题
>
> > 当分支合并时，原分支和以前发生了变化就会产生冲突
> > 当合并分支时添加新的模块（文件），这种冲突可以自动解决，只需自己决定commit操作即可。
> > 当合并分支时两个分支修改了同一个文件，则需要手动解决冲突。

5. 删除分支

> git branch -d [branch]  删除分支
> git branch -D [branch]  删除没有被合并的分支

![分支合并](/home/tarena/.cache/.fr-3IqI7Y/╧ю─┐╫█║╧/img/merge.png)

### 远程仓库

> 远程主机上的git仓库。实际上git是分布式结构，每台主机的git仓库结构类似，只是把别人主机上的git仓库称为远程仓库。

### GitHub介绍

>github是一个开源的项目社区网站，拥有全球最多的开源项目。开发者可以注册网站在github建立自己的项目仓库。

>网址： github.com

>代码管理工具：git

### 获取项目

* 在左上角搜索栏搜索想要的获取的项目

![](/home/tarena/.cache/.fr-3IqI7Y/╧ю─┐╫█║╧/img/1.png)

* 选择项目后复制项目git地址

![](/home/tarena/.cache/.fr-3IqI7Y/╧ю─┐╫█║╧/img/2.png)

* 在本地使用git clone方法即可获取

```
git clone https://github.com/xxxxxxxxx

```

> 注意： 获取到本地的项目会自动和github远程仓库建立连接。且获取的项目本身也是个git项目。

### 创建删除git仓库

* 点击右上角加号下拉菜单，选择新的仓库

![](/home/tarena/.cache/.fr-3IqI7Y/╧ю─┐╫█║╧/img/4.png)

* 填写相应的项目信息即可

* github仓库相对本地主机就是一个远程仓库 通过remote连接，如果需要输入密码输入github密码即可。连接后即可使用远程仓库操作命令操作。readme文件会被自动作为项目介绍

* 如果是在自己的仓库界面选择settings，在最后可以选择删除仓库。

![](/home/tarena/.cache/.fr-3IqI7Y/╧ю─┐╫█║╧/img/5.jpg)
![](/home/tarena/.cache/.fr-3IqI7Y/╧ю─┐╫█║╧/img/6.jpg)


### 远程仓库操作命令

所有操作在本地git仓库下进行

1. 添加远程仓库

```
git remote  add origin https://github.com/xxxxxxxxx

```

2. 查看连接的主机

>git remote
>注意: 一个git项目连接的远程主机名不会重复

3. 删除远程主机

>git remote rm [origin]

4. 将本地分支推送给远程仓库

将master分支推送给origin主机远程仓库，第一次推送分支使用-u表示与远程对应分支建立自动关联

```
git push -u origin  master

```

5. 推送代码到远程仓库

```
git push

```

6. 推送标签

> git push origin [tag]  推送本地标签到远程

> git push origin --tags  推送本地所有标签到远程

7. 推送旧的版本

> git push --force origin  用于本地版本比远程版本旧时强行推送本地版本

5. 删除远程分支和标签

> git branch -a  查看所有分支
> git push origin  [:branch]  删除远程分支
> git push origin --delete tag  [tagname]  删除远程仓库标签

7. 从远程获取代码

获取远程分支代码

> git pull 

将远程分支master拉取到本地，作为tmp分支

> git fetch origin  master:tmp  

> 区别
>
> > pull将远程内容直接拉取到本地，并和对应分支内容进行合并
> > fetch将远程分支内容拉取到本地，但是不会和本地对应分支合并，可以自己判断后再使用merge合并。


## 软件项目开发流程

```
需求分析 ----》 概要设计  ---》 项目计划 ----》详细设计---》编码测试 -----》项目测试 ----》调试修改 ---》项目发布----》后期维护

```

>需求分析 ： 确定用户的真实需求 
>
>>1. 确定用户的真实需求，项目的基本功能
>>2. 确定项目的整体难度和可行性分析
>>3. 需求分析文档，用户确认

>概要设计：对项目进行初步分析和整体设计
>
>>1. 确定功能模块
>>2. 进行可行性分析 搭建整体架构图
>>3. 确定技术思路和使用框架
>>4. 形成概要文档指导开发流程

>项目计划 ： 确定项目开发的时间轴和流程
>
>>1. 确定开发工作的先后顺序
>>2. 确定时间轴  ，事件里程碑
>>3. 人员分工 
>>4. 形成甘特图和思维导图等辅助内容

>详细设计 ： 项目的具体实现
>
>>1.形成详细设计文档 ： 思路，逻辑流程，功能说明，技术点说明，数据结构说明，代码说明

>编码测试 ： 按照预定计划实现代码编写，并且做基本检测
>
>>1. 代码编写
>>2. 写测试程序
>>3. 技术攻关

>项目测试 ： 对项目按照功能进行测试
>
>>1. 跨平台测试 ，使用测试
>>2. 根据测试报告进行代码修改
>>3. 完成测试报告

>项目发布
>
>>1.项目交付用户进行发布
>>2.编写项目说明文档

>后期维护
>
>>1.维护项目正常运转
>>2.进行项目的迭代升级

### 项目注意事项

* 按时完成项目工作和项目时间不足之间的冲突
* 项目实施人员之间的冲突

### 项目工具的使用

编写文档： word  ppt  excel  markdown   LaTex
项目流程图 ： Mindmanager  visio
项目管理 ： project
代码管理 ： svn   git

