#include <dirent.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define Size_of_grid_in_x 10
#define Size_of_grid_in_y 10

int CreateGid(){
    int* grid[Size_of_grid_in_y][Size_of_grid_in_x] = 0;
    return grid;
}

void ToPlaceObj(grid, coord){
    //grid[y][x] = 1;

}
int GetCoords(grid){
    int* coords[2] = {1, 0};
    return coords;
}
int main(){
    int grid = CreateGid();
    int *coords = GetCoords(grid);
    ToPlaceObj(grid, &coords);
    
}

