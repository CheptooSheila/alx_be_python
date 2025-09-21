# control-flow/multiplication_table.py
# Multiplication Table Generator

# Ask user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table using a for loop
for i in range(1, 11):  # from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")

