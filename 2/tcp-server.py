import time
from socket import *
import threading

def handle_client(connectionSocket):
    try:
        request = connectionSocket.recv(1024).decode('utf-8')
        print(f"Requisição recebida: {request}")

        parts = request.split(maxsplit=1)
        if len(parts) < 2:
            response = "Erro: formato inválido. Use 'simples' ou 'cientifica' seguido da operação."
        else:
            service, operation = parts

            if service.lower() == 'simples':
                # simples
                operands = operation.split()
                if len(operands) != 3:
                    response = "Erro: formato inválido para calculadora simples. Use: <operando operador operando>"
                else:
                    opr1, opd, opr2 = operands
                    try:
                        opr1 = float(opr1)
                        opr2 = float(opr2)

                        if opd == '+':
                            res = opr1 + opr2
                        elif opd == '-':
                            res = opr1 - opr2
                        elif opd == '*':
                            res = opr1 * opr2
                        elif opd == '/':
                            if opr2 == 0:
                                response = "Erro: divisão por zero"
                            else:
                                res = opr1 / opr2
                        else:
                            response = "Erro: operador inválido"

                        if 'response' not in locals():
                            response = str(res)
                    except ValueError:
                        response = "Erro: operandos inválidos"
            
            elif service.lower() == 'cientifica':
                # científica
                operands = operation.split()
                if len(operands) != 2 or operands[0].lower() != 'sqrt':
                    response = "Erro: formato inválido para calculadora científica. Use: 'sqrt <operando>'"
                else:
                    try:
                        opr = float(operands[1])
                        if opr < 0:
                            response = "Erro: raiz quadrada de número negativo não é suportada"
                        else:
                            response = str(opr ** 0.5)
                    except ValueError:
                        response = "Erro: operando inválido"
            else:
                response = "Erro: serviço inválido. Use 'simples' ou 'cientifica'."
        
        # Enviar resposta ao cliente
        connectionSocket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Erro no processamento: {e}")
    finally:
        connectionSocket.close()

# Configuração do servidor
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print("O servidor está pronto para receber")
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket,)).start()
