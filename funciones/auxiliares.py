# Copyright (C) 2024 <UTN FRA>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame.mixer as mixer
import time


def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def play_sound():
    """
    The `play_sound` function initializes the mixer, loads a sound file, sets the volume to 0.4, and
    plays the sound.
    """
    mixer.init()
    mixer.music.load('./assets/snd/select.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()
    time.sleep(0.4)

def mostrar_nombre(lista_de_nombres:list, indice:int) :
    """pide una lista de nombres y un índice,
    para luego retornar un elemento de la lista según
    el índice pedido.

    Args:
        lista_de_nombres(list): la lista de nombres 
        indice(int): posición del elemento a retornar 
                    de la lista


    Returns:
        nombre_a_mostrar(str): el elemento en base al índice
                            ingresado
    
    """
    nombre_a_mostrar = lista_de_nombres[indice - 1]
    
    return nombre_a_mostrar

def obtener_maximo(lista_de_numeros:list) -> float:
    """Esta función pide como parametro una lista
    que tenga elementos del tipo int ó float para
    compararlos y obtener el máximo de ellos.

    Args:
        lista_de_numeros(list): lista de números a comparar

    Returns:
        valor_maximo(float): valor máximo de la lista
    """
    valor_maximo = None

    for valor in lista_de_numeros:
        
        if valor_maximo == None: 
            valor_maximo = valor
        else:
            if valor > valor_maximo :
                valor_maximo = valor

    return float(valor_maximo)



def promedio(lista_de_numeros:list) -> float:
    """Esta función pide como parametro una lista
    que tenga elementos del tipo int ó float para recorrela
    y obtener el promedio del mismo. 

    Args:
        lista_de_numeros(list): lista de números

    Returns:
        resultado(float): la operación del promedio
    """
    suma_numeros = 0
    contador_de_vueltas = 0
    for valor in lista_de_numeros:
        suma_numeros += valor
        contador_de_vueltas += 1

    operacion_promedio = suma_numeros / contador_de_vueltas
    
    resultado = operacion_promedio

    return resultado

def obtener_mitad_de_maximo (lista_numeros):
    """Esta función pide como parametro una lista
    que tenga elementos del tipo int ó float para
    obtener su elemento máximo y luego dividir ese
    resultado a la mitad.

    Args:
        lista_de_numeros(list): lista de números 

    Returns:
        mitad_maximo(float): la mitad del número máximo obtenido
    """
    num_maximo = obtener_maximo(lista_numeros)

    mitad_maximo = num_maximo / 2

    return mitad_maximo

def bubble_sort_ascendente(lista_a_ordenar: list[int], lista_uno, lista_dos, lista_tres, lista_cuatro) -> list:
    """Esta función toma como parámetro una lista de números y
    ordena sus elementos de manera ascendente y retorna la lista
    modificada.

    Args:
        lista_a_ordenar(list[int]): lista de números

    Returns:
            *None*
    """

    for indice in range(len(lista_a_ordenar) - 1):

        for sub_indice in range (indice + 1 , len(lista_a_ordenar)):
            
            if lista_a_ordenar[indice] > lista_a_ordenar[sub_indice]:

                lista_a_ordenar[indice], lista_a_ordenar[sub_indice] =\
                lista_a_ordenar[sub_indice], lista_a_ordenar[indice]

    
def mostrar_datos_heroes(indice,lista_alturas,lista_generos,lista_identidades,
                                   lista_nombres,lista_poder):
    """
    """
    mensaje = f"Nombre: {lista_nombres[indice]:20} | "\
                f"Identidad: {lista_identidades[indice]:15} | "\
                f"Altura: {lista_alturas[indice]:8.1f} | "
    
    print(mensaje)
    
if __name__ == '__main__':
    mostrar_nombre()
    obtener_maximo()