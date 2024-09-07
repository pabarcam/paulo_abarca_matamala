class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} Precio: {self.precio}, Stock: {self.stock}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, nombre, precio, stock):
        if nombre in self.productos:
            print(f"El producto '{nombre}' ya está registrado.")
        else:
            self.productos[nombre] = {"precio": precio, "stock": stock}
            print(f"Producto '{nombre}' registrado exitosamente.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
        else:
            print("Información de productos registrados:")
            for nombre, detalles in self.productos.items():
                print(f"{nombre} Precio: {detalles['precio']}, Stock: {detalles['stock']}")

def menu():
    inventario = Inventario()
    
    while True:
        print("\nMenú de Inventario")
        print("1. Registrar producto")
        print("2. Mostrar productos registrados")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese la cantidad en stock del producto: "))
            inventario.registrar_producto(nombre, precio, stock)
        
        elif opcion == "2":
            inventario.mostrar_productos()
        
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu()
