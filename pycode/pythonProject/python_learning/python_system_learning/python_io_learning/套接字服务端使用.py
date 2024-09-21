"""
                套接字服务端流程熟悉
"""
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 1025))
sock.listen(10)
while True:
    print('waiting for connection...')
    try:
        conn, addr = sock.accept()
        print('connection from', addr)
    except KeyboardInterrupt:
        sock.close()
        break
    except Exception as e:
        print(e)
        continue
    while True:
        recv_data = conn.recv(1024)
        print(recv_data.decode())
        if not recv_data:
            break
        send_data = input('message:>')
        n = conn.send(send_data.encode())
        print(n)
    conn.close()
