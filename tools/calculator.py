def calculate(expression: str) -> str:
    """
    Safely evaluate a simple mathematical expression.
    Example: calculate("15 / 100 * 280")
    """
    allowed_chars = set("0123456789+-*/(). %")

    if not set(expression).issubset(allowed_chars):
        return "Error: expression contains unsupported characters."

    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"