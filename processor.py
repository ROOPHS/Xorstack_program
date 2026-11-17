from tabulate import tabulate


class OrderProcessor:
    def __init__(self, orders):
        self.orders = orders

    def apply_discount(self, amount, discount):
        if discount is None or not isinstance(discount, (int, float)):
            return amount

        return amount - (amount * discount / 100)

    def classify_order(self, amount):
        if amount >= 1000:
            return "Large"
        elif amount >= 500:
            return "Medium"
        elif amount >= 100:
            return "Small"
        else:
            return "Micro"

    def process(self):
        results = []

        for order in self.orders:
            discount = order.get("discount")
            amount = order.get("amount", 0)
            final_amount = self.apply_discount(amount, discount)

            classification = self.classify_order(final_amount)

            results.append(
                {
                    "customer": order["customer"],
                    "region": order["region"],
                    "final_amount": final_amount,
                    "classification": classification,
                    "order_date": order["order_date"],
                }
            )

        return results

    def summary(self, results):
        valid = [item for item in results if item["final_amount"] is not None]
        if not valid:
            return {"total_revenue": None, "latest_customer": None}

        total_revenue = sum(item["final_amount"] for item in valid)

        latest = max(valid, key=lambda item: item["order_date"])

        return {"total_revenue": total_revenue, "latest_customer": latest["customer"]}

    def print_report(self, results):
        rows = []

        for order in results:
            if order["final_amount"] is None:
                amount = "N/A"
            else:
                amount = f"{order['final_amount']:.2f}"

            rows.append(
                [order["customer"], order["region"], amount, order["classification"]]
            )

        print("\nSales Order Report")
        print(
            tabulate(
                rows,
                headers=["Customer", "Region", "Final Amount", "Classification"],
                tablefmt="github",
            )
        )
        print(f"\nTotal orders: {len(results)}")

    def print_summary(self, summary):
        print("\nSales Summary")
        print("-" * 30)

        if summary["total_revenue"] is None:
            print("Total revenue: N/A")
        else:
            print(f"Total revenue: ${summary['total_revenue']:.2f}")
            if summary["latest_customer"] is None:
                print("Most recent order:N/A")
            else:
                print(f"Most recent order: {summary['latest_customer']}")
