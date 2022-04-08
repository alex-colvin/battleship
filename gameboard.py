from item import Item
from ship import Ship
class GameBoard:
    def __init__(self) -> None:
        self.grid = ''
        self.name = ''
        self.square = ''
        self.score_board = ''
        self.grid = []
        self.curser = Item("Curser", 1, "I")
        self.hit = Item("Hit", 1, "X")
        self.miss = Item("Miss", 1, "O")
        self.destroyer = Ship("Destroyer", 2, "D")
        self.submarine = Ship("Submarine", 3, "S")
        self.battleship = Ship("Battleship", 4, "B")
        self.aircraft_carrier = Ship("Aircraft Carrier", 5, "A")
        self.move_direction = ''
        #make item, hit and miss an item and make an item class
        

    def update_board(self):
        pass

    def display_hit(self):
        pass

    def display_mist(self):
        pass
    
    def display_sunk_ships(self):
        pass

    def display_ship_on_grid(self, ship):
        
        self.display_item_grid(ship)

    def clear_ship(self, ship):
        pass
         
    def display_item_grid(self, item):
        if item.size > 1:
            item.generate_ship_coordinates()
            if item.is_vertical == True:
                for p in item.y_coordinates:
                    self.grid[p][item.x] = item.identifyer
            else:
                for p in item.x_coordinates:
                    self.grid[item.y][p] = item.identifyer
        elif item.size == 1:
            self.grid[item.y][item.x] = item.identifyer
        for cell in self.grid:
            print(" ".join(cell))
    
    def generate_grid(self, rows, columns):
        for y in range(0, rows):
            self.grid.append(["[ ]" for x in range(0, columns)])
#working on moving ships around and boundaries...
    def move_item (self, item):
        self.display_item_grid(item)
        while True:
            print(f"""Insructions:
            Up: w
            Down: s
            Left: a
            Right: d
            To place {item.name}, press SPACE BAR, then ENTER :""")
            self.move_direction = input(f"Enter an option above to move the {item.name} :")
            self.clear_item(item)
            if self.move_direction == "w":
                if item.y == 0:
                    item.y = 10 - item.size
                else:
                    item.y -= 1
            elif self.move_direction == "s":
                if item.y == 9:
                    item.y = 0
                else:
                    item.y += 1
            elif self.move_direction == "a":
                if item.x == 0:
                    item.x = 9
                else:
                    item.x -= 1
            elif self.move_direction == "d":
                if item.x == 9 + item.size == 10:
                    item.x = 0
                else:
                    item.x += 1
            self.display_item_grid(item)
            if self.move_direction == " ":
                break
        
    def run_game(self):
        self.generate_grid(10, 10)
        self.move_item(self.curser)
        self.move_item(self.battleship)
    
    def clear_item(self, item):
        if item.size > 1:
            if item.is_vertical == True:
                for p in item.y_coordinates:
                    self.grid[p][item.x] = "[ ]"
            else:
                for p in item.x_coordinates:
                    self.grid[item.y][p] = "[ ]"
            item.clear_coordinates()
        else:
            self.grid[item.y][item.x] = "[ ]"
    
    # def populate_item(self, item):
        # self.grid[item.y][item.x] = "[item.identifyer]"
