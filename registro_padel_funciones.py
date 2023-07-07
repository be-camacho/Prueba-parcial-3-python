## funciones
def validarint(text,min,max):
    while True:
        try:
            numero=int(input(text))
            if min!=None and max!=None:
                if min<=numero<=max:
                    break
                else:
                    print("fuera de rango")
            else:
                break
        except:
            print("valor ingresado debe ser un numero!!!")
    return numero

def menu():
    print("******************************************")
    print("REGISTRO CAMPIONATO DE PADEL")
    print("******************************************")
    print("Ingrese una de las siguientes opciones")
    print("1-->Ingresar jugador")
    print("2-->Buscar jugador")

def validaredad():
    anno_nacimiento=input(validarint("ingrese año",1943,2015))
    return anno_nacimiento
        
def validanombre():
    while True:
        try:
            nombre=input("ingrese nombre")
            if len(nombre)<3:
                print("el nombre debe contener mas de dos letras")
            else:
                break
        except:
            print("ingrese un nombre")
    return nombre

def validacorreo():
    while True:
        try:
            correo=input("ingrese correo")
            if len(correo)<6:
                print("el correo debe contener mas de 6 digitos")
            elif "@" in correo:
                break
            else:
                print("el coreo debe contener un '@' ")
        except:
            print("ingrese un correo")
    return correo

def validarut():
    while True:
        try:
            rut=input("ingrese rut")
            break
        except:
            print("ingrese un rut")
    return rut

def menucategoria():
            print("1-->categra oro")
            print("2-->categra plata")
            print("3-->categra bronce")
        
def mi_nombre():
    print("benjamin Camacho")

##correo con un len ver el largo y tiene que ser de 6 o mayor
##eda tiene que ser maor a 80 años
##nombre mayor a 2 caracteres leer con un len 
