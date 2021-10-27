idUsuario=input("Ingresa tu identificador de Usuario:")
Contraseña=input("Ingresa tu contraseña")
if Contraseña.find("admin"):
    Contraseña.find("123")
    Contraseña.find("password")
    print("error de seguridad, no usar admin, 123 o password en tu contraseña")
else:
    print("Contraseña segura")
