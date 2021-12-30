importe1=input("Escribe el primer importe: ")
importe1=float(importe1)
importe2=input("Escribe el segundo importe: ")
importe2=float(importe2)
iva=input("Introduce el IVA aplicado: ")
iva=float(iva)
resultado=(importe1+importe2)*(1+iva/100)
miNumeroRedondeado=round(resultado,2)
if  importe1<0:
    importe2<0
    iva<0
    miNumeroRedondeado<0
    print("importe incorrecto, no puede ser negativo") 
else:
    print("El importe a pagar es: ",miNumeroRedondeado," €")