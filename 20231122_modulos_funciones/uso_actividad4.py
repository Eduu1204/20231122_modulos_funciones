from actividad4 import Silla

def crear_sillas():
    try:
        color_silla_azul = input("Ingrese el color de la silla azul: ")
        precio_silla_azul = float(input("Ingrese el precio de la silla azul: "))
        silla_azul = Silla(color_silla_azul, precio_silla_azul)

        color_silla_roja = input("Ingrese el color de la silla roja: ")
        precio_silla_roja = float(input("Ingrese el precio de la silla roja: "))
        silla_roja = Silla(color_silla_roja, precio_silla_roja)

        return silla_azul, silla_roja
    except ValueError:
        print("Error: Ingrese un precio válido.")

if __name__ == "__main__":
    silla_azul, silla_roja = crear_sillas()

    print("\nInformación de las sillas:")
    print(f"Silla Azul - Color: {silla_azul.color}, Precio: {silla_azul.precio}")
    print(f"Silla Roja - Color: {silla_roja.color}, Precio: {silla_roja.precio}")
