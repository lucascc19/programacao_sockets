import socket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

def main():
    #Criando o socket do cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Fazendo conexão do cliente ao servidor
    cliente.connect((HOST, PORT))


if __name__ == '__main__':
    main()    