# Declarando variavel
texto = input('Qual seu nome?') 
print("Olá " + texto)
idade = int(input('Quantos anos você tem?'))

# Estrutura de decisão
if idade >= 18:
    print('A idade é maior ou igual a 18')
else:
    print('A idade é menor que 18')

# Estrutura de repetição

while idade > 18:
    if idade > 18 and idade < 30:
        print('Idade maior que 18 anos e menor que 30')
        idade = int(input('Qual sua idade?'))
texto = 'curso de lógica'
for x in texto:
    print(x)

# Lista
compras = ["banana", "maça", "uva"]

print(compras)
print(compras[1])

for x in compras: 
    print(x)

valores = ["texto", 2, True]
print(valores)