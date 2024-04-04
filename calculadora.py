def calculadora(op, a, b):
    if op == 'adicao':
        return a + b
    elif op == 'subtracao':
        return a - b
    elif op == 'multiplicacao':
        return a * b
    elif op == 'divisao':
        if b == 0:
            return "impossível dividir por zero!"
        else:
            return a / b
    else:
        return "inválido"

print("Selecione a operação:")
print("- Adição")
print("- Subtração")
print("- Multiplicação")
print("- Divisão")

op = input("Digite a operação desejada (adicao / subtracao / multiplicacao / divisao): ")

val1 = float(input("Digite o primeiro número: "))
val2 = float(input("Digite o segundo número: "))

print("Resultado:", calculadora(op, val1, val2))
