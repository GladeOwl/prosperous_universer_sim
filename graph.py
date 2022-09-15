from cProfile import label
import string
import numpy as np
from inventory import Inventory
from matplotlib import pyplot as plot


def plot_inventory_stock(inventory: Inventory, days: int):
    stock_history = inventory.stock_history
    days_in_graph = []
    days_in_graph.extend(range(0, days))

    for item in stock_history:
        plot.plot(days_in_graph, stock_history[item], label=item)
        plot.title(item)

    plot.legend()
    plot.show()
