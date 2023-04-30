# Trabalho Prático - Programação de Sockets

Temos duas aplicações: <br>
➞ Aplicação cliente <br>
➞ Aplicação servidor

## Descrição
### Cliente
1. O cliente irá se conectar ao servidor;
2. Gerar um número inteiro com até 30 casas;
3. Enviar esse número para o servidor;
4. Receber do servidor e imprimir o valor recebido + a string "FIM".
5. Fecha a conexão
> Obs.: esse processo repete a cada 10 segundos

### Servidor
1. O servidor irá esperar a conexão de clientes;
2. Recebe o número;
3. Se o número tiver mais de 10 casas, gera e envia uma string do mesmo tamanho para o cliente;
4. Se for menor que 10, verifica se é par ou ímpar e envia "PAR" ou "ÍMPAR" para o cliente.

## Configuração de ambiente
### Windows
➞ Entrar na **Microsoft Store** e baixar **python 3.11** <br>
➞ Entrar no Visual Studio Code e baixar a extensão **Python**

### Linux
➞ No terminal, basta digitar o comando
`sudo apt install python3`

## Executando o código
Para executar o código no Windows e Linux basta digitar no terminal o comando `python nome_do_arquivo.py`.
No caso, será necessário estar executando tanto a aplicação cliente quanto servidor ao mesmo tempo, então será necessário abrir dois terminal.
> Obs.:executar primeiro o servidor e depois o cliente

## Resultado
![image](https://user-images.githubusercontent.com/62766998/235376855-3ad5e65c-3f62-448c-89ce-9cb8cc92181b.png)
