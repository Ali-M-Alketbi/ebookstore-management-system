# **E-Bookstore Management System**

# Overview

This project is an implementation of an E-Bookstore Management System in Python. It is designed to enhance the customer experience and streamline internal operations for an e-bookstore. The system includes functionalities for e-book management, customer management, shopping cart operations, order processing, discount application, and invoice generation.

# Features

- E-Book Management: Add, modify, and remove e-books in the    store's catalog.
- Customer Management: Create and manage customer accounts, including loyalty program membership.
- Shopping Cart: Customers can add, update, and remove e-books in their shopping carts.
- Order Processing: Create orders from shopping carts and process them for delivery.
- Discounts and Pricing: Apply loyalty and bulk purchase discounts to eligible orders.
- Payment and Invoicing: Generate invoices detailing itemized prices, discounts, VAT, and the final total.
Project Structure

**The project consists of two main Python files:**

- main.py: Contains all the class definitions for the system.
- test_cases.py: Contains test cases demonstrating all the program's features.

**Class Descriptions**

**EBook**
Represents an e-book in the e-bookstore.

Attributes:

- __title: The title of the e-book.
- __author: The author of the e-book.
- __publication_date: The publication date of the e-book.
- __genre: The genre of the e-book.
- __price: The price of the e-book.

Methods:

- Getters and setters for each attribute.
- __str__(): Returns a string representation of the e-book.
  
**EBookCatalog**

Represents the e-book catalog in the e-bookstore.

Attributes:

- __ebooks: A list of EBook instances.
Methods:
- add_ebook(ebook): Adds an e-book to the catalog.
- remove_ebook(ebook): Removes an e-book from the catalog.
get_ebooks(): Returns the list of e-books.
- __str__(): Returns a string representation of the catalog.
Customer
- Represents a customer of the e-bookstore.

Attributes:

- __name: The name of the customer.
- __contact_info: The contact information of the customer.
- __is_loyalty_member: Indicates if the customer is a loyalty program member.
- __shopping_cart: An instance of ShoppingCart.
  
Methods:

- Getters and setters for each attribute.
- get_shopping_cart(): Returns the customer's shopping cart.
- __str__(): Returns a string representation of the customer.

**ShoppingCart**

Represents a customer's shopping cart.

Attributes:

- __items: A dictionary mapping EBook instances to quantities.
Methods:
- add_item(ebook, quantity): Adds an e-book to the cart.
- remove_item(ebook): Removes an e-book from the cart.
- update_item(ebook, quantity): Updates the quantity of an e-book.
- get_items(): Returns the items in the cart.
get_total_price(): Calculates the total price of the items.
- __str__(): Returns a string representation of the cart.

**Discount (Abstract Class)**

An abstract base class for discounts.

Methods:

- apply_discount(order): Abstract method to apply the discount to an order.

**LoyaltyDiscount**

A discount applied to loyalty program members.

Attributes:

- __discount_percentage: The discount percentage (10%).
Methods:
- apply_discount(order): Applies the loyalty discount.
- __str__(): Returns a string representation of the discount.

**BulkPurchaseDiscount**

A discount applied to bulk purchases.

Attributes:

- __discount_percentage: The discount percentage (20%).
Methods:

- apply_discount(order): Applies the bulk purchase discount.
- __str__(): Returns a string representation of the discount.

**Order**

Represents a customer's order.

Attributes:

- __order_date: The date the order was placed.
- __items: The items included in the order.
- __customer: The customer who placed the order.
- __total_amount: The total amount for the order.
- __discounts_applied: Discounts applied to the order.
  
Methods:

- calculate_total(): Calculates the total amount.
- apply_discounts(discounts): Applies discounts to the order.
- Getters and setters for attributes.
- deliver_ebooks(): Placeholder method for delivery.
- __str__(): Returns a string representation of the order.

**Invoice**

Represents an invoice for an order.

Attributes:

- __order: The associated order.
- __vat_rate: The VAT rate (8%).
- __final_total: The final total including VAT.

Methods:

- generate_invoice(): Calculates the final total.
- calculate_vat(): Calculates the VAT amount.
- __str__(): Returns a string representation of the invoice.

**Requirements**

- Python Version: Python 3.6 or higher
- Modules Used:
    - abc
    - datetime
    - collections
  
**Setup Instructions**

1. Clone the Repository


```bash
      git clone <repository-url>
      cd <repository-directory>
```

2. Ensure Python is Installed

    Make sure Python 3.6 or higher is installed:

```bash
        python3 --version
```

**Running the Test Cases**

1. Navigate to the Project Directory
   

    Open a terminal and navigate to the directory containing main.py and test_cases.py.

2. Run the Test Cases

    Execute the following command:

```bash
    python3 test_cases.py
```

3. Review the Output

        The test cases will run and output results demonstrating the system's features.


**Test Cases Overview**

The test_cases.py script includes the following scenarios:

- E-Book Catalog Operations

    - Adding e-books to the catalog.
    - Modifying an e-book's price.
    - Removing an e-book from the catalog.
  
- Customer Account Operations

    - Creating customer accounts.
    - Modifying customer loyalty status.

- Shopping Cart Operations

    - Adding e-books to shopping carts.
    - Updating item quantities.

- Order Processing

    - Creating orders from shopping carts.
    - Applying discounts (loyalty and bulk purchase).

- Invoice Generation

    - Generating invoices with itemized prices, discounts, VAT, and totals.

**Sample Output**

When you run test_cases.py, you can expect output similar to:

```sql
E-Book Catalog:
EBook(title='Python Programming', author='John Doe', publication_date='2020-01-01', genre='Programming', price=29.99)
EBook(title='Data Science Essentials', author='Jane Smith', publication_date='2019-05-15', genre='Data Science', price=39.99)
EBook(title='Machine Learning', author='Tom Brown', publication_date='2021-07-22', genre='Artificial Intelligence', price=49.99)

Invoice for Customer 1:
Invoice for Order Date: 2023-11-24 02:45:12.345678
Customer: Alice
Items:
  Python Programming x2 @ 29.99 each
  Data Science Essentials x1 @ 39.99 each
Subtotal: 80.97
VAT (8.0%): 6.48
Total Amount Due: 87.45
Discounts Applied: ['LoyaltyDiscount']

Invoice for Customer 2:
Invoice for Order Date: 2023-11-24 02:45:12.456789
Customer: Bob
Items:
  Machine Learning x5 @ 49.99 each
Subtotal: 199.96
VAT (8.0%): 15.997
Total Amount Due: 215.96
Discounts Applied: ['BulkPurchaseDiscount']

Updated E-Book Price:
EBook(title='Python Programming', author='John Doe', publication_date='2020-01-01', genre='Programming', price=24.99)

Updated E-Book Catalog:
EBook(title='Python Programming', author='John Doe', publication_date='2020-01-01', genre='Programming', price=24.99)
EBook(title='Data Science Essentials', author='Jane Smith', publication_date='2019-05-15', genre='Data Science', price=39.99)

Updated Customer Account:
Customer(name='Bob', contact_info='bob@example.com', is_loyalty_member=True)
```

Note: Timestamps and exact values may vary due to the current 
date and floating-point arithmetic.

**Extensibility**

- Adding New Discount Types: Extend the Discount abstract class.
- Enhancing Customer Features: Implement additional attributes or methods in the Customer class.
- Expanding E-Book Information: Add more attributes to the EBook class (e.g., ISBN, language).


**Contact**

For questions or support, please contact aliuae6973@gmail.com.
