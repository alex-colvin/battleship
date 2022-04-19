from item import Item
from ship import Ship
import inspect
class GameBoard:
    def __init__(self) -> None:
        self.grid = ''
        self.name = ''
        self.square = ''
        self.score_board = ''
        self.grid = []
        self.curser = Item("Curser", 1, "I",10)
        self.hits_misses_curser = [self.curser]
        # self.hit = Item("Hit", 1, "X")
        # self.miss = Item("Miss", 1, "O")
        # self.destroyer = Ship("Destroyer", 2, "D")
        # self.submarine = Ship("Submarine", 3, "S")
        # self.battleship_1 = Ship("Battleship_1", 4, "B")
        # self.battleship_2 = Ship("Battleship_2", 4, "B" )
        # self.aircraft_carrier = Ship("Aircraft Carrier", 5, "A")
        self.move_direction = ''
        self.move_directions = ['a','s','d','w']
        # self.ships = [self.destroyer, self.submarine, self.battleship_1, self.aircraft_carrier, self.battleship_2]
        self.collision_exists = True
        self.sunk_ships = 0
        

    def update_board(self):
        pass

    def display_hit(self, x, y):
        hit = Item("Hit", 1, "X", x)
        hit.y = y
        hit.is_set = True
        self.hits_misses_curser.append(hit)
        self.mark_identifyer(hit)
        print("HIT!")

    def display_miss(self, x, y):
        miss = Item("Miss", 2, "O", x)
        miss.y = yield
        miss.is_set = True
        self.hits_misses_curser.append(miss)
        self.mark_identifyer(miss)
        print("MISS!")
    
    def display_sunk_ships(self):
        pass

    def check_collisions(self, item, items):
        if item.size > 1:
            item.generate_ship_coordinates()
        self.collision_exists = False
        for boat in items:
            if boat.name == item.name:
                pass
            elif item.is_vertical == True:
                self.check_vertical(item, boat)
            elif item.is_vertical == False:
                self.check_horizontal(item, boat)

    def check_vertical (self, item, boat):        
        if boat.is_vertical == True:
            if item.x == boat.x:                
                for z in boat.y_coordinates:
                    if item.size > 1:
                        for y in item.y_coordinates:                        
                            if y == z:
                                self.collision_exists = True
                                break
                    else:
                        if item.y == z:
                            self.collision_exists = True
                            break
        else:
            for x in boat.x_coordinates:
                if item.x == x:
                    if item.size > 1:
                        for y in item.y_coordinates:
                            if y == boat.y:
                                self.collision_exists = True
                    else:
                        if item.y == boat.y:
                            self.collision_exists = True

    def check_horizontal(self, item, boat):
        if boat.is_vertical == False:
            if item.y == boat.y:
                for w in boat.x_coordinates:
                    if item.size > 1:
                        for x in item.x_coordinates:                        
                                if x == w:
                                    self.collision_exists = True
                    else:
                        if item.x == w:
                            self.collision_exists = True
        else:
            for y in boat.y_coordinates:
                if item.y == y:
                    if item.size > 1:
                        for x in item.x_coordinates:
                            if x == boat.x:
                                self.collision_exists = True
                    else:
                        if item.x == boat.x:
                            self.collision_exists = True
                
            

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


    def display_set_items(self, items):
        for item in items:
            if item.is_set == True:
                self.mark_identifyer(item)
                
    def display_grid(self, item):
        for cell in self.grid:
            print(" ".join(cell))
    
    def generate_grid(self, rows, columns):
        for y in range(0, rows):
            self.grid.append(["[ ]" for x in range(0, columns)])

    def get_move_input (self, item, items):
        item.is_set = True
        self.display_set_items(items)
        if item.name != "Battleship_1":
            self.item_initial_display(item)
        while True:
            if item.name == "Curser":
                self.mark_identifyer(self.curser)
            self.display_set_items(items)  
            self.display_set_items(self.hits_misses_curser)      
            self.display_grid(item)
            print(f"""Insructions:
            Up: w
            Down: s
            Left: a
            Right: d
            Toggle ship vertical/horizontal: t
            Set {item.name} press SPACE BAR, then ENTER.""")
            self.move_direction = input(f"Enter an option above to move the {item.name} :")
            # self.move_direction = move_direction
            # move_direction = input(f"Enter an option above to move the {item.name} :")
            self.clear_item(item)
            self.move_item(item)
            if self.move_direction == " ":
                self.set(item, items, recipient=False)            
                break
            else:
                self.move_directions.append(self.move_direction)
                   
    def set(self, item, ships, recipient):
        if self.move_direction == " ":
            if item.name == 'Curser':
                item.x -= 10
                self.check_collisions(item, ships) 
                if recipient == False:
                    item.x += 10
                    if self.collision_exists == True:
                        self.display_hit(item.x, item.y)
                    else:
                        self.display_miss(item.x, item.y)
                item.x = 10
            else:
                self.collision_exists = True
                while self.collision_exists == True:
                    for move in self.move_directions[::-1]:          
                        self.check_collisions(item, ships)
                        if self.collision_exists == False:
                            break
                        self.move_direction = move
                        self.move_back(item)
        # if recipient == False:
        #     item.x += 10
        # if self.collision_exists == True:
        #     self.display_hit(item.x, item.y)
        # else:
        #     self.display_miss(item.x, item.y)


    def item_initial_display(self, item):#x is the right index
        if item.name == 'Curser':
            start = 10
            stop = 19
        else:
            start = 0
            stop = 9
        for x in range(start, stop, 1):
            n = 0
            for y in range(10):
                if self.grid[y][x] == '[ ]':
                    n += 1
                else:
                    n = 0
                if n == item.size:
                    item.x = x
                    item.y = y - item.size + 1
                    break
            if n == item.size:
                break

        # def generate_grid(self, rows, columns):
        # for y in range(0, rows):
        #     self.grid.append(["[ ]" for x in range(0, columns)])
        
    # def mark_identifyer(self, item):
    #     if item.size > 1:
    #         item.generate_ship_coordinates()
    #         if item.is_vertical == True:
    #                 for p in item.y_coordinates:
    #                     self.grid[p][item.x] = item.identifyer
    #         else:
    #             for p in item.x_coordinates:
    #                 self.grid[item.y][p] = item.identifyer
    #     elif item.size == 1:
    #         self.grid[item.y][item.x] = item.identifyer

            
    def move_item(self, item):
        #if item is ship use shipboard else use other board...fix math below
        board = isinstance(item, Ship)
        if board:
            x = 10
        else:
            x = 20        

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
            elif item.x == 0 :
                item.x = 9
            elif item.x == 10:
                item.x = 19
            else:
                item.x -= 1
        elif self.move_direction == "d":
            if item.x == 10 - item.size and item.is_vertical ==False:
                item.x = 0
            elif item.x == 9:
                item.x = 0
            elif item.x == 19:
                item.x = 10
            else:
                item.x += 1
        elif self.move_direction == 't':
            if item.x > 10 - item.size and item.is_vertical == True:
                pass
            elif item.y > 10 - item.size and item.is_vertical == False:
                pass
            else:
                item.toggle_vertical()               
        

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
            
    # def place_ships(self):
    #     self.get_move_input(self.battleship_1)
    #     self.get_move_input(self.battleship_2)
    #     self.get_move_input(self.aircraft_carrier)
    #     self.get_move_input(self.submarine)
    #     self.get_move_input(self.destroyer)

    def run_game(self):
        self.generate_grid(10, 20)
    
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
