def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
   
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")
if(imc < 18.5):
    print("Você está abaixo do peso normal.")
    print("Procure ajuda")
elif(imc >= 18.5 and imc <= 24.9):
    print("Você está com peso normal.")
    print("Você está com um peso saudável")
elif(imc >= 25.0 and imc <= 29.9):
    print("Você está com excesso de peso.")
    print("Procure ajuda")
elif(imc >= 30.0 and imc <= 34.9):
    print("Você está com obesidade grau 1.")
    print("Procure mais atendimentos médicos")
elif(imc >= 35.0 and imc <= 39.9):
    print("Você está com obesidade grau 2.")
    print("Procure ajuda urgente")
else:
    print("Você está com obesidade grau 3.")
    print("EMERGÊNCIA!!! Procure ajuda urgentemente.")