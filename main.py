import json
import math
import string
from operator import inv
from base import Base
from item import Item
from graph import plot_inventory_stock
from inventory import Inventory
from production import Producer
from setup import setup_simulation
from logger import create_log, write_to_log, add_partition, write_text_to_log


def simulate_time(base: Base, producers: list):
    runtime_in_days = 365
    max_runtime: int = runtime_in_days * 1440
    runtime: int = 0  # in minutes

    days = 0
    hours = 0
    minutes = 0

    current_day = 0

    while runtime < max_runtime:
        runtime += 1

        days = math.floor(runtime / 24 / 60)
        hours = math.floor(runtime / 60 % 24)
        minutes = math.floor(runtime % 60)
        time = (days, hours, minutes)

        for producer in producers:
            producer.tick(time)

        if current_day != days:
            base.daily_burn(time)
            inventory.log_daily_stock()

            current_day = days
            add_partition()
            inventory.log_inventory()
            write_text_to_log(f"Day {current_day}")
            add_partition()

    print(f"Done in {days}D:{hours}H:{minutes}M ({runtime} minutes).")

    add_partition()
    write_text_to_log("End of Simulation")
    inventory.log_inventory()

    # plot_inventory_stock(inventory, runtime_in_days)


if __name__ == "__main__":
    max_weight = 1500
    max_volume = 1500
    inventory = Inventory(max_weight, max_volume)

    base, items, producers = setup_simulation(inventory)

    simulate_time(base, producers)
    # print(inventory.stock_history)
