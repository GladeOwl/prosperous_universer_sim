import string


class Daily:
    def __init__(self, day: int, data: dict) -> None:
        self.day: int = day
        self.data: dict = {}

    def add_data(self, name: string, amount: int):
        """Add data to the day's stock"""
        pass
