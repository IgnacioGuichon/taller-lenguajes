# Actividades introductorias

# ==============================
# Ejercicio 1:

anio = int(input("Ingresá un año de nacimiento: "))
print(f"Cumplirás 18 años en {anio + 18}.")
print(f"Cumplirás 21 años en {anio + 21}.")
print(f"Cumplirás 100 años en {anio + 100}.")
print()

# ==============================
# Ejercicio 2:

segundos = int(input("Ingresá una cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
restantes = segundos % 60
print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {restantes} segundos.")
print()

# ==============================
# Ejercicio 3:

numero = int(input("Ingresá un número: "))
for i in range(1,11):
    print(numero, "x", i, "=", numero * i)
print()

# ==============================
# Ejercicio 4:

n = int(input("Ingresá un número: "))
for i in range(1, n + 1):
    if i % 5 == 0:
        continue
    else:
        print(i)
print()

# ==============================
# Ejercicio 5:

precio = float(input("Ingresá el precio del producto: "))
total = 0
while precio != 0:
    total += precio
    precio = float(input("Ingresá el precio del producto: "))
    if precio == 0:
        break
print(f"El total acumulado es: {total}")
print()

# ==============================
# Ejercicio 6:

n = int(input("Ingresá un número: "))
multiplo = []
no_multiplo = []
for i in range(1, n + 1):
    if i % 5 == 0:
        multiplo.append(i)
    else:
        no_multiplo.append(i)
print("Múltiplos de 5:", multiplo)
print("No múltiplos de 5:", no_multiplo)
print()

# ==============================
# Ejercicio 7:

lista = input("Ingresá una lista de palabras: ")
palabras = lista.split(" ")
oracion = ""
for i in range(len(palabras)):
    if len(palabras[i]) > 3:
        oracion += palabras[i] + " "
print("Oración con palabras de más de 3 caracteres:", oracion)
print()

# ==============================