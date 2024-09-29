# calculadora.py

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

# Função principal separada para rodar a calculadora
def main():
    print("Calculadora Simples")
    print("Operações disponíveis: +, -, *, /")
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))
    resultado = calculadora(num1, num2, operador)
    print(f"Resultado: {num1} {operador} {num2} = {resultado}")

if __name__ == "__main__":
    main()
