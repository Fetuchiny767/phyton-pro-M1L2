import random
#creacion de cositas
contrasenas = {}
caracteres = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@"
pasword = ""
accion = int

#bucle
while accion != 3:
    accion = int(input("Que quieres hacer: 1 = ver contraseñas, 2 = crear contraseña, 3 = salir:")) # accion
    if accion == 1: #ver
        print(contrasenas)

    elif accion == 2:#crear
        eleccion = int(input("quieres personalizar(1) la contraseña o randomizarla(2):"))
        if eleccion == 1:
            nom = input("dime tu nombre de usuario:")#per
            con = input("dime tu contraseña:")
            contrasenas[nom] = con
        
        elif eleccion == 2:
            nom = input("dime tu nombre de usuario:")#random
            con = int(input("cuantos caracteres tendra la contraseña?:"))
            for i in range(con):
                pasword += random.choice(caracteres)
                contrasenas[nom] = con
        else:
            print("esa no es una respuesta valida")

    elif accion == 3:#cerrar
        print("adios")
        break
    
    else:#invalido
        print("esa no es una respuesta valida")
        continue