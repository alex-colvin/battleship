class Item:
    def __init__(self, name, size, identifyer) -> None:
        self.size = size
        self.name = name
        self.x = 4
        self.y = 4
        self.identifyer = f"[{identifyer}]"
        self.position = None
        self.is_vertical = True
        self.is_set = False