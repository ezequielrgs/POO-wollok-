def dimensiones(x:int, y:int)->tuple:
    return (x, y)
def grilla(dimensiones:tuple)->list:
    future_grid = []

    for y in range(0, dimensiones[1]):
        eje_x=[]
        for x in range(0, dimensiones[0]):
            eje_x.append(0)

        future_grid.append(eje_x)
    return future_grid
        
    # return [[0 for _ in range(0, dimensiones[0])] for _ in range(0, dimensiones[1])] <-- Revisar la sintaxis
def colocar_objeto(grilla:list)->list:
    pass
def pedir_cantidad_objetos():
    return cantidad_objetos(c=int(input("Ingrese la cantidad de 'Barcos' que usted desee:\t")))
def cantidad_objetos(c)->int:
    #
    # Principalmente vamos a ingresar una cantidad de "barcos" a la fuerza,
    # para asegurarnos de la funcionalidad del código, en un futuro cuando el codigo esté
    # bien optimizado y debuggeado intentar que la cantidad sea al azar... #
    return c
def celda_vacia(grilla:list)->bool:
    #
    # if (bordes == 1)=> false
    #
    # array. #

    

    pass
def graficar(grilla:list)->None:
    #
    # **Grilla == [[0,0,0,0,0,0,0,0],
    #              [0,0,0,0,0,0,0,0],
    #               [0,0,0,0,0,0,0,0],
    #                  [0,0,0,0,0,0,0,0]
    # ]
    # Para GRAFICAR sería NECESARIO recorrer toda la grilla para imprimir cada una de las filas
    # con el objetivo de que aparezcan de forma ordenda. O sea 
    # [0,0,0,1,0,1],
    # [0,1,0,0,0,0],
    # [0,0,0,0,1,0],
    # ] #
    for fila in grilla:
        print(fila,"\n")




def main():
    pass