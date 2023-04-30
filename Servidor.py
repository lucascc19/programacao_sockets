import socket

#Nome do Host e o valor da Porta
HOST = "LocalHost"
PORT = 5000

#Criando socket
Servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Iniciando a conexão
Servidor.bind((HOST,PORT))

#CONTROLE DE CONEXÃO
Servidor.listen()
