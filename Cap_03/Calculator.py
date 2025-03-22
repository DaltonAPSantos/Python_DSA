#Pseudocódigo

# Inicio
# Exiba para o usuário que ele é bem vindo a calculadora.
# peça para o usuário digitar o primeiro numero.
# armazene o primeiro numero em uma variavel.
# peça para o usuario digitar o segundo numero.
# armazene o primeiro numero em uma variavel.
# peça para o usuario digitar qual tipo de operação ele quer executar, utilizando os caracteres (+-/*)
# armazene a operação em uma variavel.
# verifique qual o tipo de operação o usuário selecionou.
# realize a operação desejada pelo usuário.
# apresente o resultado.
# Fim

resultado = 0
print('Bem vindo a BasicCalculator!!!!!')
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

operator = input('Qual operação devo executar?(+-/*) ')

if operator == '+':
    resultado = num1 + num2

elif operator == '-':
     resultado = num1 - num2

elif operator == '/':
    if num2 == 0:
          print('Não é possível realizar divisão por Zero')
    else:
        resultado = num1 / num2

elif operator == '*':
     resultado = num1 * num2

else:
     print('Operação Inválida!')

print(resultado)

