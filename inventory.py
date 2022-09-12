from item import Item

class Inventory():
    def __init__(self, max_weight: float, max_volume: float) -> None:
        self.max_weight: float = max_weight
        self.max_volume: float = max_volume
        self.current_weight: float = 0
        self.current_volume: float = 0
        self.stock: dict = {}

    def add_stock(self, item: Item, amount: int):
        """Adds the requested stock to the inventory stock"""
        
        if item.name not in self.stock:
            self.stock[item.name]["info"] = item
            self.stock[item.name]["amount"] = 0
        
        self.stock[item.name]["amount"] += amount
        self.current_weight += item.weight * amount
        self.current_volume += item.volume * amount
    
    def remove_stock(self, item: Item, amount: int):
        """Removes the requested item from the inventory stock"""
        
        if item.name not in self.stock:
            print(f"{item.name} doesn't exist in the inventory.")
            return
        
        self.stock[item.name]["amount"] -= amount

        if self.stock[item.name] < 0:
            print(f"{item.name} has run out.")
            return
        
        self.current_weight -= item.weight * amount
        self.current_volume -= item.volume * amount