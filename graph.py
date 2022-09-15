from cProfile import label
import string
import math
import numpy as np
from inventory import Inventory
from matplotlib import pyplot as plot


def plot_inventory_stock(inventory: Inventory, days: int):
    stock_history = inventory.stock_history
    days_in_graph = []
    days_in_graph.extend(range(0, days))

    index = 1
    number_of_items = len(stock_history)

    column = int(math.sqrt(number_of_items))
    rows = int(math.ceil(number_of_items / column))

    for item in stock_history:
        plot.subplot(
            rows,
            column,
            index,
        )
        plot.plot(days_in_graph, stock_history[item], label=item)
        plot.title(item)
        index += 1

    # plot.legend()
    plot.show()
