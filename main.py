import json
import math
from logger import create_log, write_to_log, add_partition, write_text_to_log
from inventory import Inventory
from production import Producer
from item import Item


def simulate_time(producers: list):
    runtime_in_days = 60
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
            current_day = days
            add_partition()
            inventory.log_inventory()
            write_text_to_log(f"Day {current_day}")
            add_partition()

    print(f"Done in {days}D:{hours}H:{minutes}M ({runtime} minutes).")

    add_partition()
    write_text_to_log("End of Simulation")
    inventory.log_inventory()


def setup_simulation(inventory: Inventory):
    create_log()
    add_partition()

    items = []
    producers = []
    with open("./data.json", encoding="utf-8") as jsonf:
        data = json.load(jsonf)
        for producer in data["producers"]:
            new_producer = Producer(
                name=producer["name"],
                queue=[],
                queue_slots=producer["queue_slots"],
                inventory=inventory,
            )

            producer_log = f"{new_producer.name}: "

            for item in producer["items"]:
                new_item = Item(
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

                items.append(new_item)
                new_producer.queue.append(new_item)
                inventory.add_stock(new_item, item["starting_stock"], (0, 0, 0))
                producer_log += f"| {new_item.name} [{new_item.ticker}]|"

            write_text_to_log(producer_log)
            producers.append(new_producer)

    for item in items:
        item.setup_reciepe(items)

    write_text_to_log("Simluation Setup Completed.")
    add_partition()
    write_text_to_log(f"Simulation Start")
    inventory.log_inventory()

    for producer in producers:
        producer.initial_production((0, 0, 0))

    return items, producers


if __name__ == "__main__":
    max_weight = 1500
    max_volume = 1500
    inventory = Inventory(max_weight, max_volume)

    items, producers = setup_simulation(inventory)

    simulate_time(producers)
