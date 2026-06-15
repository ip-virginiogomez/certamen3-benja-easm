edad = int(input("Ingrese su edad"))
tarjeta = input("¿tiene tarjeta de socio? (si/no: ")
monto = int(input("ingrese el monto total de la compra: "))

if monto > 10000 and (edad > 60 or tarjeta == "si"): 
    descuento = monto * 0.15
    total_final = monto - descuento

    print("usted tiene descuento en un 15%")
    print(f"descuento: ${descuento}")
    print(f"total a pagar: ${total_final})
else: 
    print("no califica para el descuento)
    print(f"total a pagar: ${monto}")
