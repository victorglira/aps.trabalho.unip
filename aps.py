

empresa=input("Digite o nome da sua Empresa: ")
funcionarios=int(input("Quantos colaboradores sua empresa possui?: "))
valor1=funcionarios*0.36 #valor que uma pessoa emite em 5 dias de trabalho com 8 horas por dia


while (funcionarios==0):#caso o usuario digite 0 na variavel funcionarios
    print("Valor incorreto, infome um valor valido!")
    funcionarios=int(input("Quantos colaboradores sua empresa possui?: "))
    print(f"A sua Emissão de carbono é:{valor1/1000:.2f}")


combustivel=int(input("Escolha entre: (1)-Etanol Hidratado, (2)-Gasolina Aditivada, (3)-Gasolina Comum, (4)-GLP, (5)-GNV, (6)-Oleo Disel ou (7)-Oleo Disel S10: "))
escolha=int(input("Digite: (1)-Informar o gasto mensal em R$ ou (2)- Para informar o gasto mensal em L: "))

if combustivel==1 and escolha==1: # se o usuario escolher etanol e informar em R$
    valor=float(input("Digite o Valor em R$: "))
    preco=(valor/3.45)*1,867 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é R$:{preco/1000:.2f}")


elif combustivel==1 and escolha==2: #se o usuario escolher etanol e informar em L
    valor=float(input("Digite o Valor em L: "))
    preco=(valor/3.45)*1.867 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")

if combustivel==2 and escolha==1: # se o usuario escolher gasolina aditivada e informar em R$
    valor=float(input("Digite o Valor em R$: "))
    preco=(valor/5.03)*2.28 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


elif combustivel==2 and escolha==2: #se o usuario escolher gasolina aditivada e informar em L
    valor=float(input("Digite o Valor em L: "))
    preco=(valor/5.03)*2.28 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


if combustivel==3 and escolha==1: # se o usuario escolher gasolina comum e informar em R$
    valor=float(input("Digite o Valor em R$: "))
    preco=(valor/4.74)*2.28 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


elif combustivel==3 and escolha==2:#se o usuario escolher gasolina comum e informar em L
    valor=float(input("Digite o Valor em L: "))
    preco=(valor/4.74)*2.28 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


if combustivel==4 and escolha==1:#se o usuario escolher glp e informar em R$
    valor=float(input("Digite o Valor em R$: "))
    preco=(valor/112,68)*2.747 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


elif combustivel==4 and escolha==2:#se o usuario escolher glp e informar em L
    valor=float(input("Digite o Valor em L: "))
    preco(valor/112.68)*2.747 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


if combustivel==5 and escolha==1: #se o usuario escolher gnv e informar em R$
    valor=float(input("Digite o Valor em R$: "))
    preco=(valor/5.12)*1.99 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


elif combustivel==5 and escolha==2:#se o usuario escolher gnv e informar em L
    valor=float(input("Digite o Valor em L: "))
    preco=(valor/5.12)*1.99 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


if combustivel==6 and escolha==1: #se o usuario escolher oleo disel e informar em R$
    valor=float(input("Digite o Valor em R$: "))
    preco=(valor/6.33)*3.2 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


elif combustivel==6 and escolha==2:#se o usuario escolher oleo disel e informar em L
    valor=float(input("Digite o Valor em L: "))
    preco(valor/6.33)*3.2 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")

    
if combustivel==4 and escolha==1:#se o usuario escolher oleo disel s10 e informar em R$
    valor=float(input("Digite o Valor em R$: "))
    preco=(valor/6.57)*3.2 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


elif combustivel==4 and escolha==2: #se o usuario escolher oleo disel s10 e informar em L
    valor=float(input("Digite o Valor em L: "))
    preco(valor/6.57)*3.2 # <<esse valor é o quanto esse tipo de combustivel emite de Co2
    print(f"A sua Emissão de carbono é:{preco/1000:.2f}")


energia=float(input("Qual é o custo mensal da conta de luz do escritório físico da sua empresa?"))
valor2=(energia/0.2727) # <<esse valor é o quanto kW emite de carbono em media
print(f"A sua Emissão de carbono é:{preco:.2f}")

total=print(f"O total que sua empresa emite de Co2 é:{valor1+valor2+preco/1000:.2f} Kg/T")
resultado=valor1+valor2+preco/1000
continuar=int(input("Digite: (1)-Para seguir para as propostas de credito de carbono/compra de arvores ou (2)-Para finalizar: "))
if continuar==1:
    escolha1=int(input("Digite: (1)-Cotar creditos de carbono ou (2)-Cotar compra de arvores: "))
    if escolha1==1:
        cotar1=resultado*66.66
        print(f"O valor total que deve ser pago para compra de credito de carbono é de R$:{cotar1:.2f}")
    if escolha1==2:
        cotar2=(resultado/7)*390
        print(f"O Valor que deve ser investido na compra de arvores é de R$:{cotar2:.2f}")
else:
    print("Caso deseje realizar o calculo novamente reinicie o programa!")












