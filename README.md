# Python Array Manipulation Challenges

This repository contains coding challenges focused on array manipulation in Python, designed to assess a candidate's ability to work with arrays (lists) and functional programming concepts.

## Challenges Overview

There are two levels of challenges:

### 1. Basic Array Manipulation Challenge

The basic challenge tests a candidate's ability to implement Python equivalents of JavaScript's map, reduce, and filter functions, along with other array operations.

**Functions to implement:**
- `my_map`: Similar to JavaScript's Array.map()
- `my_filter`: Similar to JavaScript's Array.filter()
- `my_reduce`: Similar to JavaScript's Array.reduce()
- `flatten_array`: Flatten a nested array into a single list
- `group_by`: Group array elements by a key
- `chain_operations`: Chain multiple array operations together

**Time Limit:** 10-15 minutes for a senior developer

### 2. Advanced Array Manipulation Challenge

The advanced challenge extends the basic challenge with more complex operations and functional programming concepts.

**Functions to implement:**
- `compose`: Create a function composition (f(g(x)))
- `pipe`: Create a function pipeline (g(f(x)))
- `memoize`: Create a memoized version of a function
- `zip_with`: Apply a function to corresponding elements of multiple arrays
- `partition`: Split an array into two arrays based on a predicate
- `deep_map`: Apply a function to each element in a deeply nested array

**Time Limit:** Additional 10-15 minutes

## Instructions for Candidates

### Basic Challenge:

1. Open the `array_challenge.py` file
2. Implement all the required functions
3. Run the tests using: `python test_array_challenge.py`

### Advanced Challenge:

1. Open the `array_challenge_advanced.py` file
2. Implement all the required functions
3. Run the tests using: `python test_array_challenge_advanced.py`

## Evaluation Criteria

Candidates will be evaluated on:

1. **Correctness**: Do the functions work as expected?
2. **Code Quality**: Is the code clean, readable, and efficient?
3. **Understanding**: Does the candidate demonstrate understanding of functional programming concepts?
4. **Problem-Solving**: How does the candidate approach and solve the problems?

## Tips for Interviewers

- Start with the basic challenge and move to the advanced challenge if the candidate finishes quickly
- Watch how the candidate approaches the problem
- Note if they use list comprehensions, recursion, or other Python idioms
- Pay attention to edge cases (empty lists, None values, etc.)
- Discuss their implementation choices after they complete the challenge

## Files in this Repository

- `array_challenge.py`: Basic challenge for candidates
- `test_array_challenge.py`: Tests for the basic challenge
- `array_challenge_advanced.py`: Advanced challenge for candidates
- `test_array_challenge_advanced.py`: Tests for the advanced challenge
- `array_challenge_solution.py`: Solution for the basic challenge (for interviewers)
- `array_challenge_advanced_solution.py`: Solution for the advanced challenge (for interviewers)

## Running the Tests

To run the tests for the basic challenge:
```
python test_array_challenge.py
```

To run the tests for the advanced challenge:
```
python test_array_challenge_advanced.py
```

# E-Commerce System Challenge

## Problem Statement

You are tasked with extending a simple e-commerce system. The system already has basic product and shopping cart functionality, but it needs to be enhanced with additional features.

## Objective

Complete the implementation of the e-commerce system by:

1. Implementing the `DiscountStrategy` abstract class and its concrete strategy classes
2. Extending the `ShoppingCart` class to apply discounts
3. Creating a `Customer` class with loyalty tiers
4. Implementing a product recommendation system

## Requirements

### Discount Strategies
- Implement `PercentageDiscount`: Applies a percentage discount to the total
- Implement `BuyOneGetOneFree`: Applies a buy-one-get-one-free discount for specific products
- Implement `LoyaltyDiscount`: Provides discounts based on customer loyalty tier

### Customer Class
- Create a `Customer` class with attributes for name, email, and loyalty tier
- Implement methods to upgrade loyalty tier and calculate loyalty points

### Product Recommendation
- Implement a simple recommendation system based on purchase history
- Use appropriate design patterns to make the system extensible

## Example Usage

```python
# Create products
product1 = Product("Laptop", 1000, "Electronics")
product2 = Product("Headphones", 100, "Electronics")

# Create customer
customer = Customer("John Doe", "john@example.com")

# Create shopping cart
cart = ShoppingCart(customer)
cart.add_item(product1, 1)
cart.add_item(product2, 2)

# Apply discount
discount = PercentageDiscount(10)  # 10% discount
cart.apply_discount(discount)

# Get total
print(f"Total: ${cart.get_total()}")  # Should apply the discount

# Get recommendations
recommendations = cart.get_recommendations()
print("Recommended products:", recommendations)
```

## Testing

Run the tests to verify your solution:

```bash
python test_ecommerce.py
```

## Evaluation Criteria

Your solution will be evaluated based on:
1. Proper use of OOP principles (inheritance, encapsulation, polymorphism)
2. Code organization and design patterns
3. Code quality and readability
4. Extensibility of the solution

Good luck! 