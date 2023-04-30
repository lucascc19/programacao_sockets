import socket
import random

#Nome do Host e o valor da Porta
HOST = "localhost"
PORT = 5000
BUFFER_SIZE = 1024

def main():
    #Criando socket
    servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #Iniciando a conexão
    servidor.bind((HOST,PORT))

    #CONTROLE DE CONEXÃO
    servidor.listen()

    print("Servidor pronto para receber conexão na Porta: ",PORT)

    while True:
        #Esperando conexão
        cliente,endereco = servidor.accept()
        print("Conectado em ",endereco)
        
        #Recebendo os dados enviados pelo cliente
        dados = cliente.recv(BUFFER_SIZE)
        
        #Convertendo os dados recebido em um número inteiro 
        numero = int(dados.decode())
        print("Número recebido: ",numero)
        tamanho = len(numero)
        
        if tamanho > 10:
            mensagem = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz',tamanho))
            cliente.send(mensagem.encode())
        else:
            if numero % 2 == 0:
                resposta = 'PAR'
            else:
                resposta = 'ÍMPAR'
            cliente.send(resposta.encode())
            print("Resposta enviada: ",resposta)

        cliente.close()

if __name__ == '__main__':
    main()

