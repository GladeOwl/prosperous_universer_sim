import string
from production import Production
from inventory import Inventory
from logger import create_log, write_text_to_log, write_to_log, add_partition


class Producer:
    def __init__(
        self, name: string, queue: list, queue_slots: int, inventory: Inventory
    ) -> None:
        self.name: string = name
        self.queue: list = queue
        self.queue_slots = queue_slots
        self.inventory: Inventory = inventory
        self.current_production = []

    def tick(self, time: tuple):
        """Ticks the production by 1"""
        for production in self.current_production:
            production.tick(time)

    def initial_production(self):
        """Sets up the initial production queue for the Producer"""
        index = 0
        while index < self.queue_slots - len(self.current_production):
            self.setup_production()

    def next_production(self, production: Production):
        """Sets up the next production in the queue"""
        self.current_production.remove(production)
        self.setup_production()

    def setup_production(self):
        item = self.queue.pop(0)
        production = Production(item, self.inventory)
        self.current_production.append(production)
        self.queue.append(item)
        write_text_to_log(f"Setting up production for {item.name}")
