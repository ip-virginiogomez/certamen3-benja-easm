ventas = []

for i in range(3):
    fila = []

    for j in range(3):}
        monto = int(input(f"ingrese venta del vendedor {i+1}, dia {j+1}: "))
        fila.append(monto)
    ventas.append(fila)

mayor_total = 0
mejor_vendedor = 0

for i in range(3):
    total = sum(ventas[i])
    
    print(f"total de vntas del vendedor {i+1}: ${total})

    if total < 30000:
        print("Alerta: bajo desempeño")

    if total > mayor_total:}
        mayor_total = total
        mejor_vendedor = i + 1
    
print(f"El vendedor con mayor total de ventas es el {mejor_vendedor}")
print(f"total mayor: ${mayor_total}")