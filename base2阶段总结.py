数据结构

   * 逻辑结构
	表示数据之间的抽象关系（如邻接关系、从属关系等），按每个元素可能具有的直接前趋数和直接后继数将逻辑结构分为“线性结构”和“非线性结构”两大类。

   * 存储结构
	逻辑结构在计算机中的具体实现方法,分为顺序存储方法、链接存储方法、索引存储方法、散列存储方法。

> 链表 （买房）
    1. 定义
        将线性表L=(a0,a1,......,an-1)中各元素分布在存储器的不同存储块,称为结点,每个结点(尾节点除外)中都持有一个指向下一个节点的引用,这样所得到的存储结构为链表结构。
    2. 特点
        . 逻辑上相邻的元素 ai, ai+1,其存储位置也不一定相邻;
        . 存储稀疏,不必开辟整块存储空间。
        . 对表的插入和删除等运算的效率较高。
        . 逻辑结构复杂,不利于遍历。
    3. 程序实现 
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

>栈 (杯子装物)
    1. 定义
        栈是限制在一端进行插入操作和删除操作的线性表(俗称堆栈),允许进行操作的一端称为“栈顶”,另一固定端称为“栈底”,当栈中没有元素时称为“空栈”。
    2. 特点:
        栈只能在一端进行数据操作
        栈模型具有先进后出或者叫做后进先出的规律
'''
栈模型的顺序存储
重点代码
思路：
1、利用列表完成顺序存储，但是列表功能多，不符合栈模型特点
2、使用类将列表封装，提供符合栈特点的接口方法
'''
    # 自定义异常
    class StackError(Exception):
        pass
    # 顺序栈模型
    class Sstack:
        def __init__(self):
            # 开辟一个顺序存储的模型空间
            # 列表的尾部表示栈顶
            self._elems=[]  # 单下划线为受保护，自身和子类可用
        # 判断栈是否为空
        def is_empty(self):
            return self._elems == []

        # 入栈
        def push(self, val):
            self._elems.append((val))

        # 出栈
        def pop(self):
            if self.is_empty():
                raise StackError('Stack is empty')

            # 弹出一个值并返回
            # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

            return self._elems.pop()

        #查看栈顶元素
        def top(self):
            if self.is_empty():
                raise StackError('Stack is empty')
            return self._elems[-1] #倒数第一个

    if __name__ == '__main__':
        st=Sstack()
        st.push(10)
        st.push(20)
        st.push(30)
        st.top()
        st.pop()#

'''
lstack.py 栈的链式结构
重点代码
思路：
1、源于节点存储数据，建立节点关联
2、封装方法，入栈 出栈 栈空 栈顶元素
3、链表的开头作为栈顶（不需要每次遍历）
'''
    # 创建节点类
    class Node:
        def __init__(self, val, next=None):
            self.val=val
            self.next=next
    # 自定义异常
    class StackError(Exception):
        pass
    # 链式栈
    class LStack:
        def __init__(self):
            #标记顶位置
            self._top=None
        # 空栈
        def is_empty(self):
            return self._top is None
        # 入栈
        def push(self,val):
            self._top=Node(val,self._top)
        # 出栈
        def pop(self):
            if self._top is None:
                raise StackError('Stack is empty')
            # 弹出一个值并返回
            val=self._top.val
            self._top=self._top.next
            return val
        #查看栈顶元素
        def top(self):
            if self._top is None:
                raise StackError('Stack is empty')
            return self._top.val
    if __name__=='__main__':
        ls=LStack()
        ls.push(1)
        ls.push(2)
        ls.push(3)
        while not ls.is_empty():
            print(ls.pop())

>队列 （排队买票）
    1. 定义
        队列是限制在两端进行插入操作和删除操作的线性表,允许进行存入操作的一端称为“队尾”,允许进行删除操作的一端称为“队头”。
    2. 特点:
        队列只能在队头和队尾进行数据操作
        队列模型具有先进先出或者叫做后进后出的规律
