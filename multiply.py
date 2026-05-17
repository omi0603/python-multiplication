def multiply(num1, num2):
    """Return the product of two numbers."""
    return num1 * num2


if __name__ == "__main__":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    result = multiply(first_number, second_number)
    print(f"Product: {result}")
