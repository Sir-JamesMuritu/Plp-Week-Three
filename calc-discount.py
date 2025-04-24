# week_three_assignment: Discount Calculator

def calculate_discount(price, discount_percent):
    """
    Calculates and returns the final price after applying a discount
    if the discount is 20% or higher. Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

def main():
    print("Welcome to the Discount Calculator!")

    try:
        # Get user input
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate final price
        final_price = calculate_discount(price, discount_percent)

        # Output result
        if discount_percent >= 20:
            print(f"Discount applied! Final price: Ksh {final_price:.2f}")
        else:
            print(f"No discount applied. Final price: Ksh {final_price:.2f}")

    except ValueError:
        print("⚠️  Please enter valid numbers for price and discount.")

if __name__ == "__main__":
    main()
