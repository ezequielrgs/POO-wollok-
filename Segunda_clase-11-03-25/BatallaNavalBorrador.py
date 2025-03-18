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
def colocar_objeto(grilla:list, coord:list, c=1)->list:
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
    cont=0 #Contdor que se utilizará por si salta un 1 en el centro
    for y in range(obj_coords[1]-1,obj_coords[1]+1):
        for x in range(obj_coords[0]-1, obj_coords[0]+1):
            current_coord = grid[y][x]
            print("La pieza actual es:", current_coord, "Y ésto sale en verif:", grid[y][x], "en las coordenadas: {}".format((x,y)) )
            
            validar = celda_vacia(current_coord=current_coord, is_valid=is_valid)
            is_valid = validar[0]
            if is_valid is False:
                print("Se ingresó al contador.")
                cont+=1
            elif cont>1:
                return is_valid
            
    print("Esto va a devolver verif:", is_valid)
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
    
    
    if (current_coord != 0 and current_coord!=None or current_coord == 2):
        is_valid = False
    current_coord = 2
    
    return is_valid, current_coord

    
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



def generar_coords(grid):
    from random import randint
    coords_of_object = (randint(0,len(grid[0])-1),randint(0, len(grid)-1))
    return coords_of_object
    
def vlid_coord(coords:tuple, grid:list)->bool:
    print(coords)
    if coords[0] < 0 or coords[0] >= len(grid[0]):
        return False
    if coords[1] < 0 or coords[1] >= len(grid):
        return False
    print("Las cordenadas {} son validas".format(coords))
    return True
    
    pass
def proc(coords, grid):
    
    graficar(grid)
    
    if verif_celdas(coords, grid) and vlid_coord(coords, grid):
        colocar_objeto(grid, coords)

def main():
    cantidad = cantidad_objetos(c=int(input("Cuantos objetos quire ingresar:")))
    
    for _ in range(cantidad):
        grid = grilla(dimensiones=dimensiones(int(input("X = ")), int(input("Y = "))))
        coords=generar_coords(grid)
        proc()
        #print("\nY verificar celdas devuelve:",verif_celdas(coords, grid))
main()