from .auxiliares import obtener_maximo , promedio , obtener_mitad_de_maximo, mostrar_datos_heroes

def utn_mostrar_nombres_heroes(lista_nombres: list):
    """Esta función recibe como parámetro una lista(list)
    para luego recorrer sus elementos y mostrar en consola
    cada uno de los nombres de los héroes.

    Args:
        lista_nombres(list): la lista a recorrer

    Returns:
            *None*
    """
    for nombre in lista_nombres:
        print(nombre)


def utn_mostrar_identidades_heroes(lista_identidades: list):
    """Esta función recibe como parámetro una lista(list)
    para luego recorrer sus elementos y mostrar en consola
    cada una de las identidades de los héroes

    Args:
        lista_identidades(list): la lista a recorrer

    Returns:
            *None*
    """
    for nombre in lista_identidades:
        print(nombre)

def utn_mostrar_heroe_mayor_altura(lista_alturas,lista_generos,lista_identidades,
                                   lista_nombres,lista_poder):
    """Esta función recibe como parámetros 5 listas determinadas
    para luego recorrer los elementos de la lista_alturas y mostrar
    los datos del héroe con la mayor altura.

    Args:
        lista_alturas(list): la lista de alturas a recorrer y mostrar
        lista_generos(list): lista de generos a mostrar
        lista_identidades(list): lista de identidades a mostrar
        lista_nombres(list): lista de nombres a mostrar
        lista_poder(list): lista de poderes a mostrar

    Returns:
            *None*
    """
    # indice = 0
    heroe_mas_alto = obtener_maximo(lista_alturas)
    # indice_heroe_mas_alto = None
    # for valor in lista_alturas:
    #     if valor == heroe_mas_alto:
    #         indice_heroe_mas_alto = indice
    #     indice += 1
    for indice in range(len(lista_alturas)):
        if lista_alturas[indice] == heroe_mas_alto:
            mostrar_datos_heroes(indice,lista_alturas,lista_generos,lista_identidades,lista_nombres,lista_poder)
#     mensaje =\
#             f"""
# Héroe más alto: {lista_nombres[indice_heroe_mas_alto]}
# Altura: {lista_alturas[indice_heroe_mas_alto]}
# Identidad: {lista_identidades[indice_heroe_mas_alto]}
# Género: {lista_generos[indice_heroe_mas_alto]}
# Poder: {lista_poder[indice_heroe_mas_alto]}
        
#         """
#     print(mensaje)

def utn_mostrar_heroes_mas_fuertes(lista_alturas,lista_generos,lista_identidades,
                                   lista_nombres,lista_poder):
    """Esta función recibe como parámetros 5 listas determinadas
    para luego recorrer los elementos de la lista_poder y mostrar
    los datos del héroe con el mayor poder.

    Args:
        lista_alturas(list): lista de alturas a mostrar
        lista_generos(list): lista de generos a mostrar
        lista_identidades(list): lista de identidades a mostrar
        lista_nombres(list): lista de nombres a mostrar
        lista_poder(list): la lista de poderes a recorrer y mostrar

    Returns:
            *None*
    """
    indice = 0
    heroe_mas_poderoso = obtener_maximo(lista_poder)
    for valor in lista_poder:
        if valor == heroe_mas_poderoso:
            mensaje =\
            f"""
Héroe: {lista_nombres[indice]}
Altura: {lista_alturas[indice]}
Identidad: {lista_identidades[indice]}
Género: {lista_generos[indice]}
Poder: {lista_poder[indice]}
        
            """
            print(mensaje)
        indice += 1

def utn_filtrar_heroes_genero(lista_alturas,lista_generos,lista_identidades,
                                   lista_nombres,lista_poder,genero):
    """Esta función recibe como parámetros 5 listas determinadas y
    un género (Masculino, Femenino , No-Binario) 
    para luego recorrer los elementos de la lista_genero y según
    el género ingresado muestre:

    -El nombre (si es Femenino)
    -La identidad (si es Masculino)
    -El nombre y la identidad (si es No-Binario)

    Args:
        lista_alturas(list): lista de alturas 
        lista_generos(list): lista de generos a recorrer
        lista_identidades(list): lista de identidades a mostrar
        lista_nombres(list): lista de nombres a mostrar
        lista_poder(list): la lista de poderes 
        genero(str): el género (Masculino, Femenino, No-Binario)

    Returns:
            *None*
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
#estas listas son iguales, hacen lo mismo, por lo cual se podría utilizar para las mismas cosas

def utn_mostrar_heroes_poder_superior_promedio(lista_alturas,lista_generos,lista_identidades,
                                   lista_nombres,lista_poder):
    """Esta función recibe como parámetros 5 listas determinadas 
        para luego recorrer los elementos de la lista_poder y determinar
        un promedio.
        Luego compara ese promedio con los elementos de dicha lista y
        muestra el nombre y el poder de cada héroe por debajo del promedio.


        Args:
            lista_alturas(list): lista de alturas 
            lista_generos(list): lista de generos 
            lista_identidades(list): lista de identidades 
            lista_nombres(list): lista de nombres a mostrar
            lista_poder(list): la lista de poderes a recorrer y mostrar
            

        Returns:
                *None*
        """
    promedio_total = promedio(lista_poder)

    indice = 0 

    for valor in lista_poder:
        
        poder = valor

        if poder > promedio_total:
            mensaje =\
            f"""
Héroe: {lista_nombres[indice]}
Poder(por encima del {promedio_total}): {lista_poder[indice]}
        
            """
            print(mensaje)
        indice += 1


def utn_mostrar_heroes_mas_debiles (lista_alturas,lista_generos,lista_identidades,
                                   lista_nombres,lista_poder):
    """Esta función recibe como parámetros 5 listas determinadas 
        para luego recorrer los elementos de la lista_poder y determinar
        un cual es el máximo poder.
        Luego divide ese poder a la mitad y muestra los héroes que 
        están por debajo de ese 50%



        Args:
            lista_alturas(list): lista de alturas 
            lista_generos(list): lista de generos 
            lista_identidades(list): lista de identidades 
            lista_nombres(list): lista de nombres a mostrar
            lista_poder(list): la lista de poderes a recorrer y mostrar
            

        Returns:
                *None*
        """
    minimo_poder = obtener_mitad_de_maximo(lista_poder)
    indice = 0
    for poder in lista_poder:
        
        if poder < minimo_poder:
            mensaje =\
            f"""
Héroe: {lista_nombres[indice]}
Poder(por debajo {minimo_poder}): {lista_poder[indice]}
        
            """
            print(mensaje)
        indice += 1
        

