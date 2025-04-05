# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

result = 0
persist = True

def soma(num1,num2): return num1 + num2

def subt(num1, num2): return num1 - num2

def mult(num1,num2): return num1 * num2

def div(num1,num2): return num1 / num2

while(persist):
    print("Selecione o número da operação desejada:\n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão\n")
    operator = int(input("Digite sua opção (1/2/3/4): "))
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    if operator == 1:
        result= soma(numero1,numero2)
        print(f"{numero1} + {numero2} = {result}")
    
    elif operator == 2:
        result = subt(numero1,numero2)
        print(f"{numero1} - {numero2} = {result}")
    
    elif operator == 3:
        result = mult(numero1,numero2)
        print(f"{numero1} * {numero2} = {result}")

    elif operator == 4:
        if numero2 == 0:
            print("Impossível realizar operação, divisão por zero! Digite um valor válido")
            continue
        else:
            result = div(numero1,numero2)
            print(f"{numero1} / {numero2} = {result}")
    else:
        print("Operação inválida, selecione uma operação válida")
        break

    cont = int(input("Deseja realizar uma nova operação? (1-Sim, 2-Não) "))
    
    if cont == 1:
        persist = True
    elif cont == 2:
        print("Até a próxima!!!")
        break
    else:
        print("Opção inválida até a próxima!!!")




