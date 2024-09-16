from data_heroes import *
from funciones import *

#print(lista_identidades_heroes)

#pruebo las funciones de aca para saber si esta todo ok ,
#

# def mostrar_nombre(lista_de_nombres:list, indice:int) :
#     """pide una lista de nombres y un índice,
#     para luego retornar un elemento de la lista según
#     el índice pedido.

#     Args:
#         lista_de_nombres(list): la lista de nombres 
#         indice(int): posición del elemento a retornar 
#                     de la lista


#     Returns:
#         nombre_a_mostrar(str): el elemento en base al índice
#                             ingresado
    
#     """
#     nombre_a_mostrar = lista_de_nombres[indice - 1]
    
#     return nombre_a_mostrar

# def obtener_maximo(lista_de_numeros:list) -> float:
#     """
#     """
#     valor_maximo = None

#     for valor in lista_de_numeros:
        
#         if valor_maximo == None: 
#             valor_maximo = valor
#         else:
#             if valor > valor_maximo :
#                 valor_maximo = valor

#     return float(valor_maximo)

# print(obtener_maximo(lista_alturas_heroes))

# def utn_mostrar_heroe_mayor_altura(lista_alturas,lista_generos,lista_identidades,
#                                    lista_nombres,lista_poder):
#     """
#     """
#     indice = 0
#     heroe_mas_alto = obtener_maximo(lista_alturas)
#     indice_heroe_mas_alto = None
#     for valor in lista_alturas:
#         if valor == heroe_mas_alto:
#             indice_heroe_mas_alto = indice
#         indice += 1
    
#     mensaje =\
#             f"""
# Héroe más alto: {lista_nombres[indice_heroe_mas_alto]}
# Altura: {lista_alturas[indice_heroe_mas_alto]}
# Identidad: {lista_identidades[indice_heroe_mas_alto]}
# Género: {lista_generos[indice_heroe_mas_alto]}
# Poder: {lista_poder[indice_heroe_mas_alto]}
        
#         """
#     print(mensaje)


# utn_mostrar_heroe_mayor_altura(lista_alturas_heroes,lista_generos_heroes,lista_identidades_heroes,
#                                lista_nombres_heroes,lista_poder_heroes)

# def utn_mostrar_heroes_mas_fuertes(lista_alturas,lista_generos,lista_identidades,
#                                    lista_nombres,lista_poder):
#     """
#     """
#     indice = 0
#     heroe_mas_poderoso = obtener_maximo(lista_poder)
#     for valor in lista_poder:
#         if valor == heroe_mas_poderoso:
#             mensaje =\
#             f"""
# Héroe más alto: {lista_nombres[indice]}
# Altura: {lista_alturas[indice]}
# Identidad: {lista_identidades[indice]}
# Género: {lista_generos[indice]}
# Poder: {lista_poder[indice]}
        
#             """
#             print(mensaje)
#         indice += 1

# utn_mostrar_heroes_mas_fuertes(lista_alturas_heroes,lista_generos_heroes,lista_identidades_heroes,
#                                 lista_nombres_heroes,lista_poder_heroes)

# def utn_filtrar_heroes_genero(lista_alturas,lista_generos,lista_identidades,
#                                    lista_nombres,lista_poder,genero):
#     """
#     """
    
#     indice = 0
#     for valor in lista_generos:
#         genero_encontrado = valor
        
#         if genero_encontrado == genero:
#             mensaje =\
#             f"""
# Héroe más alto: {lista_nombres[indice]}
# Altura: {lista_alturas[indice]}
# Identidad: {lista_identidades[indice]}
# Género: {lista_generos[indice]}
# Poder: {lista_poder[indice]}
        
#             """
#             print(mensaje)
#         indice += 1
        

# genero = input("Ingrese un género: ")

# utn_filtrar_heroes_genero(lista_alturas_heroes,lista_generos_heroes,lista_identidades_heroes,
#                                   lista_nombres_heroes,lista_poder_heroes,genero)

# utn_mostrar_heroes_mas_fuertes(lista_alturas_heroes,lista_generos_heroes,lista_identidades_heroes,
#                                  lista_nombres_heroes,lista_poder_heroes,)

# def seleccionar_genero():
    
    
#     opcion_genero = input (f"Seleccione un género:\n1- Masculino\n2- Femenino\n3- No-Binario\n")
    

#     match(opcion_genero):
#         case("1"):
#             genero = "Masculino"
#         case("2"):
#             genero = "Femenino"
#         case("3"):
#             genero = "No-Binario"
#         case _:
#             genero = seleccionar_genero()

#     return genero

# print(seleccionar_genero())

# def promedio(lista_de_numeros:list) -> float:
#     """
#     """
#     suma_numeros = 0
#     contador_de_vueltas = 0
#     for valor in lista_de_numeros:
#         suma_numeros += valor
#         contador_de_vueltas += 1

#     operacion_promedio = suma_numeros / contador_de_vueltas
    
#     resultado = operacion_promedio

#     return resultado


# print(promedio(lista_poder_heroes))

# def utn_mostrar_heroes_poder_superior_promedio(lista_alturas,lista_generos,lista_identidades,
#                                    lista_nombres,lista_poder):
#     """
#     """
#     promedio_total = promedio(lista_poder)

#     indice = 0 

#     for valor in lista_poder:
        
#         poder = valor

#         if poder > promedio_total:
#             mensaje =\
#             f"""
# Héroe: {lista_nombres[indice]}
# Altura: {lista_alturas[indice]}
# Identidad: {lista_identidades[indice]}
# Género: {lista_generos[indice]}
# Poder(por encima del {promedio_total}): {lista_poder[indice]}
        
#             """
#             print(mensaje)
#         indice += 1

# utn_mostrar_heroes_poder_superior_promedio(lista_alturas_heroes,lista_generos_heroes,lista_identidades_heroes,
#                                   lista_nombres_heroes,lista_poder_heroes)

# def utn_mostrar_heroes_mas_debiles (lista_alturas,lista_generos,lista_identidades,
#                                    lista_nombres,lista_poder):
#     """
#     """
#     minimo_poder = obtener_mitad_de_maximo(lista_poder)

#     indice = 0

#     for poder in lista_poder:
        
#         if poder < minimo_poder:
#             mensaje =\
#             f"""
# Héroe: {lista_nombres[indice]}
# Altura: {lista_alturas[indice]}
# Identidad: {lista_identidades[indice]}
# Género: {lista_generos[indice]}
# Poder(por debajo {minimo_poder}): {lista_poder[indice]}
        
#             """
#             print(mensaje)
#         indice += 1

# utn_mostrar_heroes_mas_debiles(lista_alturas_heroes,lista_generos_heroes,lista_identidades_heroes,
#                                    lista_nombres_heroes,lista_poder_heroes)

def utn_filtrar_heroes_genero(lista_alturas,lista_generos,lista_identidades,
                                   lista_nombres,lista_poder,genero):
    """
    """
    
    indice = 0
    for valor in lista_generos:
        genero_encontrado = valor

        if genero == genero_encontrado:
            match(genero_encontrado):
                case("Femenino"):
                    mensaje =f"Héroe: {lista_nombres[indice]}"
                case("Masculino"):
                    mensaje =f"Identidad: {lista_identidades[indice]}"
                case("No-Binario"):
                    mensaje =f"Héroe: {lista_nombres[indice]}\nIdentidad: {lista_identidades[indice]}"

            print(mensaje)
        
        indice += 1



utn_filtrar_heroes_genero(lista_alturas_heroes,lista_generos_heroes,lista_identidades_heroes,
                                    lista_nombres_heroes,lista_poder_heroes, "Femenino")