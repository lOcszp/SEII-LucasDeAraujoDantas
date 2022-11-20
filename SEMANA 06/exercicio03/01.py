import socket #Importação das bibliotecas
import sys

TCP_IP = "127.0.0.1" #Define o endereço TCP IP.
FILE_PORT = 5005 #Define a porta de transferencia de arquivos
DATA_PORT = 5006 #Define a porta de transferencia de dados
buf = 1024 #Define o tamanho do conteudo
file_name = sys.argv[1]


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crie um novo socket usando a família de endereços, tipo de soquete e número de protocolo fornecidos.
    sock.connect((TCP_IP, FILE_PORT)) #Conecta o TCP  a porta e ao IP
    sock.send(file_name) #Envia o arquivo
    sock.close() #Fecha o socket.

    print "Sending %s ..." % file_name #Printa na tela o status do envio

    f = open(file_name, "rb") #Abre o arquivo 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crie um novo socket usando a família de endereços, tipo de soquete e número de protocolo fornecidos.
    sock.connect((TCP_IP, DATA_PORT))  #Conecta o TCP  a porta e ao IP
    data = f.read() #Atribui a leitura do arquivo a uma variavel.
    sock.send(data) #Manda o dado.

finally:
    sock.close() #Fecha o socket.
    f.close() #Fecha o arquivo.