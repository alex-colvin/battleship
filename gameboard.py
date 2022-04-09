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
        self.battleship_1 = Ship("battleship_1", 4, "B")
        self.battleship_2 = Ship("Battleship_2", 4, "B" )
        self.aircraft_carrier = Ship("Aircraft Carrier", 5, "A")
        self.move_direction = ''
        self.ships = [self.destroyer, self.submarine, self.battleship_1, self.aircraft_carrier, self.battleship_2]
        #make item, hit and miss an item and make an item class
        

    def update_board(self):
        pass

    def display_hit(self):
        pass

    def display_miss(self):
        pass
    
    def display_sunk_ships(self):
        pass
# working on checking collisions
# if vertical
#   for each ship in ships check 
        # if other ship vertical
#            if x axis matches
#               then loop through y ranges to check for matches
                    #if a y matches
                    #collision detected
#       # if other ship is horizontal#           
            # if x matches a number in other ships x range
                #check if y range contains other ships y
                    #collision detected
# if horizontal
    # for each ship in ships check
        #if other ship is horizontal
            #if y axis matches
                #loop through y ranges to check for matches
                    #if match
                    #collision
        #if other ship is vertical
            #if y matches a number if the other ships y range
                #check if x range contains other ships x
                    #collision
                #
#   
#   
#   
#
    def check_collisions(self):
        for ship in self.ships:


    def mark_identifyer(self, item):
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


    def display_set_ships(self):
        for ship in self.ships:
            if ship.is_set == True:
                self.mark_identifyer(ship)
                
    def display_grid(self, item):
        for cell in self.grid:
            print(" ".join(cell))
    
    def generate_grid(self, rows, columns):
        for y in range(0, rows):
            self.grid.append(["[ ]" for x in range(0, columns)])
    def move_item (self, item):
        item.is_set = True
        while True:
            self.display_set_ships()
            self.display_grid(item)
            print(f"""Insructions:
            Up: w
            Down: s
            Left: a
            Right: d
            Toggle ship vertical/horizontal: t
            Set {item.name}: press SPACE BAR, then ENTER.""")
            self.move_direction = input(f"Enter an option above to move the {item.name} :")
            self.clear_item(item)
            if self.move_direction == "w":
                if item.y == 0 and item.is_vertical == True:
                    item.y = 10 - item.size
                elif item.y == 0:
                    item.y = 9 
                else:
                    item.y -= 1
            elif self.move_direction == "s":
                if item.y == 10 - item.size and item.is_vertical == True:
                    item.y = 0
                elif item.y == 9:
                    item.y = 0
                else:
                    item.y += 1
            elif self.move_direction == "a":
                if item.x == 0 and item.is_vertical == False:
                    item.x = 10 - item.size
                elif item.x == 0:
                    item.x = 9
                else:
                    item.x -= 1
            elif self.move_direction == "d":
                if item.x == 10 - item.size and item.is_vertical ==False:
                    item.x = 0
                elif item.x == 9:
                    item.x = 0
                else:
                    item.x += 1
            elif self.move_direction == 't':
                if item.size > 1:
                    item.toggle_vertical()
            if self.move_direction == " ":
                item.is_set = True
                break
    def place_ships(self):
        self.move_item(self.battleship_1)
        self.move_item(self.battleship_2)
        self.move_item(self.aircraft_carrier)
        self.move_item(self.submarine)
        self.move_item(self.destroyer)

    def run_game(self):
        self.generate_grid(10, 10)
        self.place_ships()
    
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
