class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers (no class/instance context needed)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Access the class attribute and return the product of two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b