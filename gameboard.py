class GameBoard:
    def __init__(self) -> None:
        self.grid = ''
        self.name = ''
        self.square = ''
        self.score_board = ''
        self.curser_x = 1
        self.curser_y = 1
        self.curser_position = "| c |"

    def update_board(self):
        pass

    def display_hit(self):
        pass

    def display_mist(self):
        pass
    
    def display_sunk_ships(self):
        pass

    def display_grid(self):
        
        self.grid = [["|   |" for a in range(3)] for b in range(3)]
        self.grid[self.curser_x][self.curser_y] = self.curser_position
        while True:
            for i in self.grid:
                print("----- ----- -----")
                print(" ".join(i))
                print("----- ----- -----")
        
            print("""Insructions:
            Up: W
            Down: S
            Left: A
            Right: D""")
            
            direction = input("Enter an option above to move the cursor :")
