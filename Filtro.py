import json
from os import system
system("clear")

with open("Movistar.json", encoding=("utf-8")) as file:
    movistar=json.load(file)

def menu():
    print("1. Agregar cliente\n2. Eliminar cliente\n3. Cambiar servició de cliente\n4. Ver clientes\n5. CAmbiar fidelizacion de cliente\n6. Salir")

bol1=True
while bol1==True:

    menu()
    bolTry=True
    while bolTry==True:
        try:
            opc=int(input("Ingresa tu opcion\n"))
            while opc<1 or opc>6:
                opc=int(input("Ingresa una opcion de las que aparecen en pantalla\n"))
            bolTry=False
        except ValueError:
            print("Ingresa una opcion valida (Numeros)")
    
    if opc==1:
        system("clear")
        
        print("-----Servicios-----")
        servicio=input("Postpago\nPrepago\nFibra Optica\nIngresa tu opcion\n")
        while servicio not in movistar["administracion"][0]["Planes"]:
            servicio=input("Ingresa una opcion de las que aparecen en pantalla(Tienes que escribirla como se ve ahi)\n")
        
        system("clear")
        print("------Paquetes------")
        cont=0
        for i in movistar["administracion"][0]["Planes"][servicio]:
            cont+=1
            print("-------------Paquete",cont,"---------------")
            print ("Nombre:",i["nombre"])
            print ("Precio:",i["precio"])
            print ("Navegacion:",i["Navegacion"])
            print("")
        
        bolTry=True
        while bolTry==True:
            try:
                paquetePost=int(input("Ingresa el numero del paquete que quieres\n"))
                while paquetePost<1 or paquetePost>len(movistar["administracion"][0]["Planes"][servicio]):
                    paquetePost=int(input("Ingresa un paquete de los que aparecen en pantalla\n"))
                bolTry=False
            except ValueError:
                print("Ingresa una opcion valida (Numeros)")
            
        system("clear")

        nombreC=input("Ingresa el nombre del nuevo cliente\n")
        direccion=input("Ingrese la direccion del nuevo cliente\n")
        bolTry=True
        while bolTry==True:
            try:
                identificacionC=int(input("Ingresa el numero de identificacion del nuevo cliente\n"))
                bolTry=False
            except ValueError:
                print("Ingresa un numero de identificacion valido (Solo numeros)")
   
        bolTry=True
        while bolTry==True:
            try:
                contacto=int(input("Ingresa un numero de contacto del nuevo cliente (Telefono)\n"))
                bolTry=False
            except ValueError:
                print("Ingresa un numero de contacto valido (Solo numeros)")
        fechaInicio=input("Ingresa una fecha de inicio (DD/MM/AAAA)\n")
        movistar[servicio].append({"nombre":nombreC,"direccion":direccion,"identificacion":identificacionC,"contacto":contacto,"servicio":servicio,"paquete":paquetePost,"fechaInicio":fechaInicio,"tipoCliente":"nuevo cliente"})

        

        input("Cliente agregado con exito\nPreciona enter para continuar\n")
        system("clear")

    elif opc==2:
        system("clear")
        
        print("-----Servicios-----")
        servicio=input("Postpago\nPrepago\nFibra Optica\n¿De que servicio quieres borrar el cliente?\n")
        while servicio not in movistar["administracion"][0]["Planes"]:
            servicio=input("Ingresa una opcion de las que aparecen en pantalla(Tienes que escribirla como se ve ahi)\n")
        
        print("-----Clientes-----")
        for i in movistar[servicio]:
            print("-----------------------------")
            print("Nombres:",i["nombre"])
            print("Identificacion:",i["identificacion"])
            print("")

        bolTry=True
        while bolTry==True:
            try:
                clienteEliminar=int(input("Ingresa la identificacion del cliente que quieres eliminar\n"))
                cont=0
                while cont==0:
                    posicion=0
                    for i in movistar[servicio]:
                        posicion+=1
                        if clienteEliminar==i["identificacion"]:
                            cont+=1
                            posicionActual=posicion-1

                    if cont==0:
                        clienteEliminar=int(input("Identificacion no encontrada Ingresa una de las que aparecen en pantalla\n"))
                bolTry=False
            except ValueError:
                print("Identificacion invalida ingresa una correcta (Solo numeros)")
        
        del movistar[servicio][posicionActual]
        

        input("Cliente eliminado con exito\nPreciona enter para continuar\n")
        system("clear")

    elif opc==3:

        system("clear")
        
        print("-----Servicios-----")
        servicioCambiar=input("Postpago\nPrepago\nFibra Optica\n¿En que servicio se encuentra el cliente al que le deseas cambiar el servivio?\n")
        while servicioCambiar not in movistar["administracion"][0]["Planes"]:
            servicioCambiar=input("Ingresa una opcion de las que aparecen en pantalla(Tienes que escribirla como se ve ahi)\n")
        

        contadorDeClientes=0
        while contadorDeClientes==0:
            print("------Clientes------")
            for i in movistar[servicioCambiar]:
                contadorDeClientes+=1
                print("------------------------------")
                print("Nombre:",i["nombre"])
                print("Identificacion:",i["identificacion"])
                print("Servicio:",i["servicio"])
                print("")
            
            if contadorDeClientes==0:
                print("Este servicio no tiene clientes")

                servicioCambiar=input("Ingresa otro servicio\n")
                while servicioCambiar not in movistar["administracion"][0]["Planes"]:
                    servicioCambiar=input("Ingresa una opcion de las que aparecen en pantalla(Tienes que escribirla como se ve ahi)\n")

        bolTry=True
        while bolTry==True:
            try:
                clienteCambiar=int(input("Ingresa la identificacion del cliente al que le quieres cambiar el servicio\n"))
                cont=0
                while cont==0:
                    posicion=0
                    for i in movistar[servicioCambiar]:
                        posicion+=1
                        if clienteCambiar==i["identificacion"]:
                            cont+=1
                            posicionCambiar=posicion-1

                    if cont==0:
                        clienteCambiar=int(input("Identificacion no encontrada Ingresa una de las que aparecen en pantalla\n"))
                bolTry=False
            except ValueError:
                print("Identificacion invalida ingresa una correcta (Solo numeros)")
            
        system("clear")
    
        print("-----Servicios-----")
        servicioNuevo=input("Postpago\nPrepago\nFibra Optica\nIngresa el nuevo servicio del cliente\n")
        while servicioNuevo not in movistar["administracion"][0]["Planes"]:
            servicioNuevo=input("Ingresa una opcion de las que aparecen en pantalla(Tienes que escribirla como se ve ahi)\n")
        
        infoClienteCambiar=movistar[servicioCambiar][posicionCambiar]

        del movistar[servicioCambiar][posicionCambiar]

        movistar[servicioNuevo].append(infoClienteCambiar)
        
        for w in range(len(movistar[servicioNuevo])):
            if clienteCambiar==movistar[servicioNuevo][w]["identificacion"]:
                posicionServicio=w

        movistar[servicioNuevo][posicionServicio]["servicio"]=servicioNuevo

        system("clear")
        print("------Paquetes------")
        cont=0
        for i in movistar["administracion"][0]["Planes"][servicioNuevo]:
            cont+=1
            print("-------------Paquete",cont,"---------------")
            print ("Nombre:",i["nombre"])
            print ("Precio:",i["precio"])
            print ("Navegacion:",i["Navegacion"])
            print("")
        
        bolTry=True
        while bolTry==True:
            try:
                paquete=int(input("Ingresa el numero del paquete que quieres\n"))
                while paquete<1 or paquete>len(movistar["administracion"][0]["Planes"][servicioNuevo]):
                    paquete=int(input("Ingresa un paquete de los que aparecen en pantalla\n"))
                bolTry=False
            except ValueError:
                print("Ingresa una opcion valida (Numeros)")
        
        movistar[servicioNuevo][posicionServicio]["paquete"]=paquete

    
    elif opc==4:
        system("clear")

        print("------Clientes------")

        for i in movistar["Postpago"]:
            print("---------------------------")
            print("Nombres:",i["nombre"])
            print("Identificacion:",i["identificacion"])
            print("Sercicio:",i["servicio"])
            print("Fidelizacion:",i["tipoCliente"])
            print("")
        
        for i in movistar["Prepago"]:
            print("---------------------------")
            print("Nombres:",i["nombre"])
            print("Identificacion:",i["identificacion"])
            print("Sercicio:",i["servicio"])
            print("Fidelizacion:",i["tipoCliente"])
            print("")
        
        for i in movistar["Fibra Optica"]:
            print("---------------------------")
            print("Nombres:",i["nombre"])
            print("Identificacion:",i["identificacion"])
            print("Sercicio:",i["servicio"])
            print("Fidelizacion:",i["tipoCliente"])
            print("")
        
        input("Preciona enter para continuar\n")
        system("clear")

    elif opc==5:
        system("clear")
        
        print("-----Servicios-----")
        servicioCambiarFidelizacion=input("Postpago\nPrepago\nFibra Optica\n¿En que servicio se encuentra el cliente al que le deseas cambiar el tipo de fidelizacion?\n")
        while servicioCambiarFidelizacion not in movistar["administracion"][0]["Planes"]:
            servicioCambiarFidelizacion=input("Ingresa una opcion de las que aparecen en pantalla(Tienes que escribirla como se ve ahi)\n")
        

        contadorDeClientes=0
        while contadorDeClientes==0:
            print("------Clientes------")
            for i in movistar[servicioCambiarFidelizacion]:
                contadorDeClientes+=1
                print("------------------------------")
                print("Nombre:",i["nombre"])
                print("Identificacion:",i["identificacion"])
                print("")
            
            if contadorDeClientes==0:
                print("Este servicio no tiene clientes")

                servicioCambiarFidelizacion=input("Ingresa otro servicio\n")
                while servicioCambiarFidelizacion not in movistar["administracion"][0]["Planes"]:
                    servicioCambiarFidelizacion=input("Ingresa una opcion de las que aparecen en pantalla(Tienes que escribirla como se ve ahi)\n")

        bolTry=True
        while bolTry==True:
            try:
                clienteCambiarFidelizacion=int(input("Ingresa la identificacion del cliente al que le quieres cambiar el servicio\n"))
                cont=0
                while cont==0:
                    posicionF=0
                    for i in movistar[servicioCambiarFidelizacion]:
                        posicionF+=1
                        if clienteCambiarFidelizacion==i["identificacion"]:
                            cont+=1
                            posicionCambiarF=posicionF-1

                    if cont==0:
                        clienteCambiarFidelizacion=int(input("Identificacion no encontrada Ingresa una de las que aparecen en pantalla\n"))
                bolTry=False
            except ValueError:
                print("Identificacion invalida ingresa una correcta (Solo numeros)")

        system("clear")
        print("------Tipos De Fidelizacion------")
        for e in movistar["administracion"][1]:
            print(e)
        
        nuevaFidelizacion=input("Ingresa la nueva fidelizacion del cliente\n")
        while nuevaFidelizacion not in movistar["administracion"][1]:
            nuevaFidelizacion=input("Ingresa una fidelizacion de las que aparecen en pantalla (Tienes que escribirla como se ve ahi)")
        movistar[servicioCambiarFidelizacion][posicionCambiarF]["tipoCliente"]=nuevaFidelizacion


    elif opc==6:
        bol1=False 




movistar_Json=json.dumps(movistar)

with open("Movistar.json","w") as file:
    file.write(movistar_Json)

#desarrollado por Luis Henao c.c. 1093904929