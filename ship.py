from item import Item
class Ship(Item):
    def __init__(self, name, size, identifyer):
        super().__init__(name, size, identifyer, x_start=0)
        self.x_end = self.x + self.size
        self.y_end = self.y + self.size
        self.x_coordinates = []
        self.y_coordinates = []
        self.is_vertical = True

    def generate_ship_coordinates(self):
        self.clear_coordinates()
        if self.is_vertical == True:
            self.y_end = self.y + self.size
            for y in range(self.y,self.y_end):
                self.y_coordinates.append(y)
        else:
            self.x_end = self.x + self.size
            for x in range(self.x,self.x_end):
                self.x_coordinates.append(x)
    
    def clear_coordinates(self):
        if self.is_vertical == True:
            self.y_coordinates.clear()
        else:
            self.x_coordinates.clear()

    def toggle_vertical(self):
        self.is_vertical = not self.is_vertical
        self.generate_ship_coordinates()


