import string
from item import Item
from inventory import Inventory


class Producer:
    def __init__(self, name: string, queue: list, inventory: Inventory) -> None:
        self.name: string = name
        self.queue: list = queue
        self.inventory: Inventory = inventory

    def tick(self):
        self.current_time -= 1

    def setup_production(self):
        self.current_production = self.queue[0]
        self.current_time = self.current_production.time

    def withdraw_resources(self):
        for item in self.current_production.reciepe:
            self.inventory.remove_stock()


class Production:
    def __init__(
        self,
        item: Item,
        inventory: Inventory,
    ) -> None:
        self.item = item
        self.current_time = item.time
        self.items_required = item.reciepe
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
