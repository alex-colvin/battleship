from gameboard import GameBoard
from ship import Ship

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.gameboard = GameBoard()
        self.destroyer = Ship("Destroyer", 2, "D")
        self.submarine = Ship("Submarine", 3, "S")
        self.battleship_1 = Ship("Battleship_1", 4, "B")
        self.battleship_2 = Ship("Battleship_2", 4, "B" )
        self.aircraft_carrier = Ship("Aircraft Carrier", 5, "A")
        self.ships = [self.destroyer, self.submarine, self.battleship_1, self.aircraft_carrier, self.battleship_2]


    def move_cursor(self):
        pass
    
    def set_ship(self):
        pass

    def move_ship(self):
        pass

    def rotate_ship(self):
        pass

    def fire(self, ships):
        # move the curser
        self.gameboard.get_move_input(self.gameboard.curser, ships)
        # select the position
        # check collision on other players board
        # if collision exists hit...else miss
        pass

    def place_ships(self):
        self.gameboard.get_move_input(self.battleship_1, self.ships)
        self.gameboard.get_move_input(self.battleship_2, self.ships)
        self.gameboard.get_move_input(self.aircraft_carrier, self.ships)
        self.gameboard.get_move_input(self.submarine, self.ships)
        self.gameboard.get_move_input(self.destroyer, self.ships)

    