'''
squeue.py 队列顺序存储
思路分析：
1、基于列表完成数据存储
2、通过封装功能完成队列基本行为
3、无论哪边做队头/队尾 都会在操作中存在内存移动
'''
    # 自定义异常
    class QueueError(Exception):
        pass
    # 队列操作
    class SQueue:
        def __init__(self):
            self._elems=[]
        # 判断队列是否为空
        def is_empty(self):
            return self._elems == []
        # 入队
        def enqueue(self, val):
            self._elems.append(val)
        # 出队
        def dequeue(self):
            if not self._elems:
                raise QueueError('Queue is empty')
            return self._elems.pop(0)  # 弹出第一个数据
    if __name__ == '__main__':
        sq=SQueue()
        sq.enqueue(1)
        while not sq.is_empty():
            print(sq.dequeue())

'''
lqueue.py 链式队列
思路分析：
1、基于链表:构建队列模型
2、链表的头作为队头，尾作为队尾
3、定义两个标记:标记队头和队尾
4、头和尾代表同一个无用节点时,队列为空
'''
    # 创建节点类
    class Node:
        def __init__(self, val, next=None):
            self.val=val
            self.next=next
    # 自定义异常
    class QueueError(Exception):
        pass
    class LQueue:
        def __init__(self):
            # front 队头 rear 队尾
            self.front=self.rear=Node(None)
        def is_empty(self):
            return self.front == self.rear
        # 入队
        def enqueue(self, val):
            self.rear.next=Node(val)
            self.rear=self.rear.next
        # 出队
        def dequeue(self):
            if self.is_empty():
                raise QueueError('Queue is empty')
            # front 是指向队头节点的前一个
            self.front=self.front.next
            return self.front.val  # 弹出第一个数据
    if __name__ == '__main__':
        lq=LQueue()
        lq.enqueue(11)
        print(lq.dequeue())

        >二叉树
            1. 定义
                二叉树(Binary Tree)是n(n≥0)个节点的有限集合,它或者是空集(n=0),或者是由一个根节点以及两棵互不相交的、分别称为左子树和右子树的二叉树组成。
                二叉树与普通有序树不同,二叉树严格区分左孩子和右孩子,即使只有一个子节点也要区分左右。
            2. 遍历
                先序遍历（根左右）: 先访问树根,再访问左子树,最后访问右子树;
                中序遍历（左根右）: 先访问左子树,再访问树根,最后访问右子树;
                后序遍历（左右根）: 先访问左子树,再访问右子树,最后访问树根;
                层次遍历: 从根节点开始,逐层从左向右进行遍历。

        >递归思想 （扩展）
            1. 递归函数调用的执行过程分为两个阶段
                递推阶段:从原问题出发,按递归公式递推从未知到已知,最终达到递归终止条件。
                回归阶段:按递归终止条件求出结果,逆向逐步代入递归公式,回归到原问题求解。
            2. 代码实现
                        """
                求一个数n的阶乘
                """
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
            3. 优缺点
                优点:递归可以把问题简单化,让思路更为清晰,代码更简洁
                缺点:递归因系统环境影响大,当递归深度太大时,可能会得到不可预知的结果

        >算法： 
            * 算法设计: 取决于选定的逻辑结构 
            * 算法实现: 依赖于采用的存储结构 

        >排序,查找

"""
冒泡排序
"""
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

"""
快速排序算法
"""
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

IO文件

   * 文件
        文本文件既可以用文本方式打开，也可以使用二进制方式打开
        二进制文件如果用文本方式打开，读写时会报错
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
    l = ['hello world\n','哈哈哈\n'] #将代码输出到一行,如果想换行需自己添加\n
    f.writelines(l)
    f.close()
"""
with.py
with语句生成文件对象
"""
    with open('4.txt') as f: # 以只读方式生成f对象
        data = f.read()
        print(data)
    # with语句块结束,f会被自动清理，代替close()

