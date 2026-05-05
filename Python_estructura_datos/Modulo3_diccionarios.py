contactos = {
    "Ana":    "612345678",
    "Carlos": "698765432"
}

print(contactos["Ana"])  # Acceso directo por clave → 612345678
print(contactos.get("Elena", "No encontrado"))  # Evita error si la clave no existe


# CLAVES VÁLIDAS EN DICCIONARIOS (deben ser inmutables)

valido = {
    "nombre": "Juan",
    42: "respuesta",
    (1,2): "coord"
}


# CLAVES INVÁLIDAS (listas no son hashables)

# invalido = {[1,2]: "x"}  # ERROR: unhashable type: 'list'
Println ("------------------------------------------------------------------------------------")
colores = dict(rojo="#FF0000", verde="#00FF00", azul="#0000FF")


claves  = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Madrid"]

persona = {k: v for k, v in zip(claves, valores)}  # dict comprehension


# DICCIONARIO ANIDADO

usuario = {
    "nombre": "Miguel",
    "edad": 30,
    "direccion": {
        "calle": "Calle Mayor",
        "ciudad": "Madrid"
    }
}

ciudad = usuario["direccion"]["ciudad"]  # Acceso a diccionario dentro de otro → "Madrid"
Println ("------------------------------------------------------------------------------------")
califs = {"Mates": 85, "Historia": 72}

califs.update({"Inglés": 88, "Mates": 87, "Arte": 95})  # agrega y actualiza valores


vendido = califs.pop("Inglés")  # elimina "Inglés" y retorna su valor → 88
par_final = califs.popitem()    # elimina el último par insertado


contador = {}

contador.setdefault("hola", 0)   # si no existe la clave, la crea con valor 0
contador["hola"] += 1            # incrementa → {"hola": 1}


materias = ["Mates","Historia","Arte"]

notas = dict.fromkeys(materias, 0)  # crea diccionario con valor inicial 0


d1 = {"nombre":"Carlos","edad":28}
d2 = {"email":"c@e.com"}

unido = d1 | d2  # une diccionarios (Python 3.9+) → {"nombre":..., "edad":..., "email":...}
Println ("------------------------------------------------------------------------------------")
califs = {"Mates":85, "Historia":72, "Ciencias":90}

for asig, nota in califs.items():  # Recorre clave y valor del diccionario
    print(f"{asig}: {nota}")


# ORDEN ALFABÉTICO DE CLAVES

for asig in sorted(califs):  # sorted ordena las claves
    print(f"{asig}: {califs[asig]}")


# ELIMINAR MIENTRAS SE RECORRE (FORMA SEGURA)

d = {"a":1, "b":2, "c":3}

for k in list(d.keys()):  # se crea una copia de las claves
    if k == "b":
        del d[k]  # elimina sin romper el ciclo

print(d)  # {"a":1, "c":3}
Println ("------------------------------------------------------------------------------------")
# APLICAR DESCUENTO DEL 10% (DICT COMPREHENSION)

rebaja = {p: round(v * 0.9, 2) for p, v in precios.items()}


# FILTRAR PRODUCTOS DISPONIBLES

stock = {"manzanas":10, "peras":0, "naranjas":25}

disponibles = {f: c for f, c in stock.items() if c > 0}


# INVERTIR CLAVE-VALOR

original = {"a":1, "b":2, "c":3}

invertido = {v: k for k, v in original.items()}


# PORCENTAJE DEL TOTAL

gran_total = sum(precios.values())

pct = {p: round(v / gran_total * 100, 1) for p, v in precios.items()}
Println ("------------------------------------------------------------------------------------")

ventas_por_region = {
    "Norte": {"Q1": 12000, "Q2": 15000, "Q3": 13000, "Q4": 17000},
    "Sur": {"Q1": 10000, "Q2": 11000, "Q3": 9000, "Q4": 12000},
    "Este": {"Q1": 14000, "Q2": 16000, "Q3": 15000, "Q4": 18000},
    "Oeste": {"Q1": 8000, "Q2": 9000, "Q3": 8500, "Q4": 9500},
}

def totales_por_region():
    return {region: sum(datos.values()) for region, datos in ventas_por_region.items()}

def region_maxima():
    totales = totales_por_region()
    return max(totales.items(), key=lambda x: x[1])

def ventas_por_trimestre():
    acumulado = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
    for datos in ventas_por_region.values():
        for trimestre, valor in datos.items():
            acumulado[trimestre] += valor
    return acumulado

def porcentajes():
    totales = totales_por_region()
    gran_total = sum(totales.values())
    return {region: (valor / gran_total) * 100 for region, valor in totales.items()}

def reporte():
    totales = totales_por_region()
    porcent = porcentajes()
    ordenado = sorted(totales.items(), key=lambda x: x[1], reverse=True)

    print("\nREPORTE DE VENTAS")
    for region, total in ordenado:
        print(f"{region}: {total} ({porcent[region]:.2f}%)")

    region_mayor, valor = region_maxima()
    print(f"\nRegion con mayores ventas: {region_mayor} ({valor})")

    print("\nVentas por trimestre:")
    for trimestre, valor in ventas_por_trimestre().items():
        print(f"{trimestre}: {valor}")

def menu():
    while True:
        print("\n1. Ver totales por region")
        print("2. Region con mayores ventas")
        print("3. Ventas por trimestre")
        print("4. Ver porcentajes")
        print("5. Ver reporte completo")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione: "))
        except:
            print("Entrada invalida")
            continue

        if opcion == 1:
            for r, t in totales_por_region().items():
                print(r, t)

        elif opcion == 2:
            r, t = region_maxima()
            print(r, t)

        elif opcion == 3:
            for t, v in ventas_por_trimestre().items():
                print(t, v)

        elif opcion == 4:
            for r, p in porcentajes().items():
                print(f"{r}: {p:.2f}%")

        elif opcion == 5:
            reporte()

        elif opcion == 6:
            break

        else:
            print("Opcion invalida")

menu()