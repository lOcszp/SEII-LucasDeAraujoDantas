
import socket #Importação das bibliotecas
import select

UDP_IP = "127.0.0.1" #Define o endereço UDP IP.
IN_PORT = 5005 #Define a porta do UDP.
timeout = 3 #Define o tempo de timeout.


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Crie um novo socket usando a família de endereços, tipo de soquete e número de protocolo fornecidos.
sock.bind((UDP_IP, IN_PORT)) #Vincula-o a um IP e porta específicos para que possa ouvir solicitações de entrada nesse IP e porta.

while True:
    data, addr = sock.recvfrom(1024) #Atribui o dado e o endereço o payload.
    if data:
        print "File name:", data #Printa o nome do arquivo.
        file_name = data.strip() #Elimina os espaços do data.

    f = open(file_name, 'wb') #Abre o arquivo como escrita.

    while True:
        ready = select.select([sock], [], [], timeout) #Lê a guarda 3 transferencias
        if ready[0]:
            data, addr = sock.recvfrom(1024) #Define o endereço e o dado a partir do payload.
            f.write(data) #Escreve no arquivo o dado.
        else:
            print "%s Finish!" % file_name #Printa o status do arquivo.
            f.close() #Fecha o arquivo.
            break