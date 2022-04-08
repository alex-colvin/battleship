from item import Item
class Ship(Item):
    def __init__(self, name, size, identifyer):
        super().__init__(name, size, identifyer)
        self.x_end = self.x + size - 1
        self.y_end = self.y + size - 1
        

    def display_ship_vertical(self):
        pass


        