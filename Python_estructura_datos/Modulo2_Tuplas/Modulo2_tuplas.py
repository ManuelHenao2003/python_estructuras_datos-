coordenadas = (10, 20)

try:
    coordenadas[0] = 15  # No se puede modificar una tupla
except TypeError as e:
    print(f"Error: {e}")  # 'tuple' object does not support item assignment


# TUPLA CON ELEMENTOS MUTABLES

config = ("config_v1", [1, 2, 3])

config[1].append(4)  # La lista dentro de la tupla sí se puede modificar

print(config)  # ('config_v1', [1, 2, 3, 4])

Println ("------------------------------------------------------------------------------------")
# TUPLAS COMO CLAVES DE DICCIONARIO (SON INMUTABLES Y HASHABLES)

ubicaciones = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522, -118.2437): "Los Ángeles"
}

print(ubicaciones[(40.7128, -74.0060)])  # Nueva York


# LISTAS NO PUEDEN SER CLAVE EN DICCIONARIOS (NO SON HASHABLES)

try:
    d = {[40.71, -74.00]: "NY"}  # ERROR: las listas son mutables
except TypeError as e:
    print(f"Error: {e}")  # unhashable type: 'list'
Println ("------------------------------------------------------------------------------------")
numeros  = (1, 2, 3, 4, 5)

coords   = 10, 20, 30          # también es una tupla (empaquetado automático)

vacia    = ()                  # tupla vacía

singleton = (42,)              # tupla de un solo elemento (la coma es obligatoria)

desde_lista = tuple([1, 2, 3])     # convierte lista en tupla → (1, 2, 3)

desde_str   = tuple("Python")       # convierte string en tupla → ('P','y','t','h','o','n')

desde_rango = tuple(range(5))       # convierte rango en tupla → (0, 1, 2, 3, 4)

print(type((42)))    # <class 'int'>   → SIN coma NO es tupla
print(type((42,)))   # <class 'tuple'> → CON coma sí es tupla
Println ("------------------------------------------------------------------------------------")
datos = ("Python", 3.9, 2023, "Tuplas")

print(datos[0])    # Accede al primer elemento → "Python"
print(datos[-1])   # Accede al último elemento → "Tuplas"


nums = (0,1,2,3,4,5,6,7,8,9)

print(nums[2:6])   # Slicing desde índice 2 hasta antes de 6 → (2,3,4,5)
print(nums[::2])   # Saltos de 2 en 2 → (0,2,4,6,8)
print(nums[::-1])  # Invierte la tupla → (9,8,7,6,5,4,3,2,1,0)


t = (1, 2, 3, 2, 4, 2, 5)

print(t.count(2))  # Cuenta cuántas veces aparece 2 → 3
print(t.index(3))  # Devuelve la posición de 3 → 2
Println ("------------------------------------------------------------------------------------")
producto = ("Laptop XPS", 1299.99, "Dell")

nombre, precio, fabricante = producto  # desempaquetado de tupla

print(nombre)      # Laptop XPS
print(precio)      # 1299.99


a, b = 5, 10
a, b = b, a        # intercambio de valores (swap en una línea)

print(a, b)        # 10 5


numeros = (1, 2, 3, 4, 5)

primero, *resto = numeros        # primero=1, resto=[2,3,4,5]
primero, *medio, ultimo = numeros  # primero=1, medio=[2,3,4], ultimo=5
*iniciales, ultimo = numeros     # iniciales=[1,2,3,4], ultimo=5
Println ("------------------------------------------------------------------------------------")
datos = ("Juan","Pérez",35,"Madrid","Ingeniero")

nombre, _, edad, _, prof = datos  # _ se usa para ignorar valores

print(f"{nombre}, {edad}, {prof}")


estudiantes = [("Ana",22,9.5),("Carlos",20,8.7)]

for nombre, edad, nota in estudiantes:
    print(f"{nombre}: {nota}")  # desempaquetado en el bucle


def estadisticas(nums):
    return min(nums), max(nums), sum(nums)/len(nums)  # retorna múltiples valores

minima, maxima, promedio = estadisticas([4,7,2,9,5])  # desempaquetado del retorno

print(f"min={minima} max={maxima} avg={promedio:.2f}")
Println ("------------------------------------------------------------------------------------")


catalogo = (
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("The Matrix", "Wachowski", 1999, 8.7),
    ("Interstellar", "Christopher Nolan", 2014, 8.6),
    ("Titanic", "James Cameron", 1997, 7.8),
)

def mostrar_catalogo():
    for titulo, director, anio, puntuacion in catalogo:
        print(f"{titulo} | {director} | {anio} | {puntuacion}")

def buscar_por_director(nombre_director):
    return tuple(
        peli for peli in catalogo if peli[1].lower() == nombre_director.lower()
    )

def obtener_estadisticas():
    puntuaciones = tuple(p[3] for p in catalogo)
    return min(puntuaciones), max(puntuaciones), sum(puntuaciones) / len(puntuaciones)

def menu():
    while True:
        print("\n1. Ver catalogo")
        print("2. Buscar por director")
        print("3. Ver estadisticas")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione: "))
        except:
            print("Entrada invalida")
            continue

        if opcion == 1:
            mostrar_catalogo()

        elif opcion == 2:
            nombre = input("Director: ")
            resultados = buscar_por_director(nombre)
            if resultados:
                for titulo, director, anio, puntuacion in resultados:
                    print(f"{titulo} | {director} | {anio} | {puntuacion}")
            else:
                print("No hay coincidencias")

        elif opcion == 3:
            minimo, maximo, promedio = obtener_estadisticas()
            print("Min:", minimo)
            print("Max:", maximo)
            print("Promedio:", promedio)

        elif opcion == 4:
            break

        else:
            print("Opcion invalida")

menu()