def user_input(input_type: int, message_to_user:str) -> any:
    """ 1: num input
    2: str input"""
    if input_type == 1:
        try:
            value=int(input(f"{message_to_user}"))
            return value
        except ValueError:
            print("Valor erroneo")
            return None
    elif input_type == 2:
        value=input(f"{message_to_user}")
        return value


def rut_validator() -> bool:
    while True:
        rut=user_input(2,"Ingresa tu rut, sin puntos y con guíon ej. 12345678-9")
        if "-" not in rut:
            raise ValueError("falta el guion")
        if len(rut) not in([9,10]):
            raise ValueError("Rut invalido, necesitas 9 a 10 caracteres")
        rut_limpio=rut.split("-")
        rut_cuerpo=rut_limpio[0]
        rut_digito=rut_limpio[1]
        if rut_cuerpo.isdigit() == False:
            raise ValueError("""El cuerpo del rut deben ser digitos Ej. "12345678"-9 """)
        if rut_digito.isdigit():
            return True
        elif rut_digito.lower() == "k":
            return True
        else:
            raise ValueError("El Rut es invalido")

        
            
            
        
def password_validator() -> bool:
    pass

def create_account() -> list:
    while True:
        pass