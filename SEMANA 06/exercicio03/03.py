import socket #Importação das bibliotecas
import time
import sys

UDP_IP = "127.0.0.1" #Define o endereço UDP IP.
UDP_PORT = 5005 #Define a porta do UDP.
buf = 1024 #Define o tamanho do conteudo
file_name = sys.argv[1]


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Crie um novo socket usando a família de endereços, tipo de soquete e número de protocolo fornecidos.
sock.sendto(file_name, (UDP_IP, UDP_PORT)) #Conecta o UDP IP a porta e ao porta UDP.
print "Sending %s ..." % file_name #Printa o status do arquivo.

f = open(file_name, "r") #Abre o arquivo no modo read.
data = f.read(buf) #Abre o arquivo no modo de leitura com o tamanho do buffer.
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): #Manda o dado para o porta e o IP UDP.
        data = f.read(buf) #Atribui ao dado o conteudo do arquivo de leitura.
        time.sleep(0.02) # Give receiver a bit time to save

sock.close() #Fecha o socket.
f.close() #Fecha o arquivo.