# -------------- Mis Funciones ------------------
# -Genera las coordenadas aleatorias del barco 
# -Ingreso de las coordenadas(Fila y Columna) del jugador
# -Lectura del archivo ranking.csv
# -Escritura del archivo ranking.csv

# -------------- Librerias ------------------
import random
import csv

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

