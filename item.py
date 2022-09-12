import string


class Item:
    def __init__(
        self,
        name: string,
        ticker: string,
        category: string,
        weight: float,
        volume: float,
        producer: string,
        reciepe_raw: dict,
        time: int,
        produced_per_cycle: int,
    ) -> None:
        self.name: string = name
        self.ticker: string = ticker
        self.category: string = category
        self.weight: float = weight
        self.volume: float = volume
        self.producer: string = producer
        self.reciepe_raw: dict = reciepe_raw
        self.time: int = time
        self.produced_per_cycle: int = produced_per_cycle
        self.reciepe = []

    def setup_reciepe(self, items: list):
        """Creates Item Objects from raw json data and adds it to the reciepe list"""
        for item in items:
            if item.ticker in self.reciepe_raw.keys():
                self.reciepe.append(
                    {"item": item, "amount": self.reciepe_raw[item.ticker]}
                )
