from inventory import Inventory
from production import Production
from item import Item

def simulate_time(production: Production):
    max_runtime: int = 24 * 60
    hours: int = 0
    runtime: int = 0 # in minutes
    hour_minutes: int = 0

    while (runtime < max_runtime):
        runtime += 1
        hour_minutes += 1

        production.tick()

        if (hour_minutes == 60):
            hour_minutes = 0
            hours += 1
    
    print(f"Done in {hours}H:{hour_minutes}M ({runtime} minutes).")

def setup_simulation(inventory: Inventory):
    water = Item(name = "water", ticker = "H2O", weight = 0.2, volume = 0.2, producer = "rig", category = "liquids")
    water_production = Production(water, 423, True, inventory)
    return water_production

if __name__ == "__main__":
    max_weight = 1500
    max_volume = 1500
    inventory = Inventory(max_weight, max_volume)

    production = setup_simulation(inventory)

    simulate_time(production)