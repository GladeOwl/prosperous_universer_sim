from item import Item
from logger import create_log, write_to_log, add_partition


class Inventory:
    def __init__(self, max_weight: float, max_volume: float) -> None:
        self.max_weight: float = max_weight
        self.max_volume: float = max_volume
        self.current_weight: float = 0
        self.current_volume: float = 0
        self.stock: dict = {}

    def add_stock(self, item: Item, amount: int, time: tuple):
        """Adds the requested stock to the inventory stock"""

        if item.name not in self.stock:
            self.stock[item.name] = {"info": item, "amount": 0}

        self.stock[item.name]["amount"] += amount
        self.current_weight += item.weight * amount
        self.current_volume += item.volume * amount

        write_to_log(f"[{time[0]}H:{time[1]}M] Added {item.name}: {amount} units")

    def remove_stock(self, item: Item, amount: int, time: tuple):
        """Removes the requested item from the inventory stock"""

        if item.name not in self.stock:
            write_to_log(
                f"[{time[0]}H:{time[1]}M] {item.name} doesn't exist in the inventory."
            )
            return

        self.stock[item.name]["amount"] -= amount

        if self.stock[item.name]["amount"] < 0:
            write_to_log(f"[{time[0]}H:{time[1]}M] {item.name} has run out.")
            return

        self.current_weight -= item.weight * amount
        self.current_volume -= item.volume * amount

        write_to_log(f"[{time[0]}H:{time[1]}M] Removed {item.name}: {amount} units")

    def log_inventory(self):
        add_partition()
        write_to_log("|| Inventory Stock ||")
        for item in self.stock:
            amount = self.stock[item]["amount"]
            write_to_log(f"|| {item} : {amount} ||")
        add_partition()
