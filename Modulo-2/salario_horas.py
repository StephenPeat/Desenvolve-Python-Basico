salario_por_hora = 20.0
horas_trabalhadas = 40

salario_bruto = salario_por_hora * horas_trabalhadas

desconto_inss = salario_bruto * 0.10

desconto_sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - desconto_inss - desconto_sindicato

print("Salário semanal bruto: R$", salario_bruto)
print("Desconto INSS (10%): R$", desconto_inss)
print("Desconto Sindicato (5%): R$", desconto_sindicato)
print("Salário semanal líquido: R$", salario_liquido)
