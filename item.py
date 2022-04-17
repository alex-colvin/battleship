class Item:
    def __init__(self, name, size, identifyer, x_start=10) -> None:
        self.size = size
        self.name = name
        self.x = x_start
        self.y = 0
        self.identifyer = f"[{identifyer}]"
        self.position = None
        self.is_vertical = True
        self.is_set = False