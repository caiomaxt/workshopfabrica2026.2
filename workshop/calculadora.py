def somar(a, b):
    return a + b    
def subtrair(a, b):
    return a - b    
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    print("Soma: ", somar(numero1, numero2))
elif opcao == 2:
    print("Subtração: ", subtrair(numero1, numero2))
elif opcao == 3:
    print("Multiplicação: ", multiplicar(numero1, numero2))
elif opcao == 4:
    print("Divisão: ", dividir(numero1, numero2))
else:
    print("Opção inválida!")