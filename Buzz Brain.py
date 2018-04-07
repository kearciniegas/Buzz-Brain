import random
cont = 1
while cont ==1:
    print("Bienvenido a buzz brain")
    print("Elija la dificultad del juego")
    print("1=Nivel facil")
    print("2=Nivel Medio")
    print("3=Nivel Dificil")
    print("4=Nivel Pesadilla")
    # Nivel de dificultad 
    dificultad = int(input("Digite el numero de dificultad: "))
    if dificultad == 1:
        cant_digitos = 3
    if dificultad == 2:
        cant_digitos = 4
    if dificultad == 3:
        cant_digitos = 5
    if dificultad == 4:
        cant_digitos = 6

    dig =("0","1","2","3","4","5","6","7","8","9")
    cod = ""
    # selecciona los valores que forman
    for i in range(cant_digitos):
        valor = random.choice(dig)
        while valor in cod:
            valor = random.choice(dig)
        cod= cod+valor
    print("tienes que adivinar un codigo de ", cant_digitos, "digitos distintos")
    valor = input("Que valor propones?: ")
    inten = 1
    while valor != cod:
        inten = inten + 1
        aciert = 0
        coinci = 0
        for i in range(cant_digitos):
            if valor[i] == cod[i]:
                aciert = aciert+1
                if valor[i] in cod:
                    coinci = coinci+1
                    print ("tu propuesta (",valor,") tiene ",aciert,"aciertos y ",coinci,"concidencias")
                    valor = input("propon otro codigo:")
                    print ("¡¡¡FELICIDADES!!! Adivinaste el codigo en", inten,"intentos")
                    cont = int(input("Desea seguir jugando? Yes=1 No=0"))
         
                
