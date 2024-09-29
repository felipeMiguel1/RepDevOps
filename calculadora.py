# Função para realizar a operação
def calculadora(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro! Divisão por zero."
    else:
        return "Operador inválido!"

# Menu de operação
print("Calculadora Simples")
print("Operações disponíveis: +, -, *, /")

# Receber os números e o operador do usuário
num1 = float(input("Digite o primeiro número: "))
operador = input("Digite o operador (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Chamar a função de cálculo e exibir o resultado
resultado = calculadora(num1, num2, operador)
print(f"Resultado: {num1} {operador} {num2} = {resultado}")