"""
运行程序时,写一个日志文件,格式如下
 1. Fri Aug 30 17:57:45 2019
 2. Fri Aug 30 17:57:46 2019
    ...
每隔一秒写一次,每个时间占一行
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

面向连接--基于TCP协议的数据传输

    1. 传输特征 ： 提供了可靠的数据传输，可靠性指数据传输过程中无丢失，无失序，无差错，无重复。 
        
    2. 实现手段 ： 在通信前需要建立数据连接，通信结束要正常断开连接。 

        > 三次握手（建立连接） 
        >>客户端向服务器发送消息报文请求连接 
        >>服务器收到请求后，回复报文确定可以连接 
        >>客户端收到回复，发送最终报文连接建立 
        客户端:client
        服务端:server
                        
        >四次挥手（断开连接） 
        >>主动方发送报文请求断开连接 
        >>被动方收到请求后，立即回复，表示准备断开 
        >>被动方准备就绪，再次发送报文表示可以断开 
        >>主动方收到确定，发送最终报文完成断开 

    3. 适用情况 ： 对数据传输准确性有明确要求，传数文件较大，需要确保可靠性的情况。比如：网页获取，文件下载，邮件收发。 

无连接--基于UDP协议的数据传输

    1. 传输特点 ： 不保证传输的可靠性，传输过程没有连接和断开，数据收发自由随意。 

    2. 适用情况 ： 网络较差(丢包,丢帧)，对传输可靠性要求不高。比如：网络视频，群聊，广播

socket 实现网络编程进行数据传输的一种技术手段

tcp套接字和udp套接字对比

    >流式套接字(SOCK_STREAM): 以字节流方式传输数据，实现tcp网络传输方案。(面向连接--tcp协议--可靠的--流式套接字) 

    >数据报套接字(SOCK_DGRAM):以数据报形式传输数据，实现udp网络传输方案。(无连接--udp协议--不可靠--数据报套接字) 

    >tcp套接字和udp套接字编程区别 
        >>1. 流式套接字是以字节流方式传输数据，数据报套接字以数据报形式传输 
        >>2. tcp套接字会有粘包，udp套接字有消息边界不会粘包 
        >>3. tcp套接字保证消息的完整性，udp套接字则不能 
        >>4. tcp套接字依赖listen accept建立连接才能收发消息，udp套接字则不需要 
        >>5. tcp套接字使用send，recv收发消息，udp套接字使用 sendto，recvfrom 

"""
tcp_server.py  tcp套接字服务端流程
重点代码
注意: 功能性代码,注重流程和函数使用
"""
    import socket
    # 创建tcp套接字对象
    sockfd = socket.socket(socket.AF_INET,
                        socket.SOCK_STREAM)
    # 设置端口立即重用
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # 绑定地址
    sockfd.bind(('0.0.0.0',9999))
    # 设置监听
    sockfd.listen(5)
    # 等待处理客户端连接请求
    while True:
        print("Waiting for connect...")
        try:
            connfd,addr = sockfd.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            # ctrl-c 退出程序
            print("Server exit")
            break
        except Exception as e:
            print(e)
            continue
        # 消息收发
        while True:
            data = connfd.recv(1024)
            # 如果data为空意味着客户端断开
            if not data:
                break
            print("Receive:",data.decode())
            # if data == b'Q':
            #     break
            n = connfd.send(b"Thanks")
            print('Send %d bytes'%n)
        connfd.close()
    # 关闭套接字
    sockfd.close()
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
    while True:
        msg = input("Msg:")
        if not msg:
            break
        sockfd.send(msg.encode()) #字节串
        # if msg == 'Q':
        #     break
        data = sockfd.recv(1024)
        print("From server:",data.decode())
    sockfd.close()

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

进程： 
    1. 定义 ： 程序在计算机中的一次运行。 
        >* 程序是一个可执行的文件，是静态的占有磁盘。 
        >* 进程是一个动态的过程描述，占有计算机运行资源，有一定的生命周期。 
    2.Linux查看进程ID ： ps -aux
        查看进程树： pstree
        状态查看命令 ： ps -aux  --> STAT列
    3.进程的运行特征 
        【1】 多进程可以更充分使用计算机多核资源 
        【2】 进程之间的运行互不影响，各自独立 
        【3】 每个进程拥有独立的空间，各自使用自己空间资源 

"""
基于fork的多进程编程，子进程共享全局变量值
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

