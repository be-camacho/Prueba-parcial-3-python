import registro_padel_funciones as rgp

nombre_jugador=[]
rut=[]
fecha_nacimineto=[]
categoria=[]
celular=[]
correo={}
team_name=[]

while True:
    rgp.menu()
    opc=rgp.validarint("opcion--->",1,3)
    
    if opc==1:
        print("ingrese los siguientes datos")
        #nombre
        nombre=rgp.validanombre()
        nombre_jugador.append(nombre)
        #rut
        inrut=rgp.validarut()
        rut.append(inrut)
        #fecha
        infecha=rgp.validaredad()
        fecha_nacimineto.append(infecha)
        #categoria
        rgp.menucategoria
        cat=(input(rgp.validarint("ingrese categoria-->",1,3)))

        if cat == 1:
                categ="Categoria ORO"
        elif cat == 2:
                categ="Categoria PLATA"
        elif cat == 3:
                categ="Categoria BRONCE"
        categoria.append(cat)

        celular.append(rgp.validarint("ingrese numero celular",None,None))
        print(celular)
        tname=team_name.append(rgp.validanombre)
        print(tname)
    

