nombre=input("como te llamas:")
edad=input("Qué edad tienes:")
edad=int(edad)
if edad>=18:
    print("Buenos días:",nombre, ",eres mayor de edad, bienvenido/a")
else:
    print(nombre, ":Sin autorización de acceso, Eres menor de edad")