from funciones import (
    mostrar_menu, play_sound, limpiar_pantalla,
    utn_mostrar_nombres_heroes, 
    utn_mostrar_identidades_heroes,
    utn_mostrar_heroe_mayor_altura,
    utn_mostrar_heroes_mas_fuertes,
    utn_filtrar_heroes_genero,
    utn_mostrar_heroes_poder_superior_promedio,
    utn_mostrar_heroes_mas_debiles
)

from validaciones import validar_opcion


def utn_heroes_app(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas):
    
    while True:
        
        mostrar_menu()
        opcion = validar_opcion(1, 10)
        play_sound()
        
        match opcion:
            case 1:
                utn_mostrar_nombres_heroes(lista_nombres)
            case 2:
                utn_mostrar_identidades_heroes(lista_identidades)
            case 3:
                utn_mostrar_heroe_mayor_altura(lista_alturas,lista_generos,lista_identidades,
                                               lista_nombres,lista_poderes)
            case 4:
                utn_mostrar_heroes_mas_fuertes(lista_alturas,lista_generos,lista_identidades,
                                               lista_nombres,lista_poderes)
            case 5:
                utn_filtrar_heroes_genero(lista_alturas,lista_generos,lista_identidades,
                                               lista_nombres,lista_poderes, "Femenino")
            case 6:
                utn_filtrar_heroes_genero(lista_alturas,lista_generos,lista_identidades,
                                               lista_nombres,lista_poderes, "Masculino")
            case 7:
                utn_filtrar_heroes_genero(lista_alturas,lista_generos,lista_identidades,
                                               lista_nombres,lista_poderes, "No-Binario")
            case 8:
                utn_mostrar_heroes_poder_superior_promedio(lista_alturas,lista_generos,lista_identidades,
                                               lista_nombres,lista_poderes)
            case 9:
                utn_mostrar_heroes_mas_debiles(lista_alturas,lista_generos,lista_identidades,
                                               lista_nombres,lista_poderes)
            case 10: # Salir del programa
                break
            
        limpiar_pantalla()
        