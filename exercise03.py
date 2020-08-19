from socket import *

s=socket()
s.bind(("0.0.0.0",9999))
s.listen(5)

c,addr=s.accept()
data=c.recv(1024*10)
print(data.decode())

html="HTTP/1.1 200 OK\r\n"
html+="Content-Type:text/html\r\n"
html+="\r\n"
with open("python.html") as f:
    html+=f.read()

# html="""HTTP/1.1 200 OK
# Content-Type:text/html
#
# This is a test
# """

c.send(html.encode())

c.close()
s.close()

