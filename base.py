import string
from inventory import Inventory
from logger import create_log, write_to_log, add_partition, write_text_to_log


class Base:
    def __init__(
        self, name: string, inventory: Inventory, consumables: list, needs: dict
    ) -> None:
        self.name: string = name
        self.inventory = inventory
        self.consumables = consumables
        self.needs = needs

        self.pioneers: int = 0
        self.settlers: int = 0
        self.technicians: int = 0
        self.engineers: int = 0
        self.scientists: int = 0

    def add_base_pop(self, pop: dict, amount: int):
        self.pioneers += pop["pioneers"] * amount
        self.settlers += pop["settlers"] * amount
        self.technicians += pop["technicians"] * amount
        self.engineers += pop["engineers"] * amount
        self.scientists += pop["scientists"] * amount

    def get_total_pop(self):
        write_text_to_log(
            f"pioneers: {self.pioneers},\nsettlers: {self.settlers},\ntechnicians: {self.technicians},\nengineers: {self.engineers},\nscientists: {self.scientists}"
        )

    def daily_burn(self, time: tuple):
        for need in self.needs["pioneers"]:
            for item in self.consumables:
                if need == item.ticker:
                    self.inventory.remove_stock(
                        item, self.needs["pioneers"][need], time
                    )
