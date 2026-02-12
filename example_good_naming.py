"""
Example of good variable and function naming practices.
This code is functionally identical to example_poor_naming.py but much clearer.
"""

def calculate_discounted_price(unit_price, quantity, months):
    """
    Calculate the final price after applying a 15% discount.
    
    Args:
        unit_price: Price per unit
        quantity: Number of units
        months: Number of months for the subscription
    
    Returns:
        Final price after discount
    """
    subtotal = unit_price * quantity
    total_before_discount = subtotal * months
    discount_amount = total_before_discount * 0.15
    return total_before_discount - discount_amount

def filter_and_double_positive_numbers(numbers):
    """
    Filter positive numbers and double their values.
    
    Args:
        numbers: List of integers to process
    
    Returns:
        List of doubled positive numbers
    """
    doubled_positives = []
    for number in numbers:
        if number > 0:
            doubled_value = number * 2
            doubled_positives.append(doubled_value)
    return doubled_positives

def calculate_fibonacci_number(position):
    """
    Calculate the Fibonacci number at the given position.
    
    Args:
        position: The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        The Fibonacci number at the specified position
    """
    if position <= 1:
        return position
    return calculate_fibonacci_number(position - 1) + calculate_fibonacci_number(position - 2)

class Point2D:
    """Represents a point in 2D space with x and y coordinates."""
    
    def __init__(self, x_coordinate, y_coordinate):
        """
        Initialize a 2D point.
        
        Args:
            x_coordinate: The x-axis coordinate
            y_coordinate: The y-axis coordinate
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def calculate_sum_of_coordinates(self):
        """
        Calculate the sum of x and y coordinates.
        
        Returns:
            Sum of coordinates
        """
        return self.x_coordinate + self.y_coordinate
    
    def are_both_coordinates_positive(self):
        """
        Check if both coordinates are positive.
        
        Returns:
            True if both coordinates are positive, False otherwise
        """
        return self.x_coordinate > 0 and self.y_coordinate > 0

# Usage example with descriptive variable names
if __name__ == "__main__":
    # Variables with clear, descriptive names
    price_per_unit = 100
    quantity_ordered = 5
    subscription_months = 12
    
    discounted_price = calculate_discounted_price(price_per_unit, quantity_ordered, subscription_months)
    print(f"Discounted price: {discounted_price}")
    
    number_list = [1, -2, 3, -4, 5]
    doubled_positive_numbers = filter_and_double_positive_numbers(number_list)
    print(f"Doubled positive numbers: {doubled_positive_numbers}")
    
    fibonacci_position = 10
    fibonacci_value = calculate_fibonacci_number(fibonacci_position)
    print(f"Fibonacci number at position {fibonacci_position}: {fibonacci_value}")
    
    point = Point2D(10, 20)
    print(f"Sum of coordinates: {point.calculate_sum_of_coordinates()}")
    print(f"Both coordinates positive: {point.are_both_coordinates_positive()}")
