# **E-Bookstore Management System**

## Description

The E-Bookstore Management System is a software application designed to enhance the customer experience and streamline internal operations for an online e-bookstore. The system provides functionalities for managing e-books, customer accounts, shopping carts, orders, discounts, and invoice generation.

# Key Features:


# E-Book Management

- Maintain a comprehensive catalog of e-books.
- Store detailed information: title, author, publication date, genre, and price.
- Add, modify, or remove e-books from the catalog.

# Customer Management

- Create and manage customer accounts.
- Store personal details: name and contact information.
- Browse available e-books.

# Shopping Cart and Orders

- Add, remove, or update quantities of e-books in the shopping cart.
- Place orders reflecting the selected e-books and quantities.
- Instant delivery of e-books upon purchase completion.

# Discounts and Pricing

- Support flexible pricing and discount options.
- Apply a 10% loyalty discount for loyalty program members.
- Apply a 20% bulk purchase discount for orders of 5 or more e-books.

# Payment and Invoicing

- Generate invoices detailing itemized prices and discounts.
- Apply a fixed VAT rate of 8% to all purchases.
- Calculate the final total amount due.

# Installation Instructions

# Prerequisites

- Python 3.x installed on your system.
- Git (optional, for cloning the repository).

# Steps

# Clone the Repository

Using Git (recommended):

bash
Copy code
git clone <https://github.com/your-username/ebookstore-management-system.git>
Or download the ZIP file from the repository and extract it to your desired location.

# Navigate to the Project Directory

bash
Copy code
cd ebookstore-management-system

# Install Dependencies

There are no external dependencies required beyond the Python Standard Library.

# Usage

# Running the Test Cases

The system's features are demonstrated through test cases. Follow these steps to run them:

# Navigate to the tests Directory

bash
Copy code
cd tests

# Run the Test Script

bash
Copy code
python test_cases.py
This script will execute a series of test cases demonstrating:

Adding, modifying, and removing e-books in the catalog.
Creating and updating customer accounts.
Adding e-books to the shopping cart.
Applying loyalty and bulk purchase discounts.
Generating invoices with detailed pricing and discounts.

# Understanding the Code Structure

Main Code (src/ Directory):
ebook.py: Defines the EBook class representing an e-book.
ebook_catalog.py: Manages the EBookCatalog class for the collection of e-books.
customer.py: Contains the Customer class for customer account management.
shopping_cart.py: Implements the ShoppingCart class for cart operations.
order.py: Defines the Order class for processing orders.
invoice.py: Contains the Invoice class for invoice generation.
discount.py: Abstract base class Discount for discount mechanisms.
loyalty_discount.py: Implements the LoyaltyDiscount class.
bulk_purchase_discount.py: Implements the BulkPurchaseDiscount class.
Testing Code (tests/ Directory):

test_cases.py: Script containing test cases to demonstrate system features.

# Extending the System

To extend or customize the system:

Add New Features: Implement additional classes or methods as needed.
Enhance User Interaction: Integrate a user interface or command-line prompts.
Connect to a Database: Modify the code to use a database for persistent storage.
Implement Additional Discounts: Create new discount classes inheriting from Discount.

# Authors

A@li_moh69
