from item import Item
from inventory import Inventory

class Production():
    def __init__(self, item: Item, total_time: int, recurring: bool, inventory: Inventory, items_required: list = None) -> None:
        self.item = item
        self.total_time = total_time
        self.current_time = total_time
        self.items_required = items_required
        self.inventory = inventory

    def gather_resources(self):
        """Gather required resources from the inventory"""

        if len(self.items_required) > 0:
            for item in self.items_required:
                self.inventory.remove_stock(item[0], item[1])

    def tick(self):
        """Tick the production by 1"""

        self.current_time -= 1
        
        if self.current_time >= 0:
            self.complete_production()
    
    def complete_production(self):
        """Checks if the production cycle is complete"""

        self.current_time = self.total_time
        print("Production is complete")