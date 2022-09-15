import math
from daily import Daily
from item import Item
from logger import create_log, write_to_log, add_partition, write_text_to_log


class Inventory:
    def __init__(self, max_weight: float, max_volume: float) -> None:
        self.max_weight: float = max_weight
        self.max_volume: float = max_volume
        self.current_weight: float = 0
        self.current_volume: float = 0
        self.stock: dict = {}
        self.stock_history: dict = {}

    def add_stock(self, item: Item, amount: int, time: tuple):
        """Adds the requested stock to the inventory stock"""

        if item.name not in self.stock:
            self.stock[item.name] = {"info": item, "amount": 0}

        self.stock[item.name]["amount"] += int(amount)
        self.current_weight += item.weight * amount
        self.current_volume += item.volume * amount

        # if self.current_weight > self.max_weight:
        #     write_to_log(
        #         time,
        #         "INV",
        #         f"Max Weight Limit Exceeded. {self.current_weight}/{self.max_weight}",
        #     )
        #     self.log_inventory()
        #     raise AttributeError("Max Weight Limit Exceeded.")

        # if self.current_volume > self.max_volume:
        #     write_to_log(
        #         time,
        #         "INV",
        #         f"Max Volume Limit Exceeded. {self.current_volume}/{self.max_volume}",
        #     )
        #     self.log_inventory()
        #     raise AttributeError("Max Volume Limit Exceeded.")

        # write_to_log(
        #     f"[{time[0]}D:{time[1]}H:{time[2]}M] [INV] Added: {item.name}, {amount} units"
        # )

    def remove_stock(self, item: Item, amount: int, time: tuple):
        """Removes the requested item from the inventory stock"""

        if item.name not in self.stock:
            write_to_log(
                time,
                "INV",
                f"{item.name} doesn't exist in the inventory.",
            )
            self.log_inventory()
            raise Exception("Error! Check Logs")

        self.stock[item.name]["amount"] -= amount

        if self.stock[item.name]["amount"] < 0:
            write_to_log(
                time,
                "INV",
                f"{item.name} has run out.",
            )
            self.log_inventory()
            raise AttributeError(f"{item.name} has run out.")

        self.current_weight -= item.weight * amount
        self.current_volume -= item.volume * amount

        write_to_log(
            time,
            "INV",
            f"Removed: {item.name} [{item.ticker}], {amount} units",
        )

    def log_inventory(self):
        add_partition()
        write_text_to_log(f"|| Inventory Stock ||")
        for item in self.stock:
            write_text_to_log(
                f"|| {item} [{self.stock[item]['info'].ticker}]: {round(self.stock[item]['amount'], 2)} ||"
            )
        write_text_to_log(
            f"|| Weight: {round(self.current_weight, 2)}/{self.max_weight} | Volume: {round(self.current_volume, 2)}/{self.max_volume} ||"
        )
        add_partition()

    def log_daily_stock(self):
        for item in self.stock:
            if item not in self.stock_history:
                self.stock_history[item] = []
            self.stock_history[item].append(round(self.stock[item]["amount"], 2))
