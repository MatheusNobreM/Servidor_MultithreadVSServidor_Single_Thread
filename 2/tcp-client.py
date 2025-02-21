from socket import *
serverName = 'localhost'
serverPort = 12000

while True:
    print("Escolha o serviço: ")
    print("1 - Calculadora Simples (operações básicas: +, -, *, /)")
    print("2 - Calculadora Científica (operações avançadas: raiz quadrada)")
    print("Digite 'sair' para encerrar.")
    
    service_choice = input("Serviço (1 ou 2): ").strip()
    
    if service_choice.lower() == 'sair':
        print("Encerrando cliente.")
        break
    
    if service_choice == '1':
        operation = input("Digite a operação no formato: <operando operador operando> (ex: 5 + 3): ").strip()
        if not operation:  # Verifica se a entrada está vazia
            print("Entrada inválida. Tente novamente.")
            continue
        message = f"simples {operation}"
    elif service_choice == '2':
        operation = input("Digite a operação no formato: sqrt <operando> (ex: sqrt 16): ").strip()
        if not operation:  # Verifica se a entrada está vazia
            print("Entrada inválida. Tente novamente.")
            continue
        message = f"cientifica {operation}"
    else:
        print("Opção inválida. Tente novamente.")
        continue

    # Conexão com o servidor
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        clientSocket.send(message.encode('utf-8'))

        response = clientSocket.recv(1024).decode('utf-8')
        print(f"Resposta do servidor: {response}")
        clientSocket.close()
    except Exception as e:
        print(f"Erro ao conectar ao servidor: {e}")
