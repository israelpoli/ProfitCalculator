

class Seria:
    def __init__(self, chart: list[dict]) -> None:
        self.chart = chart

    def get_date(self, date: str) -> dict:
        return self.chart[date]
    
    