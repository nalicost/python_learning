"""
                            http请求打印与响应格式
"""
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 10086))
s.listen(3)
conn, addr = s.accept()
print(conn.recv(4096).decode())
response = """HTTP/1.1 200 OK
Content-Type: text/html
200
<h1>Hello World</h1>
"""
conn.send(response.encode())
