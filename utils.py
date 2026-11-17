import json
from dateutil.parser import parse


def load_orders(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    for order in data:
        order["order_date"] = parse(order["order_date"])

    return data
