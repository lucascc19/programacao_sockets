import socket
import random
import time

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024

def main():
    while True:
      #Criando o socket do cliente
      cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      #Fazendo conexão do cliente ao servidor
      cliente.connect((HOST, PORT))

      numero = random.randint(1, 10**30)

      numero_convertido = str(numero)

      #Envia o número para o servidor
      cliente.send(numero_convertido.encode())

      dados = cliente.recv(BUFFER_SIZE)

      resposta = dados.decode() + 'FIM'

      print('Resposta recebida: ', resposta)

      cliente.close()

      time.sleep(10)


if __name__ == '__main__':
    main()    