僵尸进程 ： 子先退出，父没处理，浪费内存
'''
signal  信号方法处理僵尸进程
'''
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

进程：  Process
"""
管道通信-在内存中开辟管道空间，生成管道操作对象，多个进程使用同一个管道对象进行读写
注意：管道对象需在父进程中创建，子进程从父进程中获取
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

pool 进程池
    1.必要性 
        【1】 进程的创建和销毁过程消耗的资源较多 
        【2】 当任务量众多，每个任务在很短时间内完成时，需要频繁的创建和销毁进程。此时对计算机压力较大 
        【3】 进程池技术增加进程的重复利用，降低资源消耗。
    2.  原理 
        >创建一定数量的进程来处理事件，事件处理完进程不退出而是继续处理其他事件，直到所有事件全都处理完毕统一销毁。
# 使用进程池拷贝一个目录下所有的文件(普通文件)，实时打印拷贝的百分比进度。
    from multiprocessing import Pool,Queue
    import os
    q = Queue() # 消息队列
    # 拷贝文件
    def copy_file(file,old_dir,new_dir):
        fr = open(old_dir+file,'rb')
        fw = open(new_dir+file,'wb')
        while True:
            data = fr.read(1024)
            if not data:
                break
            n = fw.write(data) # 写入的字节数
            q.put(n) # 放到消息队列
    # 创建进程池
    def main():
        #  确定好源目录和备份目录
        path = "/home/tarena/"
        dir = input("输入要拷贝的文件目录:")
        old_dir = path + dir + '/' #源目录绝对路径
        new_dir = path + dir+"-备份/"
        os.mkdir(new_dir)
        # 要拷贝的文件列表
        file_list = os.listdir(old_dir)
        # 获取文件总大小
        total_size = 0
        for file in file_list:
            total_size += os.path.getsize(old_dir+file)
        print("总共大小：%d M"%(total_size/1024//1024))
        pool = Pool(4)
        # 添加进程池事件
        for file in file_list:
            pool.apply_async(copy_file,args=(file,old_dir,new_dir))
        pool.close()
        copy_size = 0 # 已经拷贝的大小
        while copy_size < total_size:
            copy_size += q.get() # 获取队列数量值
            print("拷贝了%.1f%%"%(copy_size/total_size*100))
        pool.join() #回收进程池中进程
    if __name__ == '__main__':
        main()

线程:  threading (同步互斥)
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

进程、线程的区别联系 
    >>区别联系 
        1. 两者都是多任务编程方式，都能使用计算机多核资源 
        2. 进程的创建删除消耗的计算机资源比线程多 
        3. 进程空间独立，数据互不干扰，有专门通信方法；线程使用全局变量通信 
        4. 一个进程可以有多个分支线程，两者有包含关系 
        5. 多个线程共享进程资源，在共享资源操作时往往需要同步互斥处理 
        6. 进程线程在系统中都有自己的特有属性标志，如ID,代码段，命令集等

    >>使用场景 
        1. 任务场景：如果是相对独立的任务模块，可能使用多进程，如果是多个分支共同形成一个整体任务可能用多线程 
        2. 项目结构：多种编程语言实现不同任务模块，可能是多进程，或者前后端分离应该各自为一个进程。 
        3. 难易程度：通信难度，数据处理的复杂度来判断用进程间通信还是同步互斥方法。 

协程：可以暂停执行的函数。 
    >优点 
        1. 协程完成多任务占用计算资源很少 
        2. 由于协程的多任务切换在应用层完成，因此切换开销少 
        3. 协程为单线程程序，无需进行共享资源同步互斥处理 
    >缺点 
        协程的本质是一个单线程，无法利用计算机多核资源 
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


* 进程 + 协程提高并发
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
        except KeyboardInterrupt asetsockopts e:
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

IO多路复用
    1. 定义 
        >同时监控多个IO事件，当哪个IO事件准备就绪就执行哪个IO事件。以此形成可以同时处理多个IO的行为，避免一个IO阻塞造成其他IO均无法执行，提高了IO执行效率。 

    2. 具体方案 
        >select方法 ： 
            优点：跨平台性好(windows  linux  unix)；
            缺点：效率一般，最多监控1024个ＩＯ
        >poll方法:　
            优点：监控ＩＯ数量没有限制　
            缺点：跨平台性一般(linux  unix)，效率一般
        >epoll方法: 　
            优点：监控ＩＯ没有限制，效率高　
            缺点：跨平台性差(linux)
    3.优缺点
        优点：资源消耗少
        缺点：本质是单进程，只能监听IO
"""
select tcp 服务端演示
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

