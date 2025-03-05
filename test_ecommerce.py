import unittest
from solution import (
    Product, 
    CartItem, 
    ShoppingCart, 
    DiscountStrategy,
    # Import the classes that should be implemented by the candidate
    PercentageDiscount,
    BuyOneGetOneFree,
    LoyaltyDiscount,
    Customer
)


class TestProduct(unittest.TestCase):
    """Test the Product class."""
    
    def test_product_creation(self):
        """Test creating a product."""
        product = Product("Test Product", 10.0, "Test Category")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.category, "Test Category")
    
    def test_product_equality(self):
        """Test product equality."""
        product1 = Product("Product 1", 10.0, "Category")
        product2 = Product("Product 1", 10.0, "Category")
        self.assertNotEqual(product1, product2)  # Different objects should not be equal
        self.assertEqual(product1, product1)  # Same object should be equal to itself


class TestCartItem(unittest.TestCase):
    """Test the CartItem class."""
    
    def test_cart_item_creation(self):
        """Test creating a cart item."""
        product = Product("Test Product", 10.0, "Test Category")
        cart_item = CartItem(product, 2)
        self.assertEqual(cart_item.product, product)
        self.assertEqual(cart_item.quantity, 2)
    
    def test_get_subtotal(self):
        """Test calculating the subtotal of a cart item."""
        product = Product("Test Product", 10.0, "Test Category")
        cart_item = CartItem(product, 2)
        self.assertEqual(cart_item.get_subtotal(), 20.0)


class TestShoppingCart(unittest.TestCase):
    """Test the ShoppingCart class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.product1 = Product("Product 1", 10.0, "Category 1")
        self.product2 = Product("Product 2", 20.0, "Category 2")
        self.customer = Customer("Test Customer", "test@example.com")
        self.cart = ShoppingCart(self.customer)
    
    def test_add_item(self):
        """Test adding an item to the cart."""
        self.cart.add_item(self.product1, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].product, self.product1)
        self.assertEqual(self.cart.items[0].quantity, 2)
    
    def test_add_existing_item(self):
        """Test adding an existing item to the cart."""
        self.cart.add_item(self.product1, 2)
        self.cart.add_item(self.product1, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].quantity, 5)
    
    def test_remove_item(self):
        """Test removing an item from the cart."""
        self.cart.add_item(self.product1, 2)
        self.cart.add_item(self.product2, 1)
        self.cart.remove_item(self.product1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0].product, self.product2)
    
    def test_get_subtotal(self):
        """Test calculating the subtotal of the cart."""
        self.cart.add_item(self.product1, 2)  # 2 * $10 = $20
        self.cart.add_item(self.product2, 1)  # 1 * $20 = $20
        self.assertEqual(self.cart.get_subtotal(), 40.0)
    
    def test_apply_discount(self):
        """Test applying a discount to the cart."""
        self.cart.add_item(self.product1, 2)  # 2 * $10 = $20
        self.cart.add_item(self.product2, 1)  # 1 * $20 = $20
        discount = PercentageDiscount(10)  # 10% discount
        self.cart.apply_discount(discount)
        self.assertEqual(self.cart.get_total(), 36.0)  # $40 - 10% = $36
    
    def test_get_recommendations(self):
        """Test getting product recommendations."""
        self.cart.add_item(self.product1, 2)
        recommendations = self.cart.get_recommendations()
        self.assertIsInstance(recommendations, list)
        # The actual recommendations will depend on the implementation


class TestDiscountStrategies(unittest.TestCase):
    """Test the discount strategy classes."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.product1 = Product("Product 1", 10.0, "Category 1")
        self.product2 = Product("Product 2", 20.0, "Category 2")
        self.cart_items = [
            CartItem(self.product1, 2),  # 2 * $10 = $20
            CartItem(self.product2, 1)   # 1 * $20 = $20
        ]
        self.subtotal = 40.0
    
    def test_percentage_discount(self):
        """Test the percentage discount strategy."""
        discount = PercentageDiscount(10)  # 10% discount
        discount_amount = discount.apply_discount(self.cart_items, self.subtotal)
        self.assertEqual(discount_amount, 4.0)  # 10% of $40 = $4
    
    def test_buy_one_get_one_free(self):
        """Test the buy-one-get-one-free discount strategy."""
        discount = BuyOneGetOneFree(self.product1)  # BOGO for product1
        discount_amount = discount.apply_discount(self.cart_items, self.subtotal)
        self.assertEqual(discount_amount, 10.0)  # 1 free product1 = $10
    
    def test_loyalty_discount(self):
        """Test the loyalty discount strategy."""
        customer = Customer("Test Customer", "test@example.com")
        customer.loyalty_tier = "Gold"  # Assuming Gold tier gets 15% discount
        discount = LoyaltyDiscount(customer)
        discount_amount = discount.apply_discount(self.cart_items, self.subtotal)
        self.assertEqual(discount_amount, 6.0)  # 15% of $40 = $6


class TestCustomer(unittest.TestCase):
    """Test the Customer class."""
    
    def test_customer_creation(self):
        """Test creating a customer."""
        customer = Customer("Test Customer", "test@example.com")
        self.assertEqual(customer.name, "Test Customer")
        self.assertEqual(customer.email, "test@example.com")
        self.assertEqual(customer.loyalty_tier, "Bronze")  # Assuming default tier is Bronze
    
    def test_upgrade_loyalty_tier(self):
        """Test upgrading a customer's loyalty tier."""
        customer = Customer("Test Customer", "test@example.com")
        customer.upgrade_loyalty_tier("Silver")
        self.assertEqual(customer.loyalty_tier, "Silver")
    
    def test_calculate_loyalty_points(self):
        """Test calculating a customer's loyalty points."""
        customer = Customer("Test Customer", "test@example.com")
        points = customer.calculate_loyalty_points(100.0)  # Assuming $100 purchase
        self.assertEqual(points, 10)  # Assuming 10 points per $100


if __name__ == "__main__":
    unittest.main() 