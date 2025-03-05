from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Set


class Product:
    """
    Represents a product in the e-commerce system.
    """
    
    def __init__(self, name: str, price: float, category: str):
        """
        Initialize a product with name, price, and category.
        
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            category (str): The category of the product.
        """
        self.name = name
        self.price = price
        self.category = category
        self.id = id(self)  # Using object id as a simple unique identifier
    
    def __str__(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name} (${self.price})"
    
    def __eq__(self, other) -> bool:
        """Check if two products are equal based on their id."""
        if not isinstance(other, Product):
            return False
        return self.id == other.id


class CartItem:
    """
    Represents an item in the shopping cart.
    """
    
    def __init__(self, product: Product, quantity: int):
        """
        Initialize a cart item with a product and quantity.
        
        Args:
            product (Product): The product.
            quantity (int): The quantity of the product.
        """
        self.product = product
        self.quantity = quantity
    
    def get_subtotal(self) -> float:
        """Calculate the subtotal for this item."""
        return self.product.price * self.quantity


class DiscountStrategy(ABC):
    """
    Abstract base class for discount strategies.
    
    This class defines the interface for all discount strategies.
    Concrete implementations should override the apply_discount method.
    """
    
    @abstractmethod
    def apply_discount(self, cart_items: List[CartItem], subtotal: float) -> float:
        """
        Apply the discount to the given cart items and subtotal.
        
        Args:
            cart_items (List[CartItem]): The items in the cart.
            subtotal (float): The subtotal before discount.
            
        Returns:
            float: The discount amount.
        """
        pass


# TODO: Implement concrete discount strategy classes
# 1. PercentageDiscount: Applies a percentage discount to the total
# 2. BuyOneGetOneFree: Applies a buy-one-get-one-free discount for specific products
# 3. LoyaltyDiscount: Provides discounts based on customer loyalty tier


# TODO: Implement the Customer class
# The Customer class should have:
# - Attributes for name, email, and loyalty tier
# - Methods to upgrade loyalty tier and calculate loyalty points


class ShoppingCart:
    """
    Represents a shopping cart in the e-commerce system.
    """
    
    def __init__(self, customer=None):
        """
        Initialize an empty shopping cart.
        
        Args:
            customer (Optional[Customer]): The customer who owns this cart.
        """
        self.items: List[CartItem] = []
        self.customer = customer
        self.discount_strategy: Optional[DiscountStrategy] = None
    
    def add_item(self, product: Product, quantity: int) -> None:
        """
        Add a product to the cart.
        
        Args:
            product (Product): The product to add.
            quantity (int): The quantity to add.
        """
        # Check if the product is already in the cart
        for item in self.items:
            if item.product == product:
                item.quantity += quantity
                return
        
        # If not, add a new cart item
        self.items.append(CartItem(product, quantity))
    
    def remove_item(self, product: Product) -> None:
        """
        Remove a product from the cart.
        
        Args:
            product (Product): The product to remove.
        """
        self.items = [item for item in self.items if item.product != product]
    
    def get_subtotal(self) -> float:
        """Calculate the subtotal of all items in the cart."""
        return sum(item.get_subtotal() for item in self.items)
    
    # TODO: Implement the apply_discount method
    # This method should apply the given discount strategy to the cart
    
    # TODO: Implement the get_total method
    # This method should return the total after applying any discounts
    
    # TODO: Implement the get_recommendations method
    # This method should return a list of recommended products based on the cart contents


# TODO: Implement a simple recommendation system
# The recommendation system should suggest products based on the customer's purchase history 