"""
select tcp 客户端演示
"""
    from select import select
    from socket import *
    s = socket()
    s.bind(('127.0.0.1',8888))
    s.listen(3)
    f = open('12.txt')
    print(" 监控io ")
    rs,ws,xs = select([s],[s],[s])
    print("rlist:",rs)
    print("wlist:",ws)
    print("xlist:",xs)

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


避免死锁RLock
    * 数据比较复杂，多个线程操作共享数据需谨慎
    * 排查时，不要所有的锁一起看，应该按照一个一个的逻辑梳理

>聊天室
"""
chat room 服务端
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

>ftp 文件服务器
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
"""
ftp 文件服务 ，客户端
"""
    from socket import *
    import sys

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
            else:
                print("请输入正确命令!")

    if __name__ == '__main__':
        main()

>httpserver2.0
"""
httpserver 2.0 文件服务器 服务端
env: python3.6
io多路复用 
1. 主要功能 ： 
    【1】 接收客户端（浏览器）请求 
    【2】 解析客户端发送的请求 
    【3】 根据请求组织数据内容 
    【4】 将数据内容形成http响应格式返回给浏览器 
2. 升级点 ： 
    【1】 采用IO并发，可以满足多个客户端同时发起请求情况 
    【2】 做基本的请求解析，根据具体请求返回具体内容，同时满足客户端简单的非网页请求情况 
    【3】 通过类接口形式进行功能封装 
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

>httpserver3.0
"""
cookie
"""

    json ： 数据格式 "{'xxx':'abc'}"  "[1,2,3,4]"

    import json

    json.dumps(dict/list)  将字典或者列表转换为json格式

    json.loads(json)  将json数据解析为Python类型


    cookie

    让程序后台运行

    1. 程序第一行加解释器路径
        #! /usr/bin/env python3

    2. 设置程序的可执行权限
        chmod 774 httpserer.py

    3. 执行的时候后面加 &
        ./httpserver.py  &

    4. 如果想让程序在任意目录下都可以执行可以添加到/usr/bin下

        cd /usr/bin
        sudo  ln -s /home/tarena/.../httpserver.py  http

"""
httpserver 3.0
获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端
"""
    #!/usr/bin/env python3
    from socket import *
    import sys
    from threading import Thread
    from config import *
    import re
    import json

    # 和frame进行交互
    def connect_frame(env):
        s = socket()
        try:
            # 链接webframe
            s.connect((frame_ip,frame_port))
        except:
            return
        data = json.dumps(env) # 转换为json
        s.send(data.encode()) # 发送请求
        data = s.recv(1024*1024*10).decode()
        try:
            data = json.loads(data) # {‘status’:200,'data':'c'}
            return data
        except:
            return

    class HTTPServer:
        def __init__(self):
            self.host = host
            self.port = port
            self.address = (host,port)
            # 创建套接字
            self.create_socket()
            self.bind()

        # 创建套接字
        def create_socket(self):
            self.sockfd = socket()
            self.sockfd.setsockopt(SOL_SOCKET,
                                SO_REUSEADDR,
                                DEBUG)

        # 绑定地址
        def bind(self):
            self.sockfd.bind(self.address)

        # 启动服务
        def serve_forever(self):
            self.sockfd.listen(5)
            print("Listen the port %d"%self.port)
            while True:
                connfd,addr = self.sockfd.accept()
                client = Thread(target=self.handle,
                                args = (connfd,))
                client.setDaemon(True)
                client.start()

        # 具体处理客户端请求
        def handle(self,connfd):
            request = connfd.recv(4096).decode()
            pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
            try:
                env = re.match(pattern,request).groupdict()
            except:
                connfd.close()
                return
            else:
                # 和frame进行交互
                response = connect_frame(env)
                if response:
                    self.send_response(connfd,response)

        # 组织http响应，发送给浏览器
        def send_response(self,connfd,response):
            # response->{'status':'200','data':'ccc'}
            if response['status'] == '200':
                data = "HTTP/1.1 200 OK\r\n"
                data += "Content-Type:text/html\r\n"
                data += '\r\n'
                data += response['data']
            elif response['status'] == '404':
                data = "HTTP/1.1 404 Not Found\r\n"
                data += "Content-Type:text/html\r\n"
                data += '\r\n'
                data += response['data']
            elif response['status'] == '500':
                pass
            connfd.send(data.encode())

    if __name__ == '__main__':
        httpd = HTTPServer()
        httpd.serve_forever() # 启动服务
