import string
from logger import create_log, write_to_log, add_partition
from item import Item
from inventory import Inventory


class Producer:
    def __init__(
        self, name: string, queue: list, queue_slots: int, inventory: Inventory
    ) -> None:
        self.name: string = name
        self.queue: list = queue
        self.queue_slots = queue_slots
        self.inventory: Inventory = inventory
        self.current_production = []

    def setup_production(self):
        for index in range(self.queue_slots - len(self.current_production)):
            production = self.queue.pop(0)
            self.current_production.append(production)
            self.queue.append(production)

    def tick(self, time: tuple):
        """Ticks the production by 1"""
        self.current_time -= 1
        if self.current_time <= 0:
            self.complete_production(time)

    def complete_production(self, time: tuple):
        """Completes the production of an item"""
        write_to_log(
            f"[{time[0]}D:{time[1]}H:{time[2]}M] [{self.name}] Produced: {self.current_production.name}, {self.current_production.produced_per_cycle} units"
        )
        self.deposit_resources(time)

        if self.current_production_index + 1 >= len(self.queue):
            self.current_production_index = 0
        else:
            self.current_production_index += 1

        self.current_production = self.queue[self.current_production_index]

        self.current_time = self.current_production.time
        self.withdraw_resources(time)

    def withdraw_resources(self, time: tuple):
        """Witdraws the required resources from the inventory"""
        for item in self.current_production.reciepe:
            write_to_log(
                f"[{time[0]}D:{time[1]}H:{time[2]}M] [{self.name}] Withdraw Request: {item['item'].name}, {item['amount']} units --> {self.current_production.name}"
            )
            self.inventory.remove_stock(item["item"], item["amount"], time)

    def deposit_resources(self, time: tuple):
        """Desposits the resources to the inventory"""
        self.inventory.add_stock(
            self.current_production, self.current_production.produced_per_cycle, time
        )


class Production:
    def __init__(self, item: Item, time: int, inventory: Inventory) -> None:
        self.item: Item = item
        self.time: int = time
        self.time_left = time
        self.inventory: Inventory = inventory

    def tick(self):
        self.time_left -= 1
        if self.time_left <= 0:
            pass

    def finish_production(self):
        pass

    def withdraw_resources(self):
        for item in self.item.reciepe:
            self.inventory.remove_stock(item["item"], item["amount"])

    def deposit_resources(self):
        self.inventory.add_stock(self.item, self.item.produced_per_cycle)
