from src.create_account import create_account, listar_cuentas

def main():
    while True:
        respuesta = main_menu()
        print(respuesta)
        match respuesta:
            case "1":
                print("Crear cuenta")
                create_account()
            case "2":
                listar_cuentas()
            case "3":
                break    

def main_menu():
    while True:
        opcion = input("Ingrese una opción\n"
        "1. Crear cuenta\n"
        "2. Listar cuentas\n"
        "3. Salir\n> ")

        if opcion in ("1", "2", "3"):
            return opcion
        print("Opción inválida")

if __name__ == "__main__":
    main()
