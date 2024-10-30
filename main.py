# main.py

from abc import ABC, abstractmethod
from collections import defaultdict
from datetime import datetime


class EBook:
    """
    Class representing an e-book in the e-bookstore.
    """

    def __init__(self, title, author, publication_date, genre, price):
        """
        Initializes a new EBook instance.

        :param title: The title of the e-book.
        :param author: The author of the e-book.
        :param publication_date: The publication date of the e-book.
        :param genre: The genre of the e-book.
        :param price: The price of the e-book.
        """
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    def get_title(self):
        """Gets the title of the e-book."""
        return self.__title

    def set_title(self, title):
        """Sets the title of the e-book."""
        self.__title = title

    def get_author(self):
        """Gets the author of the e-book."""
        return self.__author

    def set_author(self, author):
        """Sets the author of the e-book."""
        self.__author = author

    def get_publication_date(self):
        """Gets the publication date of the e-book."""
        return self.__publication_date

    def set_publication_date(self, publication_date):
        """Sets the publication date of the e-book."""
        self.__publication_date = publication_date

    def get_genre(self):
        """Gets the genre of the e-book."""
        return self.__genre

    def set_genre(self, genre):
        """Sets the genre of the e-book."""
        self.__genre = genre

    def get_price(self):
        """Gets the price of the e-book."""
        return self.__price

    def set_price(self, price):
        """Sets the price of the e-book."""
        self.__price = price

    def __str__(self):
        """Returns a string representation of the e-book."""
        return (f"EBook(title='{self.__title}', author='{self.__author}', "
                f"publication_date='{self.__publication_date}', genre='{self.__genre}', "
                f"price={self.__price})")


class EBookCatalog:
    """
    Class representing the e-book catalog in the e-bookstore.
    """

    def __init__(self):
        """Initializes the e-book catalog."""
        self.__ebooks = []

    def add_ebook(self, ebook):
        """
        Adds an e-book to the catalog.

        :param ebook: An instance of EBook.
        """
        self.__ebooks.append(ebook)

    def remove_ebook(self, ebook):
        """
        Removes an e-book from the catalog.

        :param ebook: An instance of EBook.
        """
        if ebook in self.__ebooks:
            self.__ebooks.remove(ebook)

    def get_ebooks(self):
        """Returns the list of e-books in the catalog."""
        return self.__ebooks

    def __str__(self):
        """Returns a string representation of the e-book catalog."""
        return f"EBookCatalog(ebooks={self.__ebooks})"


class ShoppingCart:
    """
    Class representing a shopping cart for a customer.
    """

    def __init__(self):
        """Initializes a new ShoppingCart instance."""
        self.__items = defaultdict(int)

    def add_item(self, ebook, quantity=1):
        """
        Adds an e-book to the shopping cart.

        :param ebook: An instance of EBook.
        :param quantity: The quantity to add.
        """
        self.__items[ebook] += quantity

    def remove_item(self, ebook):
        """
        Removes an e-book from the shopping cart.

        :param ebook: An instance of EBook.
        """
        if ebook in self.__items:
            del self.__items[ebook]

    def update_item(self, ebook, quantity):
        """
        Updates the quantity of an e-book in the shopping cart.

        :param ebook: An instance of EBook.
        :param quantity: The new quantity.
        """
        if quantity <= 0:
            self.remove_item(ebook)
        else:
            self.__items[ebook] = quantity

    def get_items(self):
        """Gets the items in the shopping cart."""
        return self.__items

    def get_total_price(self):
        """Calculates the total price of items in the cart."""
        total = sum(ebook.get_price() * quantity for ebook, quantity in self.__items.items())
        return total

    def __str__(self):
        """Returns a string representation of the shopping cart."""
        items_str = ', '.join([f"{ebook.get_title()} (x{quantity})" for ebook, quantity in self.__items.items()])
        return f"ShoppingCart(items=[{items_str}])"


class Customer:
    """
    Class representing a customer in the e-bookstore.
    """

    def __init__(self, name, contact_info, is_loyalty_member=False):
        """
        Initializes a new Customer instance.

        :param name: The name of the customer.
        :param contact_info: The contact information of the customer.
        :param is_loyalty_member: Boolean indicating loyalty program membership.
        """
        self.__name = name
        self.__contact_info = contact_info
        self.__is_loyalty_member = is_loyalty_member
        self.__shopping_cart = ShoppingCart()

    def get_name(self):
        """Gets the customer's name."""
        return self.__name

    def set_name(self, name):
        """Sets the customer's name."""
        self.__name = name

    def get_contact_info(self):
        """Gets the customer's contact information."""
        return self.__contact_info

    def set_contact_info(self, contact_info):
        """Sets the customer's contact information."""
        self.__contact_info = contact_info

    def is_loyalty_member(self):
        """Checks if the customer is a loyalty program member."""
        return self.__is_loyalty_member

    def set_loyalty_member(self, status):
        """Sets the customer's loyalty membership status."""
        self.__is_loyalty_member = status

    def get_shopping_cart(self):
        """Gets the customer's shopping cart."""
        return self.__shopping_cart

    def __str__(self):
        """Returns a string representation of the customer."""
        return (f"Customer(name='{self.__name}', contact_info='{self.__contact_info}', "
                f"is_loyalty_member={self.__is_loyalty_member})")


