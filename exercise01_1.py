from socket import *

ADDR = ("127.0.0.1", 8888)  # 服务端地址

tcp_socket = socket()  # 默认值就是创建tcp套接字

tcp_socket.connect(ADDR)  # 发起链接 对应 accept

# 发送接受消息
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("Server:", data.decode())

tcp_socket.close()  # 关闭
