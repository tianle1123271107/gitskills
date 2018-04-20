import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'tianle',b'tianleer',b'tianlele']:#这里list中每个数据都要是bytes类型
    #直接发送数据  不需要连接   不需要调用connect()，,直接通过sendto()给服务器发数据：
    s.sendto(data,('127.0.0.1',9999))
    #接受来自服务器的数据
    print(s.recv(1024).decode('utf-8'))



#UDP协议服务器那边接受数据用recvfrom   需要明确数据是用那个地址发过来  返回的是发用的数据和发送数据的地址和端口号
#而UDP接受数据的时候  就不用recvfrom来接受  因为不需要知道服务器的地址


#接受来自服务器的数据的时候  因为数据是用来读取获得，所以需要把读取的数据解码成Unicode编码的str


'''
UDP与TCP使用类型  但是不需要建立连接， 此外，服务器绑定的UDP端口和TCP端口可以一致，也就是说UDP的9999端口和TCP的9999端口不冲突 可以一致
'''