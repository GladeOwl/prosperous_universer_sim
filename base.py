from logger import create_log, write_to_log, add_partition, write_text_to_log


class Base:
    def __init__(
        self,
        name,
    ) -> None:
        self.name = name

    def get_base_pop(self, producers: list):
        pass

    def daily_burn(self):
        pass
