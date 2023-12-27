class Sudoku():
    def __init__():
        pass
    
    def available_pos(self, grid) -> bool:
        pass
    
    def start_element(self, grid):
        for i in range(9):
            for j in range(9):
                if  grid[i][j] == '0':
                    return i,j
        
        return -1,-1
    
    def solve(self, grid) -> bool:
        pass
    
    def print_grid(self, gird):
        pass
    
    
def main():
    
    grid=[
    ["0","8","0","5","3","0","2","7","6"],
    ["0","5","0","6","0","0","0","0","0"],
    ["6","1","3","0","0","0","0","0","0"],
    ["0","0","6","0","5","0","0","0","0"],
    ["0","3","2","0","0","0","7","0","1"],
    ["7","4","5","0","0","8","6","9","3"],
    ["0","7","0","9","6","0","5","0","0"],
    ["4","0","0","1","8","0","0","6","7"],
    ["5","0","0","0","0","4","8","2","9"]
    ]
    
    solve_sudoku = Sudoku()
    
    if solve_sudoku.solve(grid):
        solve_sudoku.print_grid(gird)
    

if __name__ == '__main__':
    main()
    
        