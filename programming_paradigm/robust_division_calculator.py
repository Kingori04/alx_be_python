def safe_divide(numerator, denominator):
    """
    Safely performs division while handling errors like division by zero
    and non-numeric inputs.

    Parameters:
    - numerator: The numerator of the division.
    - denominator: The denominator of the division.

    Returns:
    - The result of the division if valid.
    - An error message if invalid input or division by zero occurs.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            return "Error: Cannot divide by zero."
        return f"The result of the division is {num / den:.1f}"
    except ValueError:
        return "Error: Please enter numeric values only."
