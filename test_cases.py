# test_cases.py

from main import (
    EBook,
    EBookCatalog,
    Customer,
    Order,
    Invoice,
    LoyaltyDiscount,
    BulkPurchaseDiscount,
)

# Create e-book instances
ebook1 = EBook("Python Programming", "John Doe", "2020-01-01", "Programming", 29.99)
ebook2 = EBook("Data Science Essentials", "Jane Smith", "2019-05-15", "Data Science", 39.99)
ebook3 = EBook("Machine Learning", "Tom Brown", "2021-07-22", "Artificial Intelligence", 49.99)

# Initialize e-book catalog and add e-books
catalog = EBookCatalog()
catalog.add_ebook(ebook1)
catalog.add_ebook(ebook2)
catalog.add_ebook(ebook3)
print("E-Book Catalog:")
for ebook in catalog.get_ebooks():
    print(ebook)
print()

# Create customer accounts
customer1 = Customer("Alice", "alice@example.com", is_loyalty_member=True)
customer2 = Customer("Bob", "bob@example.com", is_loyalty_member=False)

# Add e-books to customer1's shopping cart
customer1.get_shopping_cart().add_item(ebook1, 2)
customer1.get_shopping_cart().add_item(ebook2, 1)

# Add e-books to customer2's shopping cart
customer2.get_shopping_cart().add_item(ebook3, 5)  # Bulk purchase

# Create orders for customers
order1 = Order(customer1)
order2 = Order(customer2)

# Apply discounts
discounts = [LoyaltyDiscount(), BulkPurchaseDiscount()]
order1.apply_discounts(discounts)
order2.apply_discounts(discounts)

# Generate invoices
invoice1 = Invoice(order1)
invoice2 = Invoice(order2)

# Print invoices
print("Invoice for Customer 1:")
print(invoice1)
print("Invoice for Customer 2:")
print(invoice2)

# Modify e-book in catalog
ebook1.set_price(24.99)
print("Updated E-Book Price:")
print(ebook1)
print()

# Remove e-book from catalog
catalog.remove_ebook(ebook3)
print("Updated E-Book Catalog:")
for ebook in catalog.get_ebooks():
    print(ebook)
print()

# Modify customer account
customer2.set_loyalty_member(True)
print("Updated Customer Account:")
print(customer2)