class Discount(ABC):
    """
    Abstract base class representing a discount.
    """

    @abstractmethod
    def apply_discount(self, order):
        """
        Applies the discount to the order.

        :param order: An instance of Order.
        """
        pass


class LoyaltyDiscount(Discount):
    """
    Class representing a loyalty discount.
    """

    def __init__(self):
        """Initializes a LoyaltyDiscount instance."""
        self.__discount_percentage = 0.10

    def apply_discount(self, order):
        """
        Applies the loyalty discount to the order.

        :param order: An instance of Order.
        """
        if order.get_customer().is_loyalty_member():
            discount_amount = order.get_total_amount() * self.__discount_percentage
            order.set_total_amount(order.get_total_amount() - discount_amount)

    def __str__(self):
        """Returns a string representation of the loyalty discount."""
        return f"LoyaltyDiscount({self.__discount_percentage*100}%)"


class BulkPurchaseDiscount(Discount):
    """
    Class representing a bulk purchase discount.
    """

    def __init__(self):
        """Initializes a BulkPurchaseDiscount instance."""
        self.__discount_percentage = 0.20

    def apply_discount(self, order):
        """
        Applies the bulk purchase discount to the order.

        :param order: An instance of Order.
        """
        total_quantity = sum(order.get_items().values())
        if total_quantity >= 5:
            discount_amount = order.get_total_amount() * self.__discount_percentage
            order.set_total_amount(order.get_total_amount() - discount_amount)

    def __str__(self):
        """Returns a string representation of the bulk purchase discount."""
        return f"BulkPurchaseDiscount({self.__discount_percentage*100}%)"


class Order:
    """
    Class representing an order placed by a customer.
    """

    def __init__(self, customer):
        """
        Initializes a new Order instance.

        :param customer: An instance of Customer.
        """
        self.__order_date = datetime.now()
        self.__items = customer.get_shopping_cart().get_items().copy()
        self.__customer = customer
        self.__total_amount = self.calculate_total()
        self.__discounts_applied = []

    def calculate_total(self):
        """Calculates the total amount for the order."""
        total = sum(ebook.get_price() * quantity for ebook, quantity in self.__items.items())
        return total

    def apply_discounts(self, discounts):
        """
        Applies discounts to the order.

        :param discounts: A list of Discount instances.
        """
        for discount in discounts:
            discount.apply_discount(self)
            self.__discounts_applied.append(discount)

    def get_order_date(self):
        """Gets the date of the order."""
        return self.__order_date

    def get_items(self):
        """Gets the items in the order."""
        return self.__items

    def get_customer(self):
        """Gets the customer who placed the order."""
        return self.__customer

    def get_total_amount(self):
        """Gets the total amount of the order."""
        return self.__total_amount

    def set_total_amount(self, amount):
        """Sets the total amount of the order."""
        self.__total_amount = amount

    def get_discounts_applied(self):
        """Gets the discounts applied to the order."""
        return self.__discounts_applied

    def deliver_ebooks(self):
        """Delivers e-books to the customer (placeholder method)."""
        print("E-books delivered to the customer.")

    def __str__(self):
        """Returns a string representation of the order."""
        items_str = ', '.join([f"{ebook.get_title()} (x{quantity})" for ebook, quantity in self.__items.items()])
        return (f"Order(date='{self.__order_date}', customer='{self.__customer.get_name()}', "
                f"items=[{items_str}], total_amount={self.__total_amount})")


class Invoice:
    """
    Class representing an invoice generated for an order.
    """

    def __init__(self, order):
        """
        Initializes a new Invoice instance.

        :param order: An instance of Order.
        """
        self.__order = order
        self.__vat_rate = 0.08
        self.__final_total = self.generate_invoice()

    def generate_invoice(self):
        """Generates the invoice details."""
        total = self.__order.get_total_amount()
        vat_amount = total * self.__vat_rate
        final_total = total + vat_amount
        return final_total

    def calculate_vat(self):
        """Calculates the VAT for the invoice."""
        return self.__order.get_total_amount() * self.__vat_rate

    def __str__(self):
        """Returns a string representation of the invoice."""
        invoice_details = (f"Invoice for Order Date: {self.__order.get_order_date()}\n"
                           f"Customer: {self.__order.get_customer().get_name()}\n"
                           f"Items:\n")
        for ebook, quantity in self.__order.get_items().items():
            invoice_details += f"  {ebook.get_title()} x{quantity} @ {ebook.get_price()} each\n"
        invoice_details += f"Subtotal: {self.__order.get_total_amount():.2f}\n"
        invoice_details += f"VAT ({self.__vat_rate*100}%): {self.calculate_vat():.2f}\n"
        invoice_details += f"Total Amount Due: {self.__final_total:.2f}\n"
        discounts = [type(d).__name__ for d in self.__order.get_discounts_applied()]
        invoice_details += f"Discounts Applied: {discounts}\n"
        return invoice_details

