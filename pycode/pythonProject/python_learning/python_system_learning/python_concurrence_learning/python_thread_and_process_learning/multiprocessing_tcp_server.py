"""
                                多进程实现多个客户端连接服务端
"""
import socket
import multiprocessing
import threading

ADDR = ('localhost', 10086)
PROCESS_LIST = []


def handle_accept(sock_server, sock_client):
    sock_server.close()
    while True:
        data = sock_client.recv(1024)
        print(data.decode())
        if not data:
            break
        sock_client.send(b'OK')
    sock_client.close()


def handle_zombie():
    while True:
        for item in range(len(PROCESS_LIST)):
            PROCESS_LIST[item].join(3)
            if not PROCESS_LIST[item].is_alive():
                del PROCESS_LIST[item]


if __name__ == '__main__':
    t1 = threading.Thread(target=handle_zombie, daemon=True)
    t1.start()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    while True:
        try:
            c, addr = s.accept()
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)
            continue
        print('Connected by', addr)
        p1 = multiprocessing.Process(target=handle_accept, args=(s, c), daemon=True)
        p1.start()
        PROCESS_LIST.append(p1)
        c.close()
