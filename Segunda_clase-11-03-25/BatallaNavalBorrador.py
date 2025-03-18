def dimensiones(x: int, y: int) -> tuple:
    return (x, y)


def grilla(dimensiones: tuple) -> list:
    return [[0 for _ in range(dimensiones[0])] for _ in range(dimensiones[1])]


def colocar_objeto(grilla: list, coord: list, c=1) -> list:
    new_grid = [fila[:] for fila in grilla]
    y, x = coord[0], coord[1]


    for _ in range(c):
        try:
            if verif_celdas(grid=grilla, obj_coords=(y, x)):
                new_grid[y][x] = 1
            return new_grid
        except:
            raise "Error"


def verif_celdas(obj_coords: tuple, grid: list, is_valid=True) -> bool:
    lenx = len(grid[0])
    leny = len(grid)
    LimiteSup = max(obj_coords[0] - 1, 0)
    LimiteIzq = max(obj_coords[1] - 1, 0)
    LimiteInf = min(obj_coords[0] + 1, leny) #Obtengo el límite inferior procurando que no se tomen coordenadas invalidas
    LimiteDer = min(obj_coords[1] + 1, lenx) # Obtenemos el límite derecho procurando que no se tomen coords invalidas.
    is_valid = True
    for y in range(LimiteSup, min(leny, LimiteInf+1)):
        for x in range(LimiteIzq, min(lenx, LimiteDer+1)):
            current_coord = grid[y][x]
            is_valid = celda_vacia(current_coord)
            if is_valid==False:
                break
        if is_valid==False:
            break
    #print(f"Esto va a devolver verif: {is_valid}")
    return is_valid


def pedir_cantidad_objetos() -> int:
    return cantidad_objetos(c=int(input('Ingrese la cantidad de "Barcos" que usted desee:\t')))


def cantidad_objetos(c=1) -> int:
    return c


def celda_vacia(current_coord: int):
    if current_coord != 0:
        return False
    return True


def graficar(grilla: list) -> None:
    for fila in grilla:
        print(fila, "\n")


def generar_coords(grid: list) -> tuple:
    from random import randint
    return (randint(0, len(grid[0]) - 1), (randint(0, len(grid) - 1)))


def proc(coords: tuple, grid: list) -> None:
    if verif_celdas(coords, grid):
        return colocar_objeto(grid, coords)
    else:
        #print("posicion invalida ", coords)
        return grid


def Boat_downed(cell:list)->list:
    cell = 2
    return cell

def are_cell_empty(aim)->bool:
    if aim == 1:
        return True
    elif aim != 1: 
        return False

def disparo(coord_apuntada:tuple, grid:list)->list:
    """bool_and_aiming = [grid[coord_apuntada[0]][coord_apuntada[1]],grid[coord_apuntada[0]][coord_apuntada[1]] == 1]
    if bool_and_aiming[1]:
        bool_and_aiming[0] = Boat_downed(shoot=bool_and_aiming) 
        print("Se está retornando esto en Bool_and_aiming{}".format(bool_and_aiming))
        return bool_and_aiming
    else:
        None
    """
    print("Estas son las coordenadas recibidas: \t{}\n".format(coord_apuntada))
    x,y,= coord_apuntada[1], coord_apuntada[0] 
    aiming = grid[y][x]
   # print("Esto vale MyBool:\t{}\n".format(aiming == 1))
    is_a_boat = are_cell_empty(aiming)
    if is_a_boat:
       # print("Así está la asignacion:\t{}\n".format(Boat_downed(shoot=aiming)))
        grid[y][x] = Boat_downed(aiming)
        return [grid, is_a_boat]
    return [grid, is_a_boat]
    
    #MyBool if return Boat_downed(shoot=aiming) else 

def intelligence(coords:tuple, grid:list, UsedCoords = [])->list:
   # UsedCoords = []
    if not UsedCoords: #Si UsedCoords no tiene coordenadas guardadas, el programa disparará automaticamente
        UsedCoords.append(coords)
        return disparo(coord_apuntada=coords, grid=grid)
    if disparo(coord_apuntada=coords, grid=grid)[1]:
        print("El barcho debió hundirse")
        grid[coords[1]][coords[0]] = 2
        return grid
    print("Se ha disparado a las coordenadas incorrectas")
    #En caso de si haber una coordenada, se investigará hacia que otras coordenadas se podría disparar
    
    new_grid = grid[:]#Creamos una copia de la grilla por las dudas
    
    if not coords in UsedCoords: # Si las coordenadas actuales ya fueron consultadas
        UsedCoords.append(coords)
        shoot = disparo(coord_apuntada=coords, grid=new_grid) # En caso de tratarse de coordenadas no utilizadas anteriormente efectuamos el disparo.
        if shoot[1] is True:
            return [new_grid, True]
    elif coords in UsedCoords:
        
        #return intelligence(new_grid, UsedCoords.append(coords))
        pass
    else:
        raise "Error"

def main() -> None:
    from random import randint
    objs = input("Cuantos objetos quiere ingresar: ") 
    cantidad = cantidad_objetos(c=int(objs))
    ix = input("X = ")
    iy = input("Y = ")
    grid = grilla(dimensiones=dimensiones(int(iy), int(ix)))

    for _ in range(cantidad):
        
        coords = generar_coords(grid)
        grid = proc(coords, grid)
        
    graficar(grid)
    for _ in range(0,3):
        coord_apuntada = (randint(0, len(grid)-1), randint(0, len(grid[0])-1)) 
        IA = intelligence(coords=coord_apuntada, grid= grid)  #Esto debe devolver la actualizacion de la grilla con el disparo efectuado y un valor booleano que determine el undiemiento de algún barco.


    """
    while True:
        coord_apuntada = (randint(0, len(grid)), randint(0, len(grid[0]))) 
        IA = intelligence(coords=coord_apuntada, grid= grid) #Esto debe devolver la actualizacion de la grilla con el disparo efectuado y un valor booleano que determine el undiemiento de algún barco.

        print(IA[0])

        if IA[1]: # Este condicional debería evaluar si se hundió o no un barco.

            break
    """

main()