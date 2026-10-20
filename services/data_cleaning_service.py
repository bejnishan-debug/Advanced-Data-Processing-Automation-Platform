

# Customer Name → Remove extra spaces
# Email → Remove extra spaces
# Country → Remove extra spaces
# Transaction Type → Standardize to Purchase / Refund
# Payment Status → Standardize to Completed / Pending / Cancelled

class DataCleaningService:



    def clean_transactions(self, transactions):

        for transaction in transactions:

            transaction.set_customer_name(
                transaction.get_customer_name().strip()
            )

            transaction.set_email(
                transaction.get_email().strip()
            )

            transaction.set_country(
                transaction.get_country().strip()
            )

            transaction.set_transaction_type(
                transaction.get_transaction_type().strip().capitalize()
            )

            transaction.set_payment_status(
                transaction.get_payment_status().strip().capitalize()
            )

        return transactions
    
        