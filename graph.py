from cProfile import label
import numpy as np
from inventory import Inventory
from matplotlib import pyplot as plot
from matplotlib import animation
from matplotlib import style
from matplotlib import axes


class Graph:
    def __init__(self, inventory: Inventory, days: int) -> None:
        self.inventory = inventory
        self.days = days
        self.items = {}

        plot.ion()

        for item in self.inventory.stock_history:
            self.items[item] = plot.plot(
                self.days, self.inventory.stock_history[item], label=item
            )
            self.items[item][0].axes.set_xlim(0, days)
            self.items[item][0].axes.set_ylim(-100, 100)

        plot.title("Inventory Stock")
        plot.legend()
        plot.grid()
        plot.draw()

    def update_graph(self):
        for item in self.inventory.stock_history:
            self.items[item][0].set_ydata(self.inventory.stock_history[item])
            plot.draw()


def plot_inventory_stock(inventory: Inventory, days: int):
    stock_history = inventory.stock_history
    days_in_graph = []
    days_in_graph.extend(range(0, days))

    for item in stock_history:
        plot.plot(days_in_graph, stock_history[item], label=item)

    plot.title("Inventory Stock")
    plot.legend()
    plot.show()
