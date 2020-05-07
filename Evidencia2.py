import pandas as pd
import time
separador = ("°°°" * 40) + "\n"
nomAlumnos=["Steve","Diana","Fernando","Gabriela","Krista","Sarahi","Cindy","Nayeli","Isaac","Mariana","Brayton","Jordan","Dinah","Oliver","Wally","Barton","Frank","Matthew","Wilson","Bruce","Clark","Barry","Arthur","Cisco","Tawne","Tony","Natasha","Billy","Scott","Wanda"]
calificacionesAlumnos={}

darInicio = input("\n\nPresione '0' para desplegar el menu: \n")
while darInicio>="0":
    print("\nMENU de opciones: \n\n1)- Mostrar o capturar los nombres de alumnos.\n2)- Capturar calificaciones.\n3)- Comprobar las asignaturas con el menor desempeño.\n4)- Calificaciones de estudiantes que reprobaron.\n5)- Mostrar datos completos.\n6)- Estadísticas descriptivas por materia o por estudiante\n7)- Guardar & salir.\n ")
    print(separador)
    opcion = input("¿Que operacion deseas realizar?: \n")
    if opcion == "1":
        carga=int(input("¿Que opcion desea realizar?\n1)- Capturar direfentes nombres.\n2)- Cargar los nombres predeterminados.\n\n"))
        if carga==1:
            del nomAlumnos[0:31]
            for i in range(1,31):
                nombre= input("Ingrese el nombre del alumno: ")
                nomAlumnos.append(nombre.title())
                print(f"{i*1} Alumnos registrados\n")
        else:
            print("Se cargaron los siguientes nombres de alumnos: ")
            print(nomAlumnos)
            longitud=(len(nomAlumnos))
            print('\n', longitud, "Alumnos registrados")
        time.sleep(3)
    elif opcion =="2":
        for elemento in nomAlumnos:
            calificacion1= float(input(f"Dime la calificacion en Programacion para {elemento}: "))
            while calificacion1<0 or calificacion1>100:
                print("Debes seleccionar una calificacion valida")
                calificacion1= float(input(f"Dime la calificacion en Programacion para {elemento}: "))
            else:
                print()
            calificacion2= float(input(f"Dime la calificacion en Base De Datos para {elemento}: "))
            while calificacion2<0 or calificacion2>100:
                print("Debes seleccionar una calificacion valida")
                calificacion2= float(input(f"Dime la calificacion en Base De Datos para {elemento}: "))
            else:
                print()
            calificacion3= float(input(f"Dime la calificacion en Contabilidad para {elemento}: "))
            while calificacion3<0 or calificacion3>100:
                print("Debes seleccionar una calificacion valida")
                calificacion3= float(input(f"Dime la calificacion en Contabilidad para {elemento}: "))
            else:
                print()
            calificacion4= float(input(f"Dime la calificacion en Redes para {elemento}: "))
            while calificacion4<0 or calificacion4>100:
                print("Debes seleccionar una calificacion valida")
                calificacion4= float(input(f"Dime la calificacion en Redes para {elemento}: "))
            else:
                print()
            calificacion5= float(input(f"Dime la calificacion en Estadistica para {elemento}: "))
            while calificacion5<0 or calificacion5>100:
                print("Debes seleccionar una calificacion valida")
                calificacion5= float(input(f"Dime la calificacion en Estadistica para {elemento}: "))
            else:
                print()
                print(separador)
                calificacionesAlumnos[elemento]=[calificacion1,calificacion2,calificacion3,calificacion4,calificacion5]
                notasEnDiccionario=pd.DataFrame(calificacionesAlumnos)
        notasEnDiccionario.index = ["Programacion", "Base de datos", "Contabilidad", "Redes", "Estadistica"]
    elif opcion =="3":
        print("Estadistica descriptiva calificacion mas baja de cada materia: ")
        print(notasEnDiccionario.T.min())
        print("\nMedia de todas las calificaciones por materia")
        print(notasEnDiccionario.T.mean())
        print("\nDesviacion estandar por todas las materias")
        print(notasEnDiccionario.T.std())
        print(separador)
        time.sleep(4)
    elif opcion =="4":
        print("Calificaciones de studiantes que reprobaron")
        aprodabos = notasEnDiccionario.T[notasEnDiccionario.T<70]
        print(aprodabos)
        print(separador)
        time.sleep(4)
    elif opcion =="5":
        print(notasEnDiccionario.T)
        print(separador)
        time.sleep(4)
    elif opcion =="6":
        decision=int(input("Quiere acceder a los datos estadisticos de: \n1)- Materias.\n2)- Estudiantes.\n"))
        if decision==1:
            print("\n°°°°Estadistica por materias°°°°")
            print(notasEnDiccionario.T.describe())
            op=int(input("¿Deseas guardar estos datos en un archivo de texto?\n1)- Obvio.\n2)- No gracias.\n"))
            if op==1:
                f = open("EstadisticaM.txt","w")
                f.write('--- Estadistica Descriptiva por Materia ---\n\n'+'% s'%notasEnDiccionario.T.describe())
                f.close()
                print("Se guardaron en un archivo llamado 'EstadisticaM'")
            else:
                print()
        else:
            print("\n°°°°Estadistica por alumnos°°°°")
            print(notasEnDiccionario.describe())
            op1=int(input("¿Deseas guardar estos datos en un archivo de texto?\n1)- Obvio.\n2)- No gracias.\n"))
            if op1==1:
                f = open("EstadisticaA.txt","w")
                f.write('--- Estadistica Descriptiva por Alumnos ---\n\n'+'% s'%notasEnDiccionario.describe())
                f.close()
                print("Se guardaron en un archivo llamado 'EstadisticaA'")
            else:
                print()
    elif opcion =="7":
        formatoArchivo=int(input("En que formato desea guardar los datos: \n1)- CSV.\n2)- Json.\nDejar en blanco si no desear guardarlo\n"))
        if formatoArchivo==1:
            notasEnDiccionario.T.to_csv('evidencia2.csv',index=True, header=True)
            print("La informacion se ha guardado en un archivo '.csv'")
        elif formatoArchivo==2:
            notasEnDiccionario.T.to_json('evidencia2J.json', orient="index")
            print("La informacion se a guardado en un archivo '.json'")
        else:
            break
        break
    else:
        print("Debes de elegir una opción valida >:v\n ")
else:
    print("Programa Terminado.\nDebes presionar el numero '0' para iniciar >:v")
