#implement http server for retrive the data from server

import socket

server_host="0.0.0.0"
server_port=8000

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)


server_socket.bind((server_host,server_port))

server_socket.listen(1)

print(f"server listen to a port {server_port}")


    

while True:
    #wait for connection from client
    client_connection,address=server_socket.accept()

    #get client  request
    request=client_connection.recv(1024).decode()
    print(request)
    #parse http headers
    headers=request.split('\n')
    filename=headers[0].split()[1]
 
    #get content of file
    if filename == '/':
        filename='about.html'
    try:
        with open("index.html","r") as file:
            content=file.read()
            file.close()
        #send http response to client
        response="HTTP/1.0 200 OK\n\n" + content
    except FileNotFoundError:
        response="HTTP/1.0 404 OK\n\n File not found" 
    client_connection.sendall(response.encode())

    client_connection.close()
     
#close socket
server_socket.close()
