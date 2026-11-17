from processor import OrderProcessor
from utils import load_orders


def main():
    orders = load_orders("data.json")
    processor = OrderProcessor(orders)

    summary = processor.summary(results)
    results = processor.process()

    processor.print_report(results)
    processor.print_summary(summary)


if __name__ == "__main__":
    main()
