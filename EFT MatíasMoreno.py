#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

#stock = {modelo: [precio, stock]]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca):
    marca = marca.lower()
    total = 0
    for modelo, info in productos.items():
        if info[0].lower() == marca and modelo in stock:
            total += stock[modelo][1]
    print(f"El stock es: {total}")

def busqueda_precio(p_min, p_max):
    disponible = []
    for modelo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            disponible.append(f"{marca}--{modelo}")

    if disponible:
        disponible.sort()
        print(f"Los notebooks entre los precios consultas son: {disponible}")
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = int(p)
        return True
    else:
        return False

def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca\n2. Busqueda por precio\n3. Actualizar precio\n4. Salir")

        op = input("Ingrese opción: ")

        if op == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
        elif op == "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(p_min,p_max)
        elif op == "3":
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                p = input("Ingrese precio nuevo: ")

                if actualizar_precio(modelo, p):
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")

                continuar = input("Desea actualizar otro precio (si/no): ").lower

                if continuar != 'si':
                    break
        elif op == "4":
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opción valida!!")

menu()