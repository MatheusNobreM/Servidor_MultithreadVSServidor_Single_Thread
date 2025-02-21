from Calc import Calc
from TCPserver import TCPserver
from TCPclient import TCPClient
import threading

# Função de processamento da requisição
def process_request(request: str) -> str:
    parts = request.split()
    if len(parts) != 3:
        return "Erro: formato inválido"

    try:
        op1, operator, op2 = parts
        op1, op2 = float(op1), float(op2)

        if operator == '+':
            result = Calc.add(op1, op2)
        elif operator == '-':
            result = Calc.sub(op1, op2)
        elif operator == '*':
            result = Calc.mult(op1, op2)
        elif operator == '/':
            result = Calc.div(op1, op2)
        else:
            return "Erro: Operador inválido"

        return str(result)
    except Exception as e:
        return f"Erro: {e}"

# Função para iniciar o servidor
def start_server():
    server = TCPserver(1200)
    server.start(process_request)

# Função principal para interação com o cliente
if __name__ == "__main__":
    # Inicia o servidor em uma thread separada
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Aguarda um momento para garantir que o servidor esteja escutando
    input("Pressione Enter para iniciar o cliente e enviar uma operação para o servidor...")

    # Configuração do cliente
    client = TCPClient("localhost", 1200)
    client.connect()

    # Solicita a operação matemática ao usuário
    user_input = input("Digite a operação (ex: 10 + 20): ")
    
    # Envia a requisição e recebe a resposta
    client.sendRequest(user_input)
    
    # Altere para usar getResponse com "R" maiúsculo
    response = client.getResponse()
    print(f"Resposta do servidor: {response}")

    # Fecha a conexão do cliente
    client.close()
