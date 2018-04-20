'''
TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。

虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。
'''

import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.01',9999))
#创建scoket时，SOCK_DGRAM指定的这个scoket指定的协议是UDP  绑定端口和TCP是一样的  但是不要listen（）方法，而是直接接口来自客户端的数据
print('Bind UDP on 9999...')
while True:                                 #sendto(data,addr)  这里必须是两个参数   一个是需要传输的数据（以bytes类型发送）  一个是发送的服务器地址和端口号
    #接受数据
    data,addr=s.recvfrom(1024)
    print('Recvfrom from %s:%s'%addr)
    s.sendto(b'hello,%s'%data,addr)#这边发送数据 是以bytes类型发送的  也就是不是str类型  所以在客户端接受的时候  要进行解码成str 才能正常读取
    # t=threading.Thread(duoxiancheng,args=())
#recvfrom 方法 返回客户端发送的数据和地址和端口(addr),这样 服务器收到数据后，直接调用sendto()直接把数据用UDP发送给客户端、
# 注意这里省掉了多线程，因为这个例子很简单。
