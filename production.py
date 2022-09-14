import string
from item import Item
from producer import Producer
from inventory import Inventory
from logger import create_log, write_text_to_log, write_to_log, add_partition


class Production:
    def __init__(self, item: Item, producer: Producer, inventory: Inventory) -> None:
        self.item: Item = item
        self.time: int = item.time
        self.time_left: int = item.time
        self.inventory: Inventory = inventory
        self.producer = producer

    def tick(self, time: tuple):
        self.time_left -= 1
        if self.time_left <= 0:
            self.finish_production(time)

    def finish_production(self, time: tuple):
        write_to_log(
            time,
            self.item.producer,
            f"Produced: {self.item.name}, {self.item.produced_per_cycle} units",
        )
        self.time_left = self.time
        self.deposit_resources(time)
        self.producer.next_production(self)

    def withdraw_resources(self, time: tuple):
        for item in self.item.reciepe:
            write_to_log(
                time,
                self.item.producer,
                f"Withdraw Request: {item['item'].name}, {item['amount']} units --> {self.current_production.name}",
            )
            self.inventory.remove_stock(item["item"], item["amount"])

    def deposit_resources(self, time: tuple):
        self.inventory.add_stock(self.item, self.item.produced_per_cycle, time)