"""
config.py  httpserver 的配置文件
包含所有用户配置
"""
    # [http 服务地址]
    host = '0.0.0.0'
    port = 8000

    # 是否在调试状态
    DEBUG = True

    # webframe地址
    frame_ip = '127.0.0.1'
    frame_port = 8080

"""
webframe.py
模拟网站的后端应用行为
从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""
    #!/usr/bin/env python3
    from socket import *
    import json
    from settings import *
    from multiprocessing import Process
    from urls import *


    frame_address = (frame_ip,frame_port)

    class Application:
        def __init__(self):
            self.sockfd = socket()
            self.sockfd.bind(frame_address)
            self.sockfd.setsockopt(SOL_SOCKET,
                                SO_REUSEADDR,
                                DEBUG)
        # 启动函数
        def start(self):
            self.sockfd.listen(5)
            print("Listen the port %d"%frame_port)
            while True:
                connfd,addr = self.sockfd.accept()
                p = Process(target=self.handle,args=(connfd,))
                p.daemon = True
                p.start()

        # 处理具体的数据
        def handle(self,connfd):
            request = connfd.recv(1024).decode()
            request = json.loads(request) #请求字典
            # request=>{'method':'GET','info':'XXXX'}
            if request['method'] == 'GET':
                if request['info'] == '/' or request['info'][-5:] == '.html':
                    response = self.get_html(request['info'])
                else:
                    response = self.get_data(request['info'])
            elif request['method'] == 'POST':
                pass
            # 将结果返回给httpserver
            try:
                response = json.dumps(response)
            except:
                connfd.close()
            else:
                connfd.send(response.encode())
                connfd.close()

        def get_html(self,info):
            if info == '/':
                filename = STATIC_DIR + '/index.html'
            else:
                filename = STATIC_DIR + info
            try:
                fd = open(filename)
            except Exception:
                with open(STATIC_DIR+'/404.html') as f:
                    return {'status':'404','data':f.read()}
            else:
                return {'status':'200','data':fd.read()}

        def get_data(self,info):
            for url,func in urls:
                if url == info:
                    return {'status':'200','data':func()}
            return {'status': '404', 'data': 'sorry'}


    if __name__ == '__main__':
        app = Application()
        app.start()
"""
settings.py  webframe的配置文件
"""
    # address
    frame_ip = '0.0.0.0'
    frame_port = 8080

    # DEBUG
    DEBUG = True

    # HTML DIR
    STATIC_DIR = './static'
'''
urls.py 表达了能够处理的请求列表
'''
    from views import *

    # 表达了能够处理的请求列表
    urls = [
        ('/time',show_time),
        ('/guonei',guonei),
        ('/guoji',guoji)
    ]
'''
views.py 编写各种请求的处理方案
'''
    """
    编写各种请求的处理方案
    """

    def show_time():
        import time
        return time.ctime()

    def guonei():
        return "坚持党的领导"

    def guoji():
        return "反对恐怖注意"


>在线词典
'''
项目开发流程
'''
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
