# Python Sales Processor — Debugging Challenge

## Objective
This project loads sales order data, applies discount rules, classifies orders by value, and prints a report.

The project has been intentionally damaged. Your task is to debug it without rewriting the application from scratch.

## Setup
Install the project dependencies, then run:

```bash
pip install -r requirements.txt
python main.py
```

## Functional requirements
1. Load order records from `data.json`.
2. Parse every order's `order_date` value into a real date/datetime value. The input intentionally uses more than one date format.
3. Calculate each order's final amount by applying the discount percentage: `amount × (1 − discount / 100)`.
4. Ignore non-numeric discount values such as `null` or `"N/A"` — treat them as zero discount.
5. Classify orders by their final amount (boundaries are inclusive):
   - 1000 or above: `Large`
   - 500 to below 1000: `Medium`
   - 100 to below 500: `Small`
   - Below 100: `Micro`
6. Calculate the total revenue from all orders.
7. If no order has a valid final amount, the application must not divide by zero.
8. Display the customer with the most recent order.
9. Print the order table using the dependency listed for table formatting.
10. Keep the existing project structure and fix the existing implementation rather than replacing it wholesale.

## Time limit
10–15 minutes.

When you are finished, briefly explain:
- the problems you found,
- how you fixed them,
- and how you verified the final output.

## Expected Output

Once all bugs are fixed, the program should produce the following output:

```
Sales Order Report
| Customer    | Region   | Final Amount   | Classification   |
|-------------|----------|----------------|------------------|
| Acme Corp   | North    | 1000.00        | Large            |
| Beta LLC    | South    | 850.00         | Medium           |
| Gamma Inc   | East     | 255.00         | Small            |
| Delta Co    | West     | 75.50          | Micro            |
| Epsilon Ltd | North    | 2000.00        | Large            |
| Zeta Group  | South    | 500.00         | Medium           |
| Eta Systems | East     | 142.50         | Small            |

Total orders: 7

Sales Summary
------------------------------
Total revenue: $4,823.00
Most recent order: Epsilon Ltd
```
