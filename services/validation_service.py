import re
from datetime import datetime


class ValidationService:

    def validate_transaction(self, transaction):

        # Transaction ID
        transaction_id = transaction.get_transaction_id()

        if not transaction_id:
            raise ValueError(
                "Transaction ID is empty and cannot be empty"
            )

        # Customer ID
        customer_id = transaction.get_customer_id()

        if not customer_id:
            raise ValueError(
                "Customer ID is empty and cannot be empty"
            )

        # Customer Name
        customer_name = transaction.get_customer_name()

        name_pattern = r'^[A-Za-z ]+$'

        if not customer_name or not re.fullmatch(
            name_pattern,
            customer_name
        ):
            raise ValueError(
                "Customer name must contain only alphabetic characters and spaces"
            )

        # Email
        email = transaction.get_email()

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.fullmatch(email_pattern, email):
            raise ValueError("Invalid email format")

        # Phone
        phone = transaction.get_phone()

        phone_pattern = r'\d{10}'

        if not re.fullmatch(phone_pattern, phone):
            raise ValueError(
                "Phone number must be a 10-digit number"
            )

        # Country
        country = transaction.get_country()

        if not country:
            raise ValueError("Country cannot be empty")

        # Transaction Date
        transaction_date = transaction.get_transaction_date()

        try:
            datetime.strptime(
                transaction_date,
                "%Y-%m-%d"
            )
        except (ValueError, TypeError):
            raise ValueError(
                "Transaction date must be in YYYY-MM-DD format"
            )

        # Transaction Type
        transaction_type = transaction.get_transaction_type()

        valid_types = {"Purchase", "Refund"}

        if transaction_type not in valid_types:
            raise ValueError(
                "Transaction type must be Purchase or Refund"
            )

        # Amount
        amount = transaction.get_amount()

        try:
            if amount < 0:
                raise ValueError(
                    "Amount cannot be negative"
                )
        except TypeError:
            raise TypeError(
                "Amount must be a number"
            )

        # Payment Status
        payment_status = transaction.get_payment_status()

        valid_statuses = {
            "Completed",
            "Pending",
            "Cancelled"
        }

        if payment_status not in valid_statuses:
            raise ValueError(
                "Payment status must be Completed, Pending, or Cancelled"
            )

        return True