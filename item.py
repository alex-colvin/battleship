class Item:
    def __init__(self, name, size, identifyer) -> None:
        self.size = size
        self.name = name
        self.x = 0
        self.y = 0
        self.identifyer = f"[{identifyer}]"
        self.position = None
        self.is_vertical = True
        self.is_set = False