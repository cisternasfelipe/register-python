import re

def password_validator() -> bool:
    pass

def create_account() -> list:
    nombre = input("Ingrese su nombre \n>")
    apellido_paterno = input("Ingrese su apellido paterno \n>")
    apellido_materno = input("Ingrese su apellido materno \n>")
    rut = input("Ingrese rut \n> ")
    if validar_rut(rut) is False:
        print(f"rut no valido {rut}")

    print(f"rut valido {rut}\n"
          f"nombre: {nombre}\n"
          f"apellido paterno: {apellido_paterno}  \n"
          f"apellido materno: {apellido_materno}  \n")
    
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