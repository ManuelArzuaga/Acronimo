palabra = input("ingrese una organizacion")
palabra2 = palabra.split()
palabra3 = ""
for x in range(len(palabra2)):

    palabra3 = palabra3 + palabra2[x][0]

print(palabra3)