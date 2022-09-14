import os  
import random  

import urllib.request


textoBaseDePreguntas = ''''''
renglones = []

try:
    urlBD = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQsOzpKGITdnMwkhIrOUWsr2pUEZV0rcDKb4B8yVuOAj7fwzOG0DUdf6lqE2aRSw7Ig4SeeU04Uc8Y6/pub?output=tsv"
    HTTP_response=urllib.request.urlopen(urlBD)
    for line in HTTP_response:
        renglones.append(line.decode("utf-8").replace("\n","").replace("\r",""))
except:
    print("No hay conexión a internet, no se pudo cargar la BD")
    exit()

n_pregunta = 0

base_de_preguntas = []
cantidadDePreguntas = len(renglones)

preguntaEscogida = []
opciones = []
pregunta = ""
respuesta = ""

for i in range(cantidadDePreguntas):
    if(renglones[i] == ""):
        continue
    base_de_preguntas.append(renglones[i].split("\t"))


def borrarConsola():
    os.system("cls" if os.name == "nt" else "clear")


def escogerPregunta(n):
    global opciones, respuesta, pregunta

    preguntaEscogida = base_de_preguntas[n]
    pregunta = preguntaEscogida[0]
    respuesta = preguntaEscogida[1]
    opciones = preguntaEscogida[1:]
    for i in range(4):
        random.shuffle(opciones)
    print(opciones)
    return preguntaEscogida


def mostrarPregunta():
    borrarConsola()
    print()
    print(pregunta)
    print("A)", opciones[0])
    print("B)", opciones[1])
    print("C)", opciones[2])
    print("D)", opciones[3])
    print()


def capturarRespuesta():
    respuestaUsuario = ""
    opcionesVálidas = ["a", "b", "c", "d"]
    while True:
        respuestaUsuario = input("ingrese su respuesta > ").lower()
        if not (respuestaUsuario in opcionesVálidas):
            print("La respuesta no está entre las opciones válidas, vuelva a intentarlo")
            continue
        break
    return opcionesVálidas.index(respuestaUsuario)


def jugar():
    escogerPregunta(n_pregunta)
    mostrarPregunta()
    if(opciones[capturarRespuesta()]==respuesta):
        print("Su respuesta es correcta")
        input("ENTER PARA CONTINUAR")
    else:
        print("Su respuesta NO es correcta, la correcta es: "+ respuesta)
        input("ENTER PARA CONTINUAR")

while True:
    try:
        jugar()
    except:
        pass
    n_pregunta += 1
    if(n_pregunta==cantidadDePreguntas):
        borrarConsola()
        print("El juego ha finalizado")
        input("ENTER PARA CONTINUAR")
        break