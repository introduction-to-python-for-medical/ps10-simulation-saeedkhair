import copy


def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    new_row = [0] * grid_size
    grid.append(new_row)
    for i in range(grid_size):
        grid[i].append(0)

        for j in range(grid_size):
            if grid[i][j] == 1:
                neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]]
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid
