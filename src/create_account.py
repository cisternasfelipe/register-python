import re

cuentas = []

def password_validator(password: str = None) -> bool:
    if password is None:
        password = input("Ingrese su contraseña\n> ")
    if len(password) < 8:
        print("Error: mínimo 8 caracteres")
        return False
    if not any(caracter.isdigit() for caracter in password):
        print("Error: debe contener al menos un número")
        return False
    print("Contraseña válida")
    return True

def existe_RUT(rut):
    for cuenta in cuentas:
        if cuenta["rut"] == rut:
            return True
    return False

def create_account():
    while True:
        nombre = input("Ingrese su nombre \n>")
        apellido_paterno = input("Ingrese su apellido paterno \n>")
        apellido_materno = input("Ingrese su apellido materno \n>")

        while True:
            rut = input("Ingrese rut \n> ")
            if not validar_rut(rut):
                print("RUT no válido")
            elif existe_RUT(rut):
                print("RUT ya registrado")
            else:
                break

        while True:
            if password_validator():
                break

        cuentas.append({
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "rut": rut,
        })
        print(f"Cuenta creada: {nombre} {apellido_paterno} — RUT: {rut}")

        continuar = input("¿Desea continuar ingresando? (si/no)\n> ").lower()
        if continuar != "si":
            break
    
def validar_rut(rut_str):
    # 1. Limpiar caracteres y convertir la 'k' a mayúscula
    rut_limpio = rut_str.replace(".", "").replace("-", "").upper()
    
    # 2. Regex para formato: hasta 8 números seguidos del DV (número o K)
    patron = r"^\d{1,8}[0-9K]$"
    if not re.match(patron, rut_limpio):
        return False
    
    # 3. Extraer cuerpo y dígito verificador
    rut_cuerpo = rut_limpio[:-1]
    dv_ingresado = rut_limpio[-1]
    
    # 4. Cálculo del Módulo 11
    suma = 0
    multiplicador = 2
    
    for caracter in reversed(rut_cuerpo):
        suma += int(caracter) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
            
    resto = suma % 11
    dv_calculado = 11 - resto
    
    # 5. Ajustes para casos especiales del Módulo 11
    if dv_calculado == 11:
        dv_calculado = "0"
    elif dv_calculado == 10:
        dv_calculado = "K"
    else:
        dv_calculado = str(dv_calculado)
        
    # 6. Comparación final
    return str(dv_calculado) == dv_ingresado

def listar_cuentas():
    if not cuentas:
        print("No hay cuentas registradas")
        return
    for indice, cuenta in enumerate(cuentas, 1):
        print(f"{indice}. {cuenta['nombre']} {cuenta['apellido_paterno']} "
              f"{cuenta['apellido_materno']} — RUT: {cuenta['rut']}")