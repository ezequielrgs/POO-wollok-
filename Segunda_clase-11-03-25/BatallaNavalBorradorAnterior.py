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
    ly = max(obj_coords[0] - 1, 0)
    lx = max(obj_coords[1] - 1, 0)
    by = min(obj_coords[0] + 1, leny)
    bx = min(obj_coords[1] + 1, lenx)
    is_valid = True
    for y in range(ly, min(leny, by+1)):
        for x in range(lx, min(lenx, bx+1)):
            current_coord = grid[y][x]
            is_valid = celda_vacia(current_coord)
            if is_valid==False:
                break
        if is_valid==False:
            break
    return is_valid


def pedir_cantidad_objetos() -> int:
    return cantidad_objetos(c=int(input('Ingrese la cantidad de "Barcos" que usted desee:\t')))


def cantidad_objetos(c=1) -> int:
    return c


def celda_vacia(current_coord: int):
    return current_coord == 0


def graficar(grilla: list) -> None:
    for fila in grilla:
        print(fila, "\n")

def proc(coords: tuple, grid: list) -> None:
    if verif_celdas(coords, grid):
        return colocar_objeto(grid, coords)
    else:
        return grid

def are_cell_empty(aim)->bool:
        return aim == 1

def disparo(coord_apuntada:tuple, grid:list)->list:
    print("Estas son las coordenadas recibidas: \t{}\n".format(coord_apuntada))
    x,y,= coord_apuntada[1], coord_apuntada[0] 
    aiming = grid[y][x]
   # print("Esto vale MyBool:\t{}\n".format(aiming == 1))
    is_a_boat = are_cell_empty(aiming)
    

    if is_a_boat:
       # print("Así está la asignacion:\t{}\n".format(Boat_downed(shoot=aiming)))
        grid[y][x] = 2
        return [grid, is_a_boat]
    return [grid, is_a_boat]


def intelligence(coords:tuple, grid:list, UsedCoords = [])->list:
   # UsedCoords = []
    if not UsedCoords: #Si UsedCoords no tiene coordenadas guardadas, el programa disparará automaticamente
        UsedCoords.append(coords)
        return disparo(coord_apuntada=coords, grid=grid)
    
    if disparo(coord_apuntada=coords, grid=grid)[1]:
        print("El barco debió hundirse")
        grid[coords[1]][coords[0]] = 2
        return grid
    print("Se ha disparado a las coordenadas incorrectas")
    
    new_grid = grid[:]
    
    if not coords in UsedCoords:
        UsedCoords.append(coords)
        new_grid, collapse = disparo(coord_apuntada=coords, grid=new_grid)
        if collapse[1] is True:
            new_grid = collapse[0]
            return [new_grid, True]
    elif coords in UsedCoords:
        pass
    else:
        raise "Error"

def aiming(grid:list)->tuple: 
    from random import randint
    return (randint(0, len(grid) -1), randint(0, len(grid[0]) - 1))

def main() -> None:
    objs = input("Cuantos objetos quiere ingresar: ")
    cantidad = cantidad_objetos(c=int(objs))
    ix = input("X = ")
    iy = input("Y = ")
    grid = grilla(dimensiones=dimensiones(int(iy), int(ix)))

    for _ in range(cantidad):
        
        coords = aiming(grid)
        grid = proc(coords, grid)
        
    graficar(grid)
    used_coords = [[], []]
    for attemps in range(0, 100): 
        aiming_coords = aiming(grid)
        if not aiming_coords in used_coords[0] and not aiming_coords in used_coords[1]:    
            res_shoot = disparo(coord_apuntada=aiming_coords, grid= grid)
            if res_shoot == -1:
                used_coords[0].append(aiming_coords)
            elif res_shoot != -1:
                used_coords[1].append(aiming_coords)
    print(graficar(grid))
    print(used_coords)
    

main()