import socket #Importação das bibliotecas

TCP_IP = "127.0.0.1" #Define o endereço TCP IP.
FILE_PORT = 5005 #Define a porta de transferencia de arquivos
DATA_PORT = 5006 #Define a porta de transferencia de dados
timeout = 3 #Variavel com o tempo de espera.
buf = 1024 #Define o tamanho do conteudo


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crie um novo socket usando a família de endereços, tipo de soquete e número de protocolo fornecidos.
sock_f.bind((TCP_IP, FILE_PORT)) #Vincula-o a um IP e porta específicos para que possa ouvir solicitações de entrada nesse IP e porta.
sock_f.listen(1) #Escuta o socket.

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crie um novo socket usando a família de endereços, tipo de soquete e número de protocolo fornecidos.
sock_d.bind((TCP_IP, DATA_PORT)) #Vincula-o a um IP e porta específicos para que possa ouvir solicitações de entrada nesse IP e porta.
sock_d.listen(1) #Escuta o socket.


while True:
    conn, addr = sock_f.accept() #Define as variaveis baseadp na conbexão request de um TCP client.
    data = conn.recv(buf) #Atribui a variavel o dado.
    if data:
        print "File name:", data
        file_name = data.strip() #Remove os espaços do dado.

    f = open(file_name, 'wb') #Abre o arquivo no modo de escrita

    conn, addr = sock_d.accept() #Atribui as duas variaveis à aceitação do socket.
    while True:
        data = conn.recv(buf) #Atribui a variavel o dado.
        if not data:
            break
        f.write(data) #Escreve no arquivo o dado.

    print "%s Finish!" % file_name #Printa o status do arquivo.
    f.close() #Fecha o arquivo.