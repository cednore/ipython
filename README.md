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