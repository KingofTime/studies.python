"""
Exercício 3

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta
a serem compradas e o preço total.
"""

print("#### LOJAS COLORAMAS ####")
print("Bem vindo ao nosso sistema de compra de tinta!")
area = float(input("Qual é o tamanho em metros quadrados da área que deseja pintar? "))

cobertura_por_litro = 3
cobertura_por_lata = 18 * cobertura_por_litro
custo_por_lata = 80.00

area_em_latas = area / cobertura_por_lata
custo_total = area_em_latas * custo_por_lata

print(f"Calculamos aqui que para sua área será necessário comprar {area_em_latas} latas de tinta, totalizando R$ {custo_total} reais.")