import socket #importação da bibliotecas
import threading

HEADER = 64 #Tamanho do conteúdo.
PORT = 5050 #Número da porta.
SERVER = socket.gethostbyname(socket.gethostname()) #Cria uma variavel que retorna o o endereço IP para o host.
ADDR = (SERVER, PORT) #Associa a variavel Endereço IP e a porta.
FORMAT = 'utf-8' #Escolha do formato (Codificação Binária).
DISCONNECT_MESSAGE = "!DISCONNECT" #Mensagem de desconexão.

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crie um novo socket usando a família de endereços, tipo de soquete e número de protocolo fornecidos.
server.bind(ADDR) #Vincula-o a um IP e porta específicos para que possa ouvir solicitações de entrada nesse IP e porta.

def handle_client(conn, addr): #Função que lida com o client.
    print(f"[NEW CONNECTION] {addr} connected.") # Printa a string com o endereço definido anteriormente.

    connected = True 
    while connected: #Loop enquanto estiver conectado.
        msg_length = conn.recv(HEADER).decode(FORMAT) #Define o tamanho da mensagem decodificada e no header.
        if msg_length:
            msg_length = int(msg_length) #Casting do tamanho da mensagem para inteiro.
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE: # Se a mensagem for igual a mensagem de disconnect.
                connected = False #Define a variável para falso.

            print(f"[{addr}] {msg}") #Printa o endereço e a mensagem.
            conn.send("Msg received".encode(FORMAT)) #Manda a string após a mesnagem ser recebida (codificada).

    conn.close() #Fecha a conexão.
        

def start(): # Função para começar.
    server.listen() #"Escuta" o servidor.
    print(f"[LISTENING] Server is listening on {SERVER}") #Printa a escuta do servidor em qual servidor que ele se situa.
    while True:
        conn, addr = server.accept() #Define as variaveis baseadp na conbexão request de um TCP client.
        thread = threading.Thread(target=handle_client, args=(conn, addr)) #É um construtor de Thread.
        thread.start() #Inicia a thread.
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...") #Printa que o servidor está inciando.
start() #Inicia a thread.