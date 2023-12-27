import random

class Sudoku():
    def __init__(self, grid):
        self.grid = grid
    
    
    def available_pos(self, val, row, col) -> bool:
        block_i = (row // 3) * 3
        block_j = (col // 3) * 3
        
        for b_i in range(block_i, block_i + 3):
            for b_j in range(block_j, block_j + 3):
                if self.grid[b_i][b_j] == val:
                    return False
                
        for j in range(9):
            if self.grid[row][j] == val:
                return False
            
        for i in range(9):
            if self.grid[i][col] == val:
                return False
            
        return True
        
    
    def start_element(self):
        for i in range(9):
            for j in range(9):
                if  self.grid[i][j] == 0:
                    return i,j
        
        return -1,-1
    
    def solve(self) -> bool:
        
        i, j = self.start_element()
        
        if i == -1 and j == -1:
            return True
        
        for num in range(1, 10):
            if self.available_pos(num, i, j):
                self.grid[i][j] = num
                
                if self.solve():
                    return True
                
                self.grid[i][j] = 0
                
        return False
        
        
    def print_grid(self):   
        for row in self.grid:
            print(row)
  
  
# class Generate_Table():
    # def __init__(self):
    #     self.generated_grid = [[0] * 9 for _ in range(9)]
    #     self.sudoku = Sudoku()
        
    # def available_pos(self, grid, val, row, col):
    #     return self.sudoku.available_pos(grid, val, row, col)  
    
    # def Generate(self):
    #     for i in range(9):
    #         row = []
    #         for j in range(9):
    #             num = random.randint(0, 9)
    #             if self.available_pos(self.generated_grid, num, i, j):
    #                 row.append(num)
    #         self.generated_grid[i] = row
            
    #     print(self.generated_grid)
            
    # def print_grid(self):   
    #     for i in range(9):
    #         for j in range(9):
    #             print(self.generated_grid[i][j])
        
        
  
    
def main():
    
    grid=[
    [0,8,0,5,3,0,2,7,6],
    [0,5,0,6,0,0,0,0,0],
    [6,1,3,0,0,0,0,0,0],
    [0,0,6,0,5,0,0,0,0],
    [0,3,2,0,0,0,7,0,1],
    [7,4,5,0,0,8,6,9,3],
    [0,7,0,9,6,0,5,0,0],
    [4,0,0,1,8,0,0,6,7],
    [5,0,0,0,0,4,8,2,9]
    ]
    
    # generated_grid = Generate_Table()
    # generated_grid.Generate()
    
    solve_sudoku = Sudoku(grid)
    
    if solve_sudoku.solve():
        solve_sudoku.print_grid()
    
    

if __name__ == '__main__':
    main()
    
        