def somar_tudo(*numeros):
    total = 0
    for num in numeros:
         total += num
    return total
print(somar_tudo(1, 2, 3))       # Saída: 6
print(somar_tudo(10, 20, 30, 40)) # Saída: 100