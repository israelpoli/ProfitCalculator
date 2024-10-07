

from Seria import Seria


class Monthly(Seria):
    def __init__(self, chart: list[dict]) -> None:
        self.chart = chart
        