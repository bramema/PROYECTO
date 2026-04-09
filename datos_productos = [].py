import csv

# ================= FUNCIONES =================

def guardar_csv(nombre_archivo, datos, campos):
    with open(nombre_archivo, mode="a", newline="") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(datos)

def cargar_csv(nombre_archivo):
    try:
        with open(nombre_archivo, mode="r") as archivo:
            reader = csv.DictReader(archivo)
            return list(reader)
    except FileNotFoundError:
        return []

# ================= LISTAS =================

datos_productos = cargar_csv("productos.csv")
datos_mesas = cargar_csv("mesas.csv")
datos_cliente = cargar_csv("clientes.csv")

# ================= MENU =================

while True:
    print("===========================================")
    print("=========== BIENVENIDO AL MENU ============")
    print("===========================================")
    print("1. productos")
    print("2. mesas")
    print("3. cliente")
    print("4. Facturacion")
    print("5. salir del menu")

    print("===========================================")
    op = input("opcion: ")
    print("===========================================")

    match op:
    
            # ===== PRODUCTOS =====
        case "1":
            print("1. Agregar producto")
            print("2. Ver productos")

            print("===========================================")
            producto = input("Opcion: ")
            print("===========================================")

            if producto == "1":
                diccionario = {
                    "codigo": input("Codigo: "),
                    "nombre": input("Nombre: "),
                    "valor": input("Valor: "),
                    "IVA": input("IVA: ")
                }
                datos_productos.append(diccionario)
                guardar_csv("productos.csv", datos_productos, ["codigo","nombre","valor","IVA"])
                print(" Producto guardado")

            elif producto == "2":
                print(" LISTA DE PRODUCTOS")
                for p in datos_productos:
                    print(p)

            else:
                print(" Opción no válida, intenta nuevamente")


        # ===== MESAS =====
        case "2":
            print("1. Agregar mesa")
            print("2. Ver mesas")

            print("===========================================")
            mesas = input("Opcion: ")
            print("===========================================")

            if mesas == "1":
                diccionario = {
                    "codigo": input("Codigo: "),
                    "nombre": input("Nombre: "),
                    "puesto": input("Puesto: ")
                }
                datos_mesas.append(diccionario)
                guardar_csv("mesas.csv", datos_mesas, ["codigo","nombre","puesto"])
                print("Mesa guardada")

            elif mesas == "2":
                print("LISTA DE MESAS")
                for m in datos_mesas:
                    print(m)
                    
            else:
                print(" Opción no válida, intenta nuevamente")

        # ===== CLIENTES =====
        case "3":
            print("1. Agregar cliente")
            print("2. Ver clientes")

            print("===========================================")
            cliente = input("Opcion: ")
            print("===========================================")

            if cliente == "1":
                diccionario = {
                    "identificación": input("ID: "),
                    "nombre": input("Nombre: "),
                    "teléfono": input("Teléfono: "),
                    "email": input("Email: ")
                }
                datos_cliente.append(diccionario)
                guardar_csv("clientes.csv", datos_cliente, ["identificación","nombre","teléfono","email"])
                print("Cliente guardado")

            elif cliente == "2":
                print(" LISTA DE CLIENTES")
                for c in datos_cliente:
                    print(c)

            else:
                print(" Opción no válida, intenta nuevamente")

        # ===== FACTURACION (pendiente) =====
        
        

    