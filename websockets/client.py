from socket import*


host = gethostname()
port = 8000

cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))
        
        
while 1:
    msg =  input('Digite sua mensagem: ')
    cli.send(msg.encode())