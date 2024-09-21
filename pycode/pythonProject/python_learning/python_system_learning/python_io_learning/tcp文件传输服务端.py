"""
                    tcp文件传输服务端
"""
import socket
sockFD = socket.socket()
sockFD.bind(('localhost', 10086))
sockFD.listen(10)
while True:
    try:
        print('waiting for connection...')
        connFD, addr = sockFD.accept()
        print('connection from', addr)
    except KeyboardInterrupt:
        sockFD.close()
        break
    except Exception:
        continue
    else:
        data = connFD.recv(1024)
        try:
            file_transport = open(f'{data.decode()}', 'wb')
            connFD.send(b'start')
        except FileNotFoundError:
            continue
    while True:
        data = connFD.recv(1024*1024)
        if not data:
            break
        file_transport.write(data)
    file_transport.close()
    connFD.close()
