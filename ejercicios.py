import random

#pedir nombre y edad , calcular dias vividos
#365 x edad
def dias_vividos():
    
    nombre = input("Cual es tu nombre ?")
    print("Cual es tu edad ?")
    edad = int(input())
    dias = 365 * int(edad)
    print("Has vivido " + str(dias) + " dias")
    
#area = base por altura/2
def calcular_area():
    
    base = int(input("Cual es la base? "))

    if base <= 0:  
        print("Solo numeros positivos!")
        return

    altura = int(input("Cual es la altura? "))
    
    if altura <= 0:
        print("Solo numeros positivos!")
        return

    area = (base * altura) / 2

    print("El area del triangulo es de " + str (area) + " centimetros")

#Crear y ordenar un List de números y validar que sólo sean números
def lista():
    
    lista = [7,2,8,2,9,"Benzema",1,"Paco"]

    lista.sort(key=str)

    for i in lista:
        
        if str(i).isnumeric():
            print(i)
        else:
            print("solo numeros!")
            break
        
#elegir que ejercicio quieres hacer        
def elegir():
    
    ejercicio = int(input("Que ejercicio quieres hacer? "))
    print("1,2,3,4")
    if ejercicio == "1":
        dias_vividos()
    elif ejercicio == "2":
        calcular_area()
    elif ejercicio == "3":
        lista()
    elif ejercicio =="4":
        elegir()

#Crear un diccionario Planta con diversos atributos: Nombre, Lugar, días entre riegos, tamaño...
#Validar cada tipo de dato que se meta por consola
def diccionario():
    
    planta = {}
    
    planta['nombre'] = input("Cual es el nombre? ")
    planta['Lugar'] = input("Cual es el lugar? ")
    planta['Origen'] = input("Cual es el origen? ")
    planta['Dias'] = input("Dias entre riegos? ")
    
    while not planta['Dias'].isnumeric():
            print("Solo numeros!")
            planta['Dias'] = input("Dias entre riegos? ")
            
    planta['Dias'] = int(planta['Dias'])         
    planta['Tamaño'] = input("Tamaño? ")
    
    while not planta['Tamaño'].isnumeric():
            print("Solo numeros!")
            planta['Tamaño'] = input(("Tamaño? "))
            
    planta['Tamaño'] = int((planta['Tamaño']))
    
    print (planta)
    
def ejercicio6():
        listPlants = []
        def crearPlanta():
            listPlants.append(diccionario())
             
        for x in range(2):
            crearPlanta()   
            
        def mostrarPlantas():
            print(listPlants)
ejercicio6()
#tupla        
def funcion():
    tupla = (1,"2",3)
    tupla = modificar_tupla(tupla, "pito")
    print(tupla)
    
#tuplas
def modificar_tupla(tupla, valor):
    tupla_list = list(tupla)
    tupla_list.append(valor)
    return tuple(tupla_list)
    
#listas
def lista():
    asignaturas = ["Matematicas","Inglés","Lengua","Ciencia"]
    for asginatura in asignaturas:
        print(asginatura)
#sets
def Set():
    instrumentos = {"Guitarra","Violín","Tambor","Flauta"}
    print (instrumentos)
    
#modificarSet
def modificar_set1():
    instrumentos.add("Batería")

#modificarSet    
def eliminar_set2():
    instrumentos.remove("Tambor")

#validar un email 
def validar_email():
    
    
    correo = print("Cual es tu correo: ")
    
    correo = "contacto@parzibyte.me"
    if "@" in correo:
        print("Es válido")
    else:
        print("No es válido")
        
#Pedir por consola un número y mostrar si es par o impar
def numero_par(): 
    numero = print("Numero: ")
    if ((numero%2)==0):
        print("Es numero par")
    else:
        print("Es numero impar")

#Crear un juego
poolNumber = random.randint(10, 100)
print(poolNumber)
playerNumber = int(input("Escribe un numero del 1 al 9: "))
poolNumber = (poolNumber - playerNumber) * 2
print(poolNumber)
if poolNumber <= 9:
        poolNumber = poolNumber - poolNumber
        print("IA wins")
else:
    poolNumber = poolNumber - random.randint(1, 9)
    print(poolNumber)
print()