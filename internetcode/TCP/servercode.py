# 服务器
'''
和客户端编程相比，服务器编程就要复杂一些。

服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。

所以，服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。由于服务器会有大量来自客户端的连接，所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。
一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。

但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。

我们来编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。'''

import socket
import threading
import time
# 首先，创建一个基于IPv4和TCP协议的Socket对象：
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#设置服务器地址和访问端口
s.bind(('127.0.0.1',9999))
#调用listen()方法来监听端口  传入的参数指定等待连接的最大数量：
s.listen(5)
print('wating for connecting')
# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
def tcplink(sock,addr):                                        #而sock返回的是服务器和客户端连接的scoket，返回的不是客户端的scoket，也就是说这个scoket是服务器的scoket，是与客户端连接之后建立的
    print('Accept new connection from %s:%s...' % addr)  #addr是指服务器和客户端连接之后返回的客户端的地址和端口
    sock.send(b'Welcome!')#相当于给连接的这个客户端 发送信息
    while True:
        data=sock.recv(1024)#接受客户端发送的信息
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))#把客户端接受的信息加上'hello'再发送出去
                                                                            # 这里send方法 先将接受到的的data（bytes）数据解码成Unicode的str  这样才能展示 hello ''这个字符串   ，然后现在看完之后  又需要发送了
                                                                            #所以又需要把Unicode的str类型通过encode编程成(‘utf-8’)编码格式的bytes来发送传输过去
    sock.close()
    print('Connection from %s:%s closed.' % addr)
# 连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接。

# 接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
while True:
    sock,addr=s.accept()
    print(sock)
    print(addr)
    #创建新的线程来处理TCP连接
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

# 需要注意的是，客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序。
# 用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。
# 同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。
