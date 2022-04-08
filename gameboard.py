from item import Item
from ship import Ship
class GameBoard:
    def __init__(self) -> None:
        self.grid = ''
        self.name = ''
        self.square = ''
        self.score_board = ''
        self.grid = [["[ ]" for y in range(10)] for x in range(10)]
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

    def place_ship(self, ship):
        pass

    def display_grid(self, item):
        self.grid[item.y][item.x] = item.identifyer
        for i in self.grid:
            print(" ".join(i))
        

    def move_item (self, item):
        while True:
            print(f"""Insructions:
            Up: w
            Down: s
            Left: a
            Right: d
            To place {item.name}, press SPACE BAR, then ENTER :""")
            self.move_direction = input(f"Enter an option above to move the {item.name} :")
            if self.move_direction == "w":
                self.grid[item.y][item.x] = "[ ]"
                item.y -= 1
                self.grid[item.y][item.x] = "[item.identifyer]"
            elif self.move_direction == "s":
                self.grid[item.y][item.x] = "[ ]"
                item.y += 1
                self.grid[item.y][item.x] = "[item.identifyer]"
            elif self.move_direction == "a":
                self.grid[item.y][item.x] = "[ ]"
                item.x -= 1
                self.grid[item.y][item.x] = "[item.identifyer]"
            elif self.move_direction == "d":
                self.grid[item.y][item.x] = "[ ]"
                item.x += 1
                self.grid[item.y][item.x] = "[item.identifyer]"
            elif self.move_direction == " ":
                break
            self.display_grid(item)

    def run_game(self):
        self.display_grid(self.curser)
        self.move_item(self.curser)