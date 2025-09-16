# CALCULADORA DE IMC COM CATEGORIZAÇÃO
# FAZER UM FORK E UM PULL REQUEST PARA ENTREGAR

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura**2)

print(imc)

if imc <= 18.5:
    print("abaixo do peso.")

elif imc <= 24.9:
    print("Peso noramal. ")

elif imc <= 29.9:
    print("Sobre peso. ")

elif imc <= 34.9:
    print("Obesidade Grau 1. ")

elif imc <= 39.9: 
    print("Obesidade Grau 2.") 

else:
    print("Obesidade grau 3. ")

