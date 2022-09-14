import string
from inventory import Inventory
from logger import create_log, write_to_log, add_partition, write_text_to_log


class Base:
    def __init__(self, name: string, inventory: Inventory) -> None:
        self.name: string = name
        self.inventory = inventory

        self.pioneers: int = 0
        self.settlers: int = 0
        self.technicians: int = 0
        self.engineers: int = 0
        self.scientists: int = 0

    def add_base_pop(self, pop: dict):
        self.pioneers += pop["pioneers"]
        self.settlers += pop["settlers"]
        self.technicians += pop["technicians"]
        self.engineers += pop["engineers"]
        self.scientists += pop["scientists"]

    def get_total_pop(self):
        return {
            "pioneers": self.pioneers,
            "settlers": self.settlers,
            "technicians": self.technicians,
            "engineers": self.engineers,
            "scientists": self.scientists,
        }

    def daily_burn(self):
        pass
