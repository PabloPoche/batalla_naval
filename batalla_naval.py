# Curso de Python
# Proyecto nivel inicial

# Autor: Pablo Pochettino
# Version: 1.0
# -------------------- Juego de Batalla Naval --------------------------------
# El tablero de juego consiste en una cuadricula de 4filas x 4columnas y
# las coordenadas del barco se generaran aleatoriamente en cada partida.
# El jugador debera ingresar por teclado las coordenadas(Fila y Columna), 
# en caso de coinsidir con las del barco se displayara "FELICITACIONES!!" y
# se le pedira ingrese su nombre al Ranking de jugadores, caso contrario
# se displayara "AGUA" y se le pedira ingresar nuevas coordenadas.

# -------------- Librerias ------------------
import random
import csv
import os

# -------------- Funciones ------------------

# Genera las coordenadas aleatorias del barco 
def gen_coord_barco ():
    fila_b = chr(random.randint(65,68))
    columna_b = str(random.randint(0,3))
    coord_barco = fila_b  + columna_b
    return(coord_barco)

# Ingreso de las coordenadas(Fila y Columna) del jugador
def in_coord_jugador ():
    print("            Ingrese coordenadas ")
    print("                Fila[A a D]: ", end= "")
    while True:
        fila_j = str(input()).upper()
        if fila_j >= "A" and fila_j <= "D" : 
            break
        else:
            print("Coordenada invalida!")
            print("Typee una letra entre A y D: ", end= "")
    print("             Columna[0 a 3]: ", end= "")
    while True:
        columna_j = str(input())
        if columna_j >= "0" and columna_j <= "3" : 
            break
        else:
            print("Coordenada invalida!")
            print("Typee un numero entre 0 y 3: ", end= "")
    coord_jugador = fila_j + columna_j
    return(coord_jugador)

# Lectura del archivo ranking.csv
def read_csv():
    csvfile = open("ranking.csv")
    ranking = list(csv.DictReader(csvfile))
    csvfile.close()
    return(ranking)

# Escritura del archivo ranking.csv
def write_csv(jugador, intentos):
    csvfile = open("ranking.csv", "a", newline="")
    header = ["Jugador", "Puesto"]
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writerow({"Jugador": jugador , "Puesto": intentos})
    csvfile.close()
    return()


# --------------------------------
# -----Comienzo del programa-----

if __name__ == '__main__':

    while True:
        # Displayado del Menu principal
        os.system("cls")
        print("                        BATALLA NAVAL")
        print("                   (4-filas x 4-columnas)")
        print("")
        print("              Typee: ")
        print("                        J - Jugar")
        print("                        R - Ranking")
        print("                        S - Salir")
        
        # Ingreso de opciones [J, R o S]
        while True:
            opcion = str(input()).upper()
            if opcion == "J" or opcion == "R" :
                os.system("cls")
                break
            elif opcion == "S" :
                print("Gracias por jugar :)")
                print("")
                exit()
            else:
                print("Opcion invalida!")
                print("typee J, R o S: ", end= "")

         # Inicio del juego  
        if opcion == "J" :
            intentos = 1
            coord_barco = gen_coord_barco ()
            # print(coord_barco) ....linea usada para testear el programa
            while True:
                print("Intento N:",intentos )
                coord_jugador = in_coord_jugador ()   
                # Compara las coord. aleatorias del barco con las coord. ingresadas por el jugador
                if coord_jugador == coord_barco :
                    print("")
                    print("              FELICITACIONES!!")
                    print("Ha logrado undir el barco luego de", intentos, "intentos")
                    print("")
                    jugador = str(input("Ingrese su nombre al Ranking de jugadores: "))
                    # Agrega jugador e intentos a ranking.csv
                    write_csv(jugador, intentos)
                    break
                else:
                    print("")
                    print("                     AGUA!!")
                    print("")
                    intentos += 1
        
        # Displayado del Ranking de jugadores 
        elif opcion == "R" :
            print("                      Ranking de Jugadores")
            print("                      --------------------")
            print("           JUGADOR:                          PUESTO N:")
            print("")
            
            # Recupera ranking de archivo ranking.csv
            ranking = read_csv()
            
            # Busca en el ranking el numero maximo de intentos(puesto)
            max_intento = 0
            for i in range(len(ranking)):
                if int(ranking[i].get("Puesto")) > max_intento:
                    max_intento = int(ranking[i].get("Puesto"))
            
            # Displaya el ranking en funcion del puesto
            for j in range(max_intento + 1):
                for i in range(len(ranking)):
                    if int(ranking[i].get("Puesto")) == j :
                        print("           ", ranking[i].get("Jugador"), chr(9) + chr(9) + chr(9) + chr(9), ranking[i].get("Puesto"))
            
            print("")
            input("          Presione Enter para volver al Menu principal ")
            
            