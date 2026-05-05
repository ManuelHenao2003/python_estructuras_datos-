# BUCLE TRADICIONAL

cuadrados = []
for n in range(10):
    cuadrados.append(n**2)  # Eleva al cuadrado cada número


# LIST COMPREHENSION (más corto y limpio)

cuadrados = [n**2 for n in range(10)]  
# Resultado → [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# LIST COMPREHENSION CON FILTRO

pares = [n for n in range(10) if n % 2 == 0]
# Solo números pares → [0, 2, 4, 6, 8]


# TRANSFORMACIÓN DE DATOS

celsius = [0, 10, 20, 30, 40]

fahr = [(9/5) * t + 32 for t in celsius]
# Conversión de Celsius a Fahrenheit


# EXTRACCIÓN DE DATOS DESDE DICCIONARIOS

usuarios = [
    {"nombre":"Ana","edad":28},
    {"nombre":"Carlos","edad":35}
]

nombres = [u["nombre"] for u in usuarios]
# Resultado → ['Ana','Carlos']
Println ("------------------------------------------------------------------------------------")
# DICCIONARIOS POR COMPREHENSION

# CUADRADOS
cuadrados = {n: n**2 for n in range(5)}
# Resultado → {0:0, 1:1, 2:4, 3:9, 4:16}


# FILTRAR STOCK DISPONIBLE
stock = {"manzanas":10,"platanos":3,"naranjas":25,"peras":0}

disponibles = {f: c for f, c in stock.items() if c > 0}
# Solo productos con existencia > 0


# INVERTIR DICCIONARIO (clave ↔ valor)

original = {"a":1, "b":2, "c":3}

invertido = {v: k for k, v in original.items()}
# Resultado → {1:"a", 2:"b", 3:"c"}


# DESDE LISTA DE DICCIONARIOS

estudiantes = [
    {"id":1,"nombre":"Ana"},
    {"id":2,"nombre":"Carlos"}
]

id_nombre = {e["id"]: e["nombre"] for e in estudiantes}
# Resultado → {1:"Ana", 2:"Carlos"}
Println ("------------------------------------------------------------------------------------")
# SET COMPREHENSION

# ELIMINAR DUPLICADOS CON TRANSFORMACIÓN
numeros = [1,2,2,3,4,3,5,5,1]

unicos = {n for n in numeros}
# Elimina duplicados automáticamente → {1,2,3,4,5}


# INICIALES ÚNICAS
palabras = ["manzana","banana","mango","mora","naranja"]

iniciales = {p[0] for p in palabras}
# Toma la primera letra de cada palabra → {'m','b','n'}


# VOCALES ÚNICAS EN UN TEXTO
texto = "python es un lenguaje versátil"

vocales = {l for l in texto.lower() if l in "aeiou"}
# Extrae solo vocales sin repetir


# FILTRO + TRANSFORMACIÓN
pares_cuad = {n**2 for n in range(10) if n % 2 == 0}
# Cuadrados de números pares → {0, 4, 16, 36, 64}
Println ("------------------------------------------------------------------------------------")
ventas = [
    {"producto":"laptop",  "unidades":20, "precio":800},
    {"producto":"teclado", "unidades":50, "precio":25},
    {"producto":"mouse",   "unidades":30, "precio":15},
    {"producto":"monitor", "unidades":10, "precio":200}
]

# LIST COMPREHENSION: VALOR TOTAL POR PRODUCTO
valor_por_producto = [i["unidades"] * i["precio"] for i in ventas]
# Resultado → [16000, 1250, 450, 2000]


# LIST COMPREHENSION CON FILTRO: PRODUCTOS DE ALTO VALOR
alto_valor = [
    i["producto"] for i in ventas
    if i["unidades"] * i["precio"] > 1000
]
# Resultado → ['laptop','teclado','monitor']


# DICT COMPREHENSION: PRODUCTO → VALOR TOTAL
resumen = {
    i["producto"]: i["unidades"] * i["precio"]
    for i in ventas
}


# TOTAL GENERAL
gran_total = sum(valor_por_producto)
# Resultado → 19700
Println ("------------------------------------------------------------------------------------")
# LIST COMPREHENSION: SIMPLE, LEGIBLE Y EFICIENTE

cuadrados = [n**2 for n in range(100)]
# Genera una lista de cuadrados del 0 al 99


# GENERADORES: AHORRO DE MEMORIA (NO GUARDA TODO EN RAM)

gen = (n**2 for n in range(1_000_000))
primero = next(gen)  # Calcula solo el primer valor cuando se necesita


# CUÁNDO USAR BUCLE TRADICIONAL

resultados = []

for item in datos:
    if item["activo"]:                 # condición 1
        valor = calcular(item)         # procesamiento
        if valor > umbral:             # condición 2
            resultados.append(transformar(valor))
# En casos con mucha lógica, el bucle es más claro que una comprehension
Println ("------------------------------------------------------------------------------------")

ventas = [
    {"nombre": "Laptop", "unidades": 3, "precio": 1200, "categoria": "Tecnologia"},
    {"nombre": "Mouse", "unidades": 10, "precio": 25, "categoria": "Accesorios"},
    {"nombre": "Teclado", "unidades": 5, "precio": 60, "categoria": "Accesorios"},
    {"nombre": "Monitor", "unidades": 2, "precio": 300, "categoria": "Tecnologia"},
    {"nombre": "Audifonos", "unidades": 4, "precio": 45, "categoria": "Audio"},
]

def calcular_valores():
    valores = [(p["nombre"], p["unidades"] * p["precio"]) for p in ventas]
    for nombre, valor in valores:
        print(nombre, valor)

def productos_mayores():
    resultado = [p["nombre"] for p in ventas if p["unidades"] * p["precio"] > 1000]
    print(resultado)

def producto_info():
    info = {
        p["nombre"]: {
            "valor": p["unidades"] * p["precio"],
            "unidades": p["unidades"]
        }
        for p in ventas
    }
    print(info)

def ranking_premium():
    ranking = {
        p["nombre"]: p["unidades"] * p["precio"]
        for p in ventas if p["precio"] > 50
    }
    ordenado = dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True))
    print(ordenado)

def sets_info():
    categorias = {p["categoria"] for p in ventas}
    baratos = {p["nombre"] for p in ventas if p["precio"] <= 50}
    print("Categorias:", categorias)
    print("Baratos:", baratos)

def resumen():
    resumen_formateado = [
        f'{p["nombre"]}: {p["unidades"] * p["precio"]}'
        for p in ventas
    ]
    gran_total = sum(p["unidades"] * p["precio"] for p in ventas)

    for linea in resumen_formateado:
        print(linea)
    print("Total:", gran_total)

def menu():
    while True:
        print("\n1. Valor total por producto")
        print("2. Productos con valor > 1000")
        print("3. Producto info")
        print("4. Ranking premium")
        print("5. Sets (categorias y baratos)")
        print("6. Resumen total")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione: "))
        except:
            print("Entrada invalida")
            continue

        if opcion == 1:
            calcular_valores()
        elif opcion == 2:
            productos_mayores()
        elif opcion == 3:
            producto_info()
        elif opcion == 4:
            ranking_premium()
        elif opcion == 5:
            sets_info()
        elif opcion == 6:
            resumen()
        elif opcion == 7:
            break
        else:
            print("Opcion invalida")

menu()