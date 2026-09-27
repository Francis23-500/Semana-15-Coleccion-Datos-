notas = {}
 
notas["Ana"] = 8.5
notas["Luis"] = 7.0
notas["Marco"] = 9.2
 
print("Notas registradas:")
for nombre, nota in notas.items():
    print(f"{nombre}: {nota}")
 
buscar = "Luis"
print(f"\nNota de {buscar}: {notas[buscar]}")
 