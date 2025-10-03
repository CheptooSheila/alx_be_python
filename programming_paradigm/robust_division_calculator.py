def safe_divide(numerator, denominator):
    """Perform safe division with error handling."""
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."

        # Perform division
        result = num / denom
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."
    except Exception as e:
        # Catch any unexpected errors
        return f"An unexpected error occurred: {e}"

