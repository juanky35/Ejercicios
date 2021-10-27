salario=input("Escribe tu salario anual: ")
if salario.isdigit():
    print("correcto")
    divisor=input("Sobre cuantos meses hay que operar '(incluir pagas)', 12, 13 o 14?: ")
    resultadomensual=int(salario)/int(divisor)
    print("Este es tu salario medio mensual: ",resultadomensual,"€ mensuales en ",divisor, " pagas anuales ")
elif salario[0]=="-":
    print("formato incorrecto, Escribe nuevamente tu salario: ")
    salario=input("...")
else:
    print("formato incorrecto, Escribe nuevamente tu salario: ")
