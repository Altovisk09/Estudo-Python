compras = []
resp = 's'
while resp != "n":
    compras.append(input('Digite o item da Lista'))
    resp = input('Deseja continuar - s para Sim ou n para Não')
print(compras)
for x in compras:
    if x == "banana":
        print('encontrei a banana')
    else:
        print('não encontrei a banana')
