temperatura = int(input("Qual a temperatura?: "))

if temperatura > 30:
    print("Está muito quente.")
elif temperatura > 20:
    print("Está quente.")
elif temperatura > 10:
    print("Está agradável")
else:
    print("Está frio")