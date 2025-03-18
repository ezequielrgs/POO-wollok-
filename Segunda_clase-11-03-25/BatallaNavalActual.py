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
def disparo(coord_apuntada:tuple, grid:list)->list:

    pass
def intelligence(coords:tuple, grid:list, UsedCoords = [])->list:
   # UsedCoords = []
    if not UsedCoords: #Si UsedCoords no tiene coordenadas guardadas, el programa disparará automaticamente
        UsedCoords.append(coords)
        return disparo(coord_apuntada=coords, grid=grid)
    #En caso de si haber una coordenada, se investigará hacia que otras coordenadas se podría disparar
    new_grid = grid[:]#Creamos una copia de la grilla
    if coords in UsedCoords: #Si las coordenadas actuales ya fueron consultadas
        
        pass
    
    disparo()
    return new_grid, UsedCoords
    

def main() -> None:
    objs = input("Cuantos objetos quiere ingresar: ")
    cantidad = cantidad_objetos(c=int(objs))
    ix = input("X = ")
    iy = input("Y = ")
    grid = grilla(dimensiones=dimensiones(int(iy), int(ix)))

    for _ in range(cantidad):
        
        coords = generar_coords(grid)
        grid = proc(coords, grid)
        
    graficar(grid)


main()