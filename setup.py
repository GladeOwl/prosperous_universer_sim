import json
import string
from outpost import Outpost
from item import Item
from inventory import Inventory
from production import Producer
from logger import create_log, write_to_log, add_partition, write_text_to_log


def setup_item(
    producer: dict,
    new_producer: Producer,
    log: string,
    items: list,
    inventory: Inventory,
    base: Outpost,
):
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

        if "Consumables" in new_item.category:
            base.consumables.append(new_item)

        items.append(new_item)
        new_producer.queue += item["orders"] * [new_item]
        inventory.add_stock(new_item, item["starting_stock"], (0, 0, 0))

        log += f"| {new_item.name} [{new_item.ticker}]|"

    return log


def setup_simulation(inventory: Inventory):
    create_log()
    add_partition()

    items = []
    producers = []

    with open("./data.json", encoding="utf-8") as jsonf:
        data = json.load(jsonf)
        base = Outpost("Harmonia", inventory, [], data["workforce"])

        for producer in data["producers"]:
            new_producer = Producer(
                name=producer["name"],
                queue=[],
                queue_slots=producer["queue_slots"],
                inventory=inventory,
                workforce=producer["workforce"],
            )

            log = f"{new_producer.name}: "
            log = setup_item(producer, new_producer, log, items, inventory, base)
            write_text_to_log(log)

            producers.append(new_producer)
            base.add_base_pop(new_producer.workforce, producer["queue_slots"])

    base.get_total_pop()

    for item in items:
        item.setup_reciepe(items)

    write_text_to_log("Simluation Setup Completed.")
    add_partition()
    write_text_to_log(f"Simulation Start")

    inventory.log_inventory()

    for producer in producers:
        producer.initial_production((0, 0, 0))

    return base, items, producers
