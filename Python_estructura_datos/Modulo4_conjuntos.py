colores = {"rojo","verde","azul","rojo"}
print(colores)  # Los sets eliminan duplicados automáticamente → {'verde','azul','rojo'}


numeros = set([1, 2, 3, 2, 1])
print(numeros)  # Elimina repetidos → {1, 2, 3}


# BÚSQUEDA EFICIENTE EN SETS

frutas = {"manzana","naranja","plátano"}

print("manzana" in frutas)  # True → búsqueda rápida (O(1))


# CONJUNTO VACÍO

vacio = set()

print(type({}))     # <class 'dict'> → esto NO es un set
print(type(set()))  # <class 'set'> → forma correcta de set vacío

Println ("------------------------------------------------------------------------------------")
tecnologias = {"Python","JavaScript","SQL"}

tecnologias.add("Java")  # agrega un solo elemento
tecnologias.update(["Go","Rust"])  # agrega varios elementos


frutas = {"manzana","naranja","platano"}

frutas.remove("naranja")   # elimina el elemento (da error si no existe)
frutas.discard("kiwi")     # elimina si existe, si no existe no pasa nada

elem = frutas.pop()        # elimina y retorna un elemento aleatorio

frutas.clear()             # elimina todos los elementos → set vacío


# SUBCONJUNTOS Y SUPERCONJUNTOS

pares = {2,4,6,8}
nums  = {1,2,3,4,5,6,7,8,9}

print(pares.issubset(nums))    # True → pares está dentro de nums
print(nums.issuperset(pares))  # True → nums contiene a pares
Println ("------------------------------------------------------------------------------------")
grupo_a = {"Ana","Carlos","Elena","David"}
grupo_b = {"Carlos","Elena","Fernando"}


comunes    = grupo_a.intersection(grupo_b)  # Elementos en común → {'Carlos','Elena'}
todos      = grupo_a.union(grupo_b)         # Unión de ambos conjuntos
solo_en_a  = grupo_a.difference(grupo_b)    # Elementos solo en A → {'Ana','David'}
exclusivos = grupo_a.symmetric_difference(grupo_b)  # Diferentes en ambos conjuntos


vegetales = {"zanahoria","pepino"}
frutas    = {"manzana","platano"}

print(vegetales.isdisjoint(frutas))  # True → no tienen elementos en común


# ENCADENAMIENTO DE OPERACIONES

resultado = grupo_a.intersection(grupo_b).difference({"Elena"})
# Primero encuentra comunes → luego elimina "Elena" → {'Carlos'}
Println ("------------------------------------------------------------------------------------")
u1 = {"acción","comedia","ciencia ficción","aventura"}
u2 = {"drama","comedia","romance","documental"}
u3 = {"acción","aventura","fantasía","ciencia ficción"}


comunes_1_3 = u1 & u3   # Intersección → elementos en común
todos_1_2   = u1 | u2   # Unión → todos los elementos sin repetir
solo_u1     = u1 - u2   # Diferencia → elementos solo en u1
excl_2_3    = u2 ^ u3   # Diferencia simétrica → elementos que no se repiten en ambos


# COMPARACIÓN DE CONJUNTOS

print(u3 <= u1)  # False → u3 no está contenido dentro de u1

print({2,4} <= {1,2,3,4,5})  # True → {2,4} sí es subconjunto
Println ("------------------------------------------------------------------------------------")


tienda_centro = {"Laptop", "Mouse", "Teclado", "Monitor"}
tienda_norte = {"Mouse", "Teclado", "Impresora", "Tablet"}
tienda_sur = {"Laptop", "Tablet", "Audifonos", "Monitor"}

usuario1 = {"Accion", "Ciencia Ficcion", "Drama"}
usuario2 = {"Drama", "Comedia", "Accion"}
usuario3 = {"Terror", "Ciencia Ficcion", "Drama"}

def analizar_tiendas():
    catalogo_completo = tienda_centro | tienda_norte | tienda_sur
    productos_comunes = tienda_centro & tienda_norte & tienda_sur

    exclusivos_centro = tienda_centro - (tienda_norte | tienda_sur)
    exclusivos_norte = tienda_norte - (tienda_centro | tienda_sur)
    exclusivos_sur = tienda_sur - (tienda_centro | tienda_norte)

    print("CATALOGO COMPLETO:", catalogo_completo)
    print("PRODUCTOS COMUNES:", productos_comunes)
    print("EXCLUSIVOS CENTRO:", exclusivos_centro)
    print("EXCLUSIVOS NORTE:", exclusivos_norte)
    print("EXCLUSIVOS SUR:", exclusivos_sur)
    print("CENTRO Y NORTE DISJUNTOS:", tienda_centro.isdisjoint(tienda_norte))
    print("CENTRO Y SUR DISJUNTOS:", tienda_centro.isdisjoint(tienda_sur))
    print("NORTE Y SUR DISJUNTOS:", tienda_norte.isdisjoint(tienda_sur))

def analizar_usuarios():
    comunes = usuario1 & usuario2 & usuario3
    universo = usuario1 | usuario2 | usuario3
    exclusivos_u1 = usuario1 - usuario2 - usuario3
    diferencias = usuario1 ^ usuario2
    subconjunto = comunes <= usuario1

    print("GENEROS COMUNES:", comunes)
    print("UNIVERSO:", universo)
    print("EXCLUSIVOS USUARIO1:", exclusivos_u1)
    print("DIFERENCIAS U1 ^ U2:", diferencias)
    print("COMUNES ES SUBCONJUNTO DE U1:", subconjunto)

def menu():
    while True:
        print("\n1. Analizar tiendas")
        print("2. Analizar usuarios")
        print("3. Ver resumen completo")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione: "))
        except:
            print("Entrada invalida")
            continue

        if opcion == 1:
            analizar_tiendas()

        elif opcion == 2:
            analizar_usuarios()

        elif opcion == 3:
            analizar_tiendas()
            print()
            analizar_usuarios()

        elif opcion == 4:
            break

        else:
            print("Opcion invalida")

menu()