from processor import OrderProcessor
from utils import load_orders


def main():
    orders = load_orders("data.json")
    processor = OrderProcessor(orders)

    results = processor.process()
    summary = processor.summary(results)

    processor.print_report(results)
    processor.print_summary(summary)


if __name__ == "__main__":
    main()
