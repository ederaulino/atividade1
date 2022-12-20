s = str(input("Qual o seu sexo: F ou M? "))
p = float
a = float(input("Qual a sua altura? "))
if (s == "F"):
 p = (62.1*a) - 44.7
 print("Seu peso ideal é:", p)
elif (s == "M"):
    p = (72.7*a)-58
    print("Seu peso ideal é:", p)
else:
    print("Escreva um sexo válido")
    