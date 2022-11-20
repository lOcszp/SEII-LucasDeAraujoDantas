import socket #importação da bibliotecas

HEADER = 64 #Tamanho do conteúdo.
PORT = 5050 #Número da porta.
FORMAT = 'utf-8' #Escolha do formato (Codificação Binária).
DISCONNECT_MESSAGE = "!DISCONNECT" #Mensagem de desconexão.
SERVER = "192.168.1.26" #Endereço IP do servidor.
ADDR = (SERVER, PORT) #Associa a variavel Endereço IP e a porta.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crie um novo socket usando a família de endereços, tipo de soquete e número de protocolo fornecidos.
client.connect(ADDR) #Conecta o client ao endereço.

def send(msg): #Criação de uma função para mandar a mensagem.
    message = msg.encode(FORMAT) #Codifica a mensagem.
    msg_length = len(message) #É atribuida à variavel o tamanho da mensagem.
    send_length = str(msg_length).encode(FORMAT) #Tamanho da mensagem que já codificada.
    send_length += b' ' * (HEADER - len(send_length)) #Tamanho da mensagem que já tratada totalmente pronta para ser enviada.
    client.send(send_length) #O cliente manda o tamanho da mensagem tratada.
    client.send(message) #O cliente manda a mensagem.
    print(client.recv(2048).decode(FORMAT)) #Printar a mensagem recebida do client decodificada.


send("Hello World!") #Manda a string escolhida para o servidor.
input() #Função que permite ao usuário digitar uma entrada no cmd.
send("Hello Everyone!") #Manda a string escolhida para o servidor.
input() #Função que permite ao usuário digitar uma entrada no cmd.
send("Hello Tim!") #Manda a string escolhida para o servidor.

send(DISCONNECT_MESSAGE) #Manda a mesnagem de desxonexão para o servidor.