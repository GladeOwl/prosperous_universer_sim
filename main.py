import json
from math import prod
from logger import create_log, write_to_log, add_partition
from inventory import Inventory
from production import Producer
from item import Item


def simulate_time(producers: list):
    max_runtime: int = 100 * 60
    hours: int = 0
    runtime: int = 0  # in minutes
    hour_minutes: int = 0

    while runtime < max_runtime:
        runtime += 1
        hour_minutes += 1

        for producer in producers:
            producer.tick((hours, hour_minutes))

        if hour_minutes == 60:
            hour_minutes = 0
            hours += 1

        if hours % 24 == 0:
            # add_partition()
            pass

        # write_to_log(str(runtime))

    print(f"Done in {hours}H:{hour_minutes}M ({runtime} minutes).")


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

            inventory.add_stock(item, 10, (0, 0))

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
    inventory.log_inventory()

    for producer in producers:
        producer.withdraw_resources((0, 0))

    simulate_time(producers)
    inventory.log_inventory()
