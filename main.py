import json
import math
from re import A
from logger import create_log, write_to_log, add_partition
from inventory import Inventory
from production import Producer
from item import Item


def simulate_time(producers: list):
    runtime_in_days = 10
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

        for producer in producers:
            producer.tick((days, hours, minutes))

        if current_day != days:
            current_day = days
            add_partition()
            write_to_log(f"Day {current_day}")
            inventory.log_inventory()

    print(f"Done in {days}D:{hours}H:{minutes}M ({runtime} minutes).")


def setup_simulation(inventory: Inventory):
    create_log()
    add_partition()

    items = []
    producers = []
    with open("./data.json", encoding="utf-8") as jsonf:
        data = json.load(jsonf)
        for item in data["items"]:
            item = Item(
                name=item["name"],
                ticker=item["ticker"],
                weight=item["weight"],
                volume=item["volume"],
                producer=item["producer"],
                category=item["category"],
                reciepe_raw=item["reciepe"],
                time=item["time"],
                produced_per_cycle=item["produced_per_cycle"],
            )
            items.append(item)

            inventory.add_stock(item, 20, (0, 0, 0))

            producer_present = False
            for producer in producers:
                if producer.name == item.producer:
                    producer_present = True
                    producer.queue.append(item)
                    break

            if not producer_present:
                producer = Producer(item.producer, [item], inventory)
                producers.append(producer)

    for item in items:
        item.setup_reciepe(items)

    write_to_log("Simluation Setup Completed.")
    add_partition()

    return items, producers


if __name__ == "__main__":
    max_weight = 1500
    max_volume = 1500
    inventory = Inventory(max_weight, max_volume)

    items, producers = setup_simulation(inventory)

    write_to_log(f"Simulation Start")
    inventory.log_inventory()

    for producer in producers:
        producer.withdraw_resources((0, 0, 0))

    simulate_time(producers)
    inventory.log_inventory()
