# Variable and Function Naming Best Practices

## Overview

This repository demonstrates the importance of using descriptive variable and function names in code. Good naming practices make code more readable, maintainable, and easier to understand for other developers (and your future self).

## Examples

- **example_poor_naming.py** - Code with unclear, abbreviated, and single-letter names
- **example_good_naming.py** - The same functionality with descriptive, clear names

## Key Principles for Good Naming

### 1. Use Descriptive Names

**Bad:**
```python
def calc(a, b, c):
    x = a * b
    y = x * c
    return y
```

**Good:**
```python
def calculate_total_cost(unit_price, quantity, tax_rate):
    subtotal = unit_price * quantity
    total_with_tax = subtotal * tax_rate
    return total_with_tax
```

### 2. Avoid Single-Letter Variables (Except in Limited Contexts)

Single-letter variables are acceptable in:
- Loop counters (i, j, k) in simple loops
- Mathematical formulas where the letters have standard meanings (x, y for coordinates)
- Lambda functions with obvious context

**Bad:**
```python
p = 100
q = 5
r = calculate(p, q)
```

**Good:**
```python
price = 100
quantity = 5
total = calculate(price, quantity)
```

### 3. Use Full Words Instead of Abbreviations

**Bad:**
```python
def chk_usr_auth():
    pass

def proc_data():
    pass
```

**Good:**
```python
def check_user_authentication():
    pass

def process_data():
    pass
```

### 4. Function Names Should Describe Actions

Functions typically perform actions, so use verbs:
- `calculate_`, `process_`, `generate_`, `validate_`, `create_`, `update_`, `delete_`
- Boolean functions should use `is_`, `has_`, `can_`, `should_`

**Bad:**
```python
def data(input):
    pass

def check():
    pass
```

**Good:**
```python
def process_user_data(user_input):
    pass

def is_valid_email():
    pass
```

### 5. Class Names Should Be Nouns

Classes represent things or concepts, so use nouns:

**Bad:**
```python
class Proc:
    pass

class DoStuff:
    pass
```

**Good:**
```python
class DataProcessor:
    pass

class UserAccount:
    pass
```

### 6. Be Consistent with Naming Conventions

Follow the conventions of your programming language:
- Python: `snake_case` for variables and functions, `PascalCase` for classes
- JavaScript: `camelCase` for variables and functions, `PascalCase` for classes
- C#: `PascalCase` for public members, `camelCase` for private members

### 7. Make Boolean Variables Self-Explanatory

**Bad:**
```python
flag = True
status = False
check = validate()
```

**Good:**
```python
is_authenticated = True
has_permission = False
is_valid_input = validate()
```

### 8. Avoid Redundant Context

If the context is clear from the class or module, don't repeat it:

**Bad:**
```python
class User:
    def get_user_name(self):
        return self.user_name
```

**Good:**
```python
class User:
    def get_name(self):
        return self.name
```

### 9. Use Intention-Revealing Names

Names should tell you why something exists, what it does, and how it's used:

**Bad:**
```python
d = 86400  # seconds in a day
```

**Good:**
```python
SECONDS_PER_DAY = 86400
```

### 10. Avoid Mental Mapping

Don't force readers to mentally translate variable names:

**Bad:**
```python
for x in items:
    y = process(x)
    z.append(y)
```

**Good:**
```python
for item in items:
    processed_item = process(item)
    results.append(processed_item)
```

## Running the Examples

To see the examples in action:

```bash
# Run the poorly named version
python example_poor_naming.py

# Run the well-named version
python example_good_naming.py
```

Both programs produce the same output, but the well-named version is much easier to understand and maintain.

## Benefits of Good Naming

1. **Improved Readability** - Code reads almost like natural language
2. **Easier Maintenance** - Future developers (including yourself) can understand the code quickly
3. **Reduced Bugs** - Clear names reduce misunderstandings and mistakes
4. **Better Documentation** - Good names often eliminate the need for comments
5. **Faster Onboarding** - New team members can understand the codebase more quickly

## Resources

- [PEP 8 - Python Style Guide](https://pep8.org/)
- [Clean Code by Robert C. Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [Google Style Guides](https://google.github.io/styleguide/)

## Contributing

If you have additional examples or best practices to share, please feel free to contribute!
