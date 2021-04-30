import threading
import socket

host = '127.0.0.1' # local host
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)

# handle client connection
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break 
            
            
def receive():
    while True:
        client, addres = server.accept()
        print('connected with {}'.format(str(address)))
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)

        print('nickname: {}'.format(nickname))
        broadcast('an user joined')
        thread = threading.Thread(target = handle, args = (client,))
        thread.start()
        
        
                
        
