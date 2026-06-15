velocidades = []
for i in range(5): 
    velocidad = int(input(f"ingresa la velocidad {i+1}: "))
    velocidades.append(velocidad)
promedio = sum(velocidades) / len(velocidades)

maxima = max(velocidades)

print(f"Velocidad promedio: {promedio:2.f} km/h)
print(f"Velocidad maxima: {maxima} km/h)

dentro_limite = True

for velocidad in velocidades: 
    if velocidad < 60 or velocidad > 120:
        dentro_limite = False
    if velocidad > 140 or velocidad < 20:
        print("Advertencia velocidad peligrosa")

if dentro_limite: 
    print("Todas la velocidades estan dentro del limite")
else:
    print("hay velocidades fuera del limite")
