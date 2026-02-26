km = int(input ("Digite a distancia em quilômetros(Km)"))
kg = int(input ("Digite o peso do pacote em quilogramas(Kg)"))

if km <= 100:
    valor_por_kg = 1
elif km <= 300:
    valor_por_kg = 1.5
else:
    valor_por_kg = 2

frete = kg * valor_por_kg

print("O valor do frete é de R$",frete)

