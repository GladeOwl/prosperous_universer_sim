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
        reciepe: list,
    ) -> None:
        self.name: string = name
        self.ticker: string = ticker
        self.category: string = category
        self.weight: float = weight
        self.volume: float = volume
        self.producer: string = producer
        self.reciepe: list = reciepe
