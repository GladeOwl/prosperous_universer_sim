import string
import numpy as np
from inventory import Inventory
from matplotlib import pyplot as plot


def plot_inventory_stock(inventory: Inventory, days: int):
    stock_history = inventory.stock_history
    days_in_graph = []
    days_in_graph.extend(range(0, days))

    index = 1
    for item in stock_history:
        plot.subplot(2, 3, index)
        plot.plot(days_in_graph, stock_history[item])
        plot.title(item)
        index += 1

    plot.show()
