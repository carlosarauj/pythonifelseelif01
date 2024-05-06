#frio = True

#if frio:
#    print("usar casaco")
#else:
#    print("nao usar")

sede = True
fome = False
dieta = True

#if sede or fome:
#    print("ir na cozinha")
#else:
#    print("ficar deitado")

#if sede and fome:
#    print("fazer comida")
#else:
#    print("nao fazer")


if sede and fome:
    print("fazer comida e beber")
elif sede and not fome:
    print("beber agua")
    if dieta:
        print("beber agua")
    else:
        print("coquinha")

elif fome and not sede:
    print("fazer comida")

else: 
    print("ficar deitado")


#usa o terminal com: python nomedoarquivo.py