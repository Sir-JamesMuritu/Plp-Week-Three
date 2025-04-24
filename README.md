# Week Three Assignment - Discount Calculator

This repository contains a Python program that calculates the final price of an item after applying a discount, based on user input and a conditional check.

## Objective

Demonstrate the use of conditional statements and functions in Python by creating a simple discount calculator.

## Task Requirements

- Define a function named `calculate_discount(price, discount_percent)`:
  - If the `discount_percent` is **20% or higher**, apply the discount and return the final price.
  - If the discount is **less than 20%**, return the original price.
- Prompt the user for:
  - The original price of an item
  - The discount percentage
- Use the function to compute and display the correct price based on the rules.

## Features

- Interactive input from the user
- Error handling for invalid numeric input
- Clear and formatted output

## Requirements

- Python 3.6 or higher

## How to Run

1. Clone the repository or download the `calculate_discount.py` file.
2. Open a terminal in the project directory.
3. Run the script using:

```bash
python calculate_discount.py
```

## Example Output

```
Welcome to the Discount Calculator!
Enter the original price: 100
Enter the discount percentage: 25
Discount applied! Final price: $75.00
```

```
Welcome to the Discount Calculator!
Enter the original price: 80
Enter the discount percentage: 10
No discount applied. Final price: $80.00
```

## License

This project is licensed under the MIT License.

