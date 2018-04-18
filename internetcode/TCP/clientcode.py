#Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。
'''
客户端
大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。
举个例子，当我们在浏览器中访问新浪时，我们自己的计算机就是客户端，浏览器会主动向新浪的服务器发起连接。如果一切顺利，新浪的服务器接受了我们的连接，一个TCP连接就建立起来的，后面的通信就是发送网页内容了。
'''
# 所以，我们要创建一个基于TCP连接的Socket，可以这样做：
#导入socket库
import socket
#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#第一步   创建Socket对象时，AF_INET指定使用IPv4协议  SOCK_STREAM指定使用面向流的TCP协议  创建成功,但是还有进行连接
s.connect(('www.sina.com.cn',96))#第二步 答案是作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口。
'''connect的参数是一个tuple元祖，包括地址和端口号'''
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接受数据
buffer=[]
while True:
    #每次最多接受字节数
    d=s.recv(1024)
    if d:
        buffer.append(d)#接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。
    else:
        break
data=b''.join(buffer)
#当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了：
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#把接受的数据写进文件
with open('sanzhixiao.html','wb')as f:
    f.write(html)