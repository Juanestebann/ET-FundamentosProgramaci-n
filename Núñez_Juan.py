productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}
print(productos)

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]
}
print(stock)

def stock_marca(marca):
    stock_modelos=[]
    stock_dispo=0
    while True:
        encuentra=False
        for m, l in productos.items():
            if marca == l[0].lower():
                stock_modelos.append(m)
                stock_modelos.sort()
                encuentra=True
        if encuentra==False:
            print("La marca ingresada no se encuentra en el diccionario.")
        else:
            print("Marca encontrada")
            break
    for m, s in stock.items():
        if m in stock_modelos:
            stock_dispo+=s[1]
    for modelos in stock_modelos:
        print(f"La marca {marca} tiene de stock el modelo: {modelos} con stock de: {stock[modelos][1]}")
    print(f"Stock total de la marca es: {stock_dispo}")

def busqueda_por_precio(rango_min, rango_max):
    
    modelos_dentro_rango=[]
    rango=range(rango_min,rango_max)
    print(f"Rango Seleccionado desde {rango_min} hasta {rango_max}")
    for m,l in stock.items():
        if l[0] in rango and l[1]!=0:
            modelos_dentro_rango.append(m)
            modelos_dentro_rango.sort()
    for m, mar in productos.items():
        if m in modelos_dentro_rango:
            print(f"El modelo: {m} de marca: {mar[0]} de encuentra dentro del rango.")
    if not modelos_dentro_rango:
        print("No hay notebooks en ese rango de precios. ")

def actualizar_precio(modelo):
    while True:
        try:
        
            
            nuevo_precio=int(input("Ingrese el nuevo precio: "))
            stock[modelo][0]=nuevo_precio
            print(f"Precio actualizado a {stock[modelo][0]}")
            actualizar=input("¿Desea actualizar otro precio de notebook? (SI/NO)").upper()
            if actualizar=="SI":
                print("Volvemos a actualizar.")
            elif actualizar=="NO":
                print("Volvemos al menú principal.")
                break
        except ValueError:
            print("Debe ingresar numeros enteros.")

def menu():
    while True:
        try:
            print("""*** MENU PRINCIPAL ***
            1. Stock marca.
            2) Busqueda por precio.
            3) Actualizar precio.
            4) Salir   
""")
            elec=int(input("Ingrese su respuesta: "))
            if elec<1 or elec>4:
                print("Debe ingresar una opcion valida. ")
            else:
                if elec==1:
                    marca=input("Ingrese la marca que desea consultar su stock: ").lower()
                    stock_marca(marca)
                elif elec==2:
                    while True:
                        try:

                            rango_min=int(input("Ingrese el rango minimo: "))
                            rango_max=int(input("Ingrese el rango maximo: "))
                            busqueda_por_precio(rango_min, rango_max)
                            break
                        except ValueError:
                            print("Debe ingresar numeros enteros")
                elif elec==3:
                    while True:
                        modelo=input("Ingresa el modelo: ").upper()
                        encontrado=False
                        if modelo in stock:
                            encontrado=True
                            if encontrado==True:
                                print("Modelo encontrado.")
                                actualizar_precio(modelo)
                                break
                        else:
                            print("Modelo no encontrado.")
                elif elec==4:
                    print("Programa finalizado.")
                    break
        except ValueError:
            print("Debe ingresar numeros enteros")

menu()


