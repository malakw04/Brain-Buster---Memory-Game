import random
import string 

class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [['X' for _ in range(size)] for _ in range(size)]
        self.pairs = self._generate_pairs()
        self.revealed_cells = set()


    def _generate_pairs(self):
        num_pairs = (self.size * self.size) // 2
        pairs = [i for i in range(num_pairs) for _ in range(2)]  
        random.shuffle(pairs)  
        cells = [(r, c) for r in range(self.size) for c in range(self.size)]  
        
        pairs_dict = {}
        for cell, value in zip(cells, pairs):
            pairs_dict[cell] = value  
        
        return pairs_dict


    def display_grid(self):
        print("----------------------")
        print("|    Brain Buster    |")
        print("----------------------")
        print()
        
        column_width = 3  
      
        header = "    " + "  ".join(f"[{chr(65 + i)}]" for i in range(self.size))  
        print(header)
        print()
        
      
        for i, row in enumerate(self.grid):
            row_display = f"[{i}] " + "  ".join(f"{cell:^{column_width}}" for cell in row) 
            print(row_display)
            print()
    

    def reveal_cell(self, row, col):
        if (row, col) not in self.revealed_cells:
            self.grid[row][col] = str(self.pairs[(row, col)]) 
            self.revealed_cells.add((row, col))  
            return self.pairs[(row, col)]
        return None


    def hide_cell(self, row, col):
        if (row, col) in self.revealed_cells:
            self.grid[row][col] = 'X'  
            self.revealed_cells.remove((row, col))  


    def reveal_grid(self):
        for (row, col), value in self.pairs.items():
            self.grid[row][col] = str(value) 
        self.display_grid() 


    def reset_grid(self):
        self.grid = [['X' for _ in range(self.size)] for _ in range(self.size)] 
        self.pairs = self._generate_pairs() 
        self.revealed_cells.clear()  

    def all_pairs_found(self):
        return len(self.revealed_cells) == self.size * self.size
