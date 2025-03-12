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
def colocar_objeto(c:int,grilla:list, coord:list )->list:
    new_grid = grilla[:]
    x = coord[0]
    y = coord[1]

    for _ in range (0, c):
        try:
            if verif_celdas(grid= grilla, obj_coords=(x,y)):
                new_grid[y][x]=1 
            return new_grid
        except:
            raise "Error"

def verif_celdas(obj_coords:tuple, grid: list, is_valid = True) -> bool:
    #print("A estas coordenadas llega nuestro objeto:{}\n".format(obj_coords))
   # is_valid = True
    for y in range(obj_coords[1]-1,obj_coords[1]+1):
        for x in range(obj_coords[0]-1, obj_coords[0]+1):
            current_coord = grid[y][x]
            print("La pieza actual es:", current_coord, "Y ésto sale en verif:", grid[y][x], "en las coordenadas: {}".format((x,y)) )
            is_valid = celda_vacia(current_coord=current_coord, is_valid=is_valid)
        #if not is_valid : break
    
    return is_valid
    
    
def pedir_cantidad_objetos():
    return cantidad_objetos(c=int(input('Ingrese la cantidad de "Barcos" que usted desee:\t')))
def cantidad_objetos(c=1)->int:
    #
    # Principalmente vamos a ingresar una cantidad de "barcos" a la fuerza,
    # para asegurarnos de la funcionalidad del código, en un futuro cuando el codigo esté
    # bien optimizado y debuggeado intentar que la cantidad sea al azar... #
    return c
def celda_vacia(is_valid:bool,current_coord:int)->bool:
    #
    # if (bordes == 1)=> false
    #
    # array. #
    
   
    if (current_coord != 0 and current_coord!=None):
        is_valid = False

    return is_valid

    
def graficar(grilla:list)->None:
    #
    # **Grilla == [[0,0,0,0,0,0,0,0],
    # **             [0,0,0,0,0,0,0,0],
    # **              [0,0,0,0,0,0,0,0],
    # **                 [0,0,0,0,0,0,0,0]
    # **                                    ]
    # ***Para GRAFICAR sería NECESARIO recorrer toda la grilla para imprimir cada una de las filas
    # ***con el objetivo de que aparezcan de forma ordenda. O sea 
    # [
    # **[0,0,0,1,0,1],
    # **[0,1,0,0,0,0],
    # **[0,0,0,0,1,0]
    # *                 ] #
    for fila in grilla:
        print(fila,"\n")




def main():
    grid = grilla((10, 10))
    print("La grilla original es:\n\t{}".format(graficar))
    from random import randint
    while True:
        coords_of_object = (randint(0, len(grid)), randint(0,len(grid[0])))
        try:
            #colocar_objeto(c=randint(0,3), grilla=grid, coord=coord_of_object) if verif_celdas(obj_coords=coord_of_object, grid=grid) else print(-1)
            if(verif_celdas(coords_of_object, grid)):
                colocar_objeto(c=cantidad_objetos(), grilla=grid, coord=coords_of_object)
            else:
                raise "No se puede colocar"
            graficar(grid)
            usr_want_to_break=input("Do you want to break the program? <Yes/no> \n\t")
            if usr_want_to_break.upper() == "YES":
                break
        except IndexError:
            continue
main()