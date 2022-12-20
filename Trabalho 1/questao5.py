média = float
n1= float(input("Qual o valor da sua primeira nota? "))
n2= float(input("Qual o valor da sua segunda nota? "))
n3= float(input("Qual o valor da sua terceira nota? "))
n4= float(input("Qual o valor da sua quarta nota? "))
média = (n1+n2+n3+n4)/4
if média>=5:
    print("Aprovado com a média:", média)
else:
    print("Reprovado com a média", média)