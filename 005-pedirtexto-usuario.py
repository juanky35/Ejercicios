frase=input("Por favor, escribe una frase!:")
frasemayuscula=frase.upper()
busqueda=input("solicita una busqueda de caractares en tu frase:")
busqueda=busqueda.upper()
resultadoabuscar=frasemayuscula.count(busqueda)
print("listo, aqui tienes los resultados",resultadoabuscar,"veces")
