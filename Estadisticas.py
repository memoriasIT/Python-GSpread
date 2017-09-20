#IMPORTAR LOS MÓDULOS NECESARIOS

import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials

#ACCEDER A LA CUENTA CON LOS CREDENCIALES QUE SE ENCUENTRAN EN EL ARCHIVO PYTHON.JSON
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('python.json', scope)

gc = gspread.authorize(credentials)

#DECLARO LAS DISTINTAS HOJAS DE LA HOJA DE CÁLCULO
uno = gc.open("Testing").sheet1
dos = gc.open("Testing").get_worksheet(1)
tres = gc.open("Testing").get_worksheet(2)
cuatro = gc.open("Testing").get_worksheet(3)


#MUESTRO UNAS ESTADÍSTICAS GENERALES DEL PROGRAMA OBTENIDAS DE LA HOJA DE CÁLCULO
print("""xcvcxcvxcvcxcvxcvcxcvxcvcxcvxcvcxcvx
      ESTADÍSTICAS GENERALES

      1er Curso
      ==========
     """)
Printall = uno.get_all_records()
Numberofstudents = uno.cell(1, 1).value
NextPoll = uno.cell(1, 2).value
pprint.pprint('Numero de estudiantes . . . . . ' + Numberofstudents)
pprint.pprint('Recibir próxima estadística . . ' + NextPoll)

print("""
      2do Curso
      ==========
     """)
Printall = dos.get_all_records()
Numberofstudents = dos.cell(1, 1).value
NextPoll = dos.cell(1, 2).value
pprint.pprint('Numero de estudiantes . . . . . ' + Numberofstudents)
pprint.pprint('Recibir próxima estadística . . ' + NextPoll)
print("""
      3er Curso
      ==========
     """)
Printall = tres.get_all_records()
Numberofstudents = tres.cell(1, 1).value
NextPoll = tres.cell(1, 2).value
pprint.pprint('Numero de estudiantes . . . . . ' + Numberofstudents)
pprint.pprint('Recibir próxima estadística . . ' + NextPoll)
print("""
      4o Curso
      ==========
     """)
Printall = cuatro.get_all_records()
Numberofstudents = cuatro.cell(1, 1).value
NextPoll = cuatro.cell(1, 2).value
pprint.pprint('Numero de estudiantes . . . . . ' + Numberofstudents)
pprint.pprint('Recibir próxima estadística . . ' + NextPoll)


#FUNCIÓN INICIAL, SELECCIÓN DEL CURSO
def inicio():
        while True:
                try:
                        curso=int(input("""xcvcxcvxcvcxcvxcvcxcvxcvcxcvxcvcxcvx
Selecciona curso: """))
                        if curso==1:
                                primero()
                                break
                        elif curso==2:
                                segundo()
                                break
                        elif curso==3:
                                tercero()
                                break
                        elif curso==4:
                                cuarto()
                                break
                        else:
                                print("Solo hay 4 cursos idiota. Mete un número del 1 al 4")
                                inicio()
                except ValueError:
                        print("Solo hay 4 cursos idiota. Mete un número del 1 al 4")
        exit
                                
#DISTINTAS VARIABLES SEGÚN EL CURSO, CADA UNA EN SU RESPECTIVA HOJA                                
def primero():
        nota=int(input("Introduce nota (1-10): "))
        celdaalumno = int(uno.cell(1, 1).value)+1
        uno.update_cell(celdaalumno, 1, nota)
        
        notificaciones=str(input("Introduce e-mail: "))
        uno.update_cell(celdaalumno, 2, notificaciones)

        inicio()
def segundo():
        nota=int(input("Introduce nota (1-10): "))
        celdaalumno = int(dos.cell(1, 1).value)+1
        dos.update_cell(celdaalumno, 1, nota)
        
        notificaciones=str(input("Introduce e-mail: "))
        dos.update_cell(celdaalumno, 2, notificaciones)

        inicio()
def tercero():
        nota=int(input("Introduce nota (1-10): "))
        celdaalumno = int(tres.cell(1, 1).value)+1
        tres.update_cell(celdaalumno, 1, nota)
        
        notificaciones=str(input("Introduce e-mail: "))
        tres.update_cell(celdaalumno, 2, notificaciones)

        inicio()
def cuarto():
        nota=int(input("Introduce nota (1-10): "))
        celdaalumno = int(cuatro.cell(1, 1).value)+1
        cuatro.update_cell(celdaalumno, 1, nota)
        
        notificaciones=str(input("Introduce e-mail: "))
        cuatro.update_cell(celdaalumno, 2, notificaciones)

        inicio()
        
#INICIO DE LA FUNCION INICIAL
inicio()
