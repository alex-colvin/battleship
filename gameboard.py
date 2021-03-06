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
        self.collision_exists = False
        #make item, hit and miss an item and make an item class
        

    def update_board(self):
        pass

    def display_hit(self):
        pass

    def display_miss(self):
        pass
    
    def display_sunk_ships(self):
        pass

    def check_collisions(self, ship):
        ship.generate_ship_coordinates()
        for boat in self.ships:
            if boat.name == ship.name:
                pass
            elif ship.is_vertical == True:
                if boat.is_vertical == True:
                    if ship.x == boat.x:
                        for y in ship.y_coordinates:
                            for z in boat.y_coordinates:
                                if y == z:
                                    self.collision_exists = True
                                    break
                else:
                    for x in boat.x_coordinates:
                        if ship.x == x:
                            for y in ship.y_coordinates:
                                if y == boat.y:
                                    self.collision_exists = True
            else:
                if boat.is_vertical == False:
                    if ship.y == boat.y:
                        for x in ship.x_coordinates:
                            for w in boat.x_coordinates:
                                if x == w:
                                    self.collision_exists = True
                else:
                    for y in boat.y_coordinates:
                        if ship.y == y:
                            for x in ship.x_coordinates:
                                if x == boat.y:
                                    self.collision_exists = True

#   PLACE COLLISION DETECTION INISDE MOVE ITEM IF " " IS SELECTED
#   TO SEPARATE GRIDS PLACE | AT X 10 
#   EXPAND GRIDS TO X 20
#   GRID.Y 0 LINE SHOULD HAVE MY SHIPS AND ENEMY SHIPS HEADER
    


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
    def get_move_input (self, item):
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
            self.move_item(item)
            if self.move_direction == " ":
                break

    def move_item(self, item):
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

        self.check_collisions(item)
        if self.collision_exists == True:
            self.move_back(item)
        
        

    def move_back(self, item):
        if self.collision_exists == True:
            if self.move_direction == "w":
                self.move_direction = "s"
            elif self.move_direction == "s":
                self.move_direction = "w"
            elif self.move_direction == "a":
                self.move_direction = "d"
            elif self.move_direction == "d":
                self.move_direction = "a"
        self.collision_exists = False
        self.move_item(item)
    


        self.move_direction = self.move_direction
            
    def place_ships(self):
        self.get_move_input(self.battleship_1)
        self.get_move_input(self.battleship_2)
        self.get_move_input(self.aircraft_carrier)
        self.get_move_input(self.submarine)
        self.get_move_input(self.destroyer)

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
