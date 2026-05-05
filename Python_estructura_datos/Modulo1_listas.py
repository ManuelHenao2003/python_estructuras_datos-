
tareas = ["estudiar","ejercicio","programar","descansar"]



primera   = tareas[0]    # Posición 0 → primer elemento → "estudiar"
ultima    = tareas[-1]   # -1 → último elemento → "descansar"
penultima = tareas[-2]   # -2 → penúltimo → "programar"

print(len(tareas))           # Cuenta elementos → 4
print("programar" in tareas) # Verifica si existe → True
print(tareas.count("ejercicio")) # Cuenta repeticiones → 1
print(tareas.index("programar")) # Posición del elemento → 2

Println ("------------------------------------------------------------------------------------")

numeros = [10, 20, 30, 40, 50, 60, 70]



primeros_tres = numeros[0:3]   # Desde índice 0 hasta antes de 3 → [10, 20, 30]
del_1_al_3    = numeros[1:4]   # Desde índice 1 hasta antes de 4 → [20, 30, 40]
hasta_tercero = numeros[:3]    # Desde inicio hasta antes de 3 → [10, 20, 30]
desde_tercero = numeros[2:]    # Desde índice 2 hasta el final → [30, 40, 50, 60, 70]
pares         = numeros[::2]   # Salta de 2 en 2 → [10, 30, 50, 70]
ultimos_tres  = numeros[-3:]   # Últimos 3 elementos → [50, 60, 70]
invertida     = numeros[::-1]  # Lista invertida → [70, 60, 50, 40, 30, 20, 10]
Println ("------------------------------------------------------------------------------------")
tareas = ["estudiar", "ejercicio"]

tareas.append("programar")         # Agrega un elemento al final → ["estudiar", "ejercicio", "programar"]
tareas.insert(0, "llamar médico")  # Inserta en posición 0 → ["llamar médico", "estudiar", "ejercicio", "programar"]
tareas.extend(["lavar ropa", "cocinar"])  # Agrega varios elementos → ["llamar médico", "estudiar", "ejercicio", "programar", "lavar ropa", "cocinar"]

# DIFERENCIA ENTRE append Y extend

a = [1, 2, 3]
a.append([4, 5])   # Agrega la lista como un solo elemento → [1, 2, 3, [4, 5]]

a = [1, 2, 3]
a.extend([4, 5])   # Agrega cada elemento por separado → [1, 2, 3, 4, 5]
Println ("------------------------------------------------------------------------------------")

colores = ["rojo", "verde", "azul", "verde"]

colores.remove("verde")  # Elimina la primera aparición de "verde" → ["rojo", "azul", "verde"]

nums = [10, 20, 30, 40]

ultimo  = nums.pop()   # Elimina y retorna el último elemento → 40 | nums = [10, 20, 30]
segundo = nums.pop(1)  # Elimina y retorna el índice 1 → 20 | nums = [10, 30]

mi_lista = [1, 2, 3, 4]

mi_lista.clear()  # Elimina todos los elementos de la lista → []
Println ("------------------------------------------------------------------------------------")

nums = [3, 1, 4, 2]

nums.sort()              # Ordena la lista original de menor a mayor → [1, 2, 3, 4]
nums.sort(reverse=True)  # Ordena de mayor a menor → [4, 3, 2, 1]

letras = ["c", "a", "b"]

letras.reverse()         # Invierte el orden actual → ["b", "a", "c"]

original = [3, 1, 4, 2]

nueva = sorted(original) # Crea una nueva lista ordenada → [1, 2, 3, 4]
print(original)          # La lista original no cambia → [3, 1, 4, 2]

Println ("------------------------------------------------------------------------------------")

frutas = ["manzana", "plátano", "naranja"]

for f in frutas:
    print(f"Me gusta {f}")  # Recorre la lista e imprime cada elemento

for i, f in enumerate(frutas, 1):
    print(f"{i}. {f}")  # enumerate agrega índice comenzando en 1

nombres = ["Ana","Carlos","Elena"]
edades  = [28, 35, 23]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad} años")  # zip une dos listas elemento a elemento

cuadrados = [n**2 for n in range(5)]  # Eleva al cuadrado cada número → [0,1,4,9,16]

pares = [n for n in range(10) if n%2==0]  # Filtra solo números pares → [0,2,4,6,8]
Println ("------------------------------------------------------------------------------------")

a = [1, 2, 3]
b = a        # b no es copia, es la misma lista (misma referencia)

b[0] = 100   # modifica la lista original

print(a)     # [100, 2, 3] → también cambia porque apuntan al mismo objeto

a = [1, 2, 3]
b = a.copy()  # crea una copia independiente

b[0] = 100

print(a)     # [1, 2, 3] → no cambia
print(b)     # [100, 2, 3]


# LISTAS ANIDADAS → deepcopy

import copy

anidada = [[1, 2], [3, 4]]

deep = copy.deepcopy(anidada)  # copia profunda (totalmente independiente)

deep[0][0] = 99

print(anidada)  # [[1, 2], [3, 4]] → intacta
print(deep)     # [[99, 2], [3, 4]]

Println ("------------------------------------------------------------------------------------")

Inventario = [
    ["Detodito", 10, 2300],
    ["Chocorramo", 40, 4000],
    ["Chocolatina", 25, 3500],
]

def actualizar_precio(producto, nuevo_precio):
    for item in Inventario:
        if item[0].lower() == producto.lower():
            item[2] = nuevo_precio
            print(f"Precio actualizado de {producto}")
            return
    print("Producto no encontrado")

def registrar_venta(producto, cantidad):
    for item in Inventario:
        if item[0].lower() == producto.lower():
            if item[1] >= cantidad:
                item[1] -= cantidad
                print(f"Venta realizada de {producto}")
            else:
                print("No hay suficiente stock")
            return
    print("Producto no encontrado")

def anadir_producto(producto, cantidad, precio):
    Inventario.append([producto, cantidad, precio])
    print(f"Producto {producto} añadido")

def mostrar_inventario():
    print("\nINVENTARIO:")
    for i, item in enumerate(Inventario):
        print(f"{i+1}. Producto: {item[0]}, Cantidad: {item[1]}, Precio: {item[2]}")

def menu():
    while True:
        print("\n1. Ver inventario")
        print("2. Actualizar precio")
        print("3. Registrar venta")
        print("4. Añadir producto")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except:
            print("Debe ingresar un número")
            continue

        if opcion == 1:
            mostrar_inventario()

        elif opcion == 2:
            producto = input("Ingrese el nombre del producto: ")
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
            except:
                print("Precio inválido")
                continue
            actualizar_precio(producto, nuevo_precio)

        elif opcion == 3:
            producto = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
            except:
                print("Cantidad inválida")
                continue
            registrar_venta(producto, cantidad)

        elif opcion == 4:
            producto = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese la cantidad: "))
                precio = int(input("Ingrese el precio: "))
            except:
                print("Datos inválidos")
                continue
            anadir_producto(producto, cantidad, precio)

        elif opcion == 5:
            break

        else:
            print("Opción inválida")

menu()