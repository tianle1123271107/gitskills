import socket
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s1.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s1.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s1.send(data)
    print(s1.recv(1024).decode('utf-8'))
s1.send(b'exit')
s1.close()



#关于编码总结一些：

'''
1  发送数据的时候  一般是用bytes的编码格式发送   因为数据要进行传输，或者保存到文件的时候，都是以bytes的形式展示     
2  接受数据的时候，相当于是从文件中读取，是在内存中运行的  所以要用Unicode的编码的str      接受的是bytes  所以查看的时候需要将其解码成Unicode
3  如果在需要把接受到消息发送出去  又要把Unicode转换成其他编码格式的byte   (test.decode('utf-8')).encode('utf-8')   
                 注意：bytes和str之间的转换都要用utf-8 因为utf-8包括了ascii编码   统一用utf-8     
'''