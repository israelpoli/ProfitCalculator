import json
from pathlib import Path


coins_data_folder = Path("")


def get_percentage_difference(a: int | float, b: int | float):
    return (a / b) * 100


def calculate(first_date: str, symbol: str, monthly_deposit: bool, how: str):
    coins_data_symbol_path = coins_data_folder / f"{symbol}.json"
    coins_data = json.loads(coins_data_symbol_path.read_text())

    first_price = coins_data[first_date]["price"]
    if not isinstance(first_price, int | float):
        raise

    coins = monthly_deposit / first_price
        
    
    