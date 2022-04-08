class Item:
    def __init__(self, name, size, identifyer) -> None:
        self.size = size
        self.name = name
        self.x = 1
        self.y = 1
        self.identifyer = f"[{identifyer}]"
        self.position = None