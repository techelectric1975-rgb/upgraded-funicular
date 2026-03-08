"""
Example of poor variable and function naming practices.
This code is functional but difficult to understand due to unclear naming.
"""

def calc(a, b, c):
    """Function with unclear purpose and parameter names."""
    x = a * b
    y = x * c
    z = y * 0.15
    return y - z

def proc(data):
    """Process data with vague function name."""
    return [i * 2 for i in data if i > 0]

def f1(n):
    """Single letter function name with unclear purpose."""
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

class Obj:
    """Class with non-descriptive name."""
    def __init__(self, x, y):
        self.a = x
        self.b = y
    
    def do(self):
        """Method with unclear purpose."""
        return self.a + self.b
    
    def chk(self):
        """Abbreviated method name."""
        return self.a > 0 and self.b > 0

# Usage example
if __name__ == "__main__":
    # Variables with single letters and unclear names
    p = 100
    q = 5
    r = 12
    
    result1 = calc(p, q, r)
    print(f"Result 1: {result1}")
    
    nums = [1, -2, 3, -4, 5]
    result2 = proc(nums)
    print(f"Result 2: {result2}")
    
    n = 10
    result3 = f1(n)
    print(f"Result 3: {result3}")
    
    obj = Obj(10, 20)
    print(f"Object result: {obj.do()}")
    print(f"Check result: {obj.chk()}")
