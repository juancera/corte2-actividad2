while True:
    print("menu\n 1.personas\n2.vehiculos\n3.universidades\n4.notas\n5.salir")
    opcion = int (input("seleccione una opcion:"))
    
    
    if opcion>5 or opcion<1:
        print("la opcion no existe")
        
    elif opcion == 1:
        print("hola has presionado la opcion personas")
        
    elif opcion == 2:
        print("hola has presionado la opcion vehiculos")
        
    elif opcion == 3:
        print("hola has presionado la opcion universidades")
        
    elif opcion == 4:
        print("hola has presionado la opcion notas")
        
    elif opcion == 5:
        print("gracias por usar nuestra app")
        break