import socket
import random
import time

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024
MIN_CASAS = 1
MAX_CASAS = 30

def main():
    while True:
      #Criando o socket do cliente
      cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      #Fazendo conexão do cliente ao servidor
      cliente.connect((HOST, PORT))

      #Gera um número inteiro com até 30 casas
      num_casas = random.randint(MIN_CASAS, MAX_CASAS)
      numero = random.randint(10**(num_casas-1), 10**num_casas-1)

      #Envia o número para o servidor
      cliente.send(str(numero).encode())

      #Recebe os dados do servidor
      dados = cliente.recv(BUFFER_SIZE)

      #Converte os dados em uma string e adiciona a mensagem FIM
      resposta = dados.decode() + '\nFIM\n'

      print('Resposta recebida: ', resposta)

      cliente.close()

      #Envia o número a cada 10 segundos
      time.sleep(10)


if __name__ == '__main__':
  main()    