# Total Transactions
# Total Transaction Amount
# Average Transaction Amount
# Total Purchase Amount
# Total Refund Amount
# Country-wise Transaction Count
# Country-wise Revenue
from utils.decorators import log_execution

class AnalyticsService:

    def __init__(self, transactions):
        self.transactions = transactions

    def total_transactions(self):
        return len(self.transactions)
    @log_execution
    def total_transaction_amount(self):

        total = 0

        for transaction in self.transactions:
            total += transaction["amount"]

        return total

    def average_transaction_amount(self):

        if not self.transactions:
            return 0

        total = self.total_transaction_amount()

        return total / len(self.transactions)

    def total_purchase_amount(self):

        purchase_transactions = filter(
            lambda transaction:
            transaction["transaction_type"] == "Purchase",
            self.transactions
        )

        purchase_amounts = map(
            lambda transaction: transaction["amount"],
            purchase_transactions
        )

        return sum(purchase_amounts)

    def total_refund_amount(self):

        refund_transactions = filter(
            lambda transaction:
            transaction["transaction_type"] == "Refund",
            self.transactions
        )

        refund_amounts = map(
            lambda transaction: transaction["amount"],
            refund_transactions
        )

        return sum(refund_amounts)

    def country_wise_transaction_count(self):

        country_counts = {}

        for transaction in self.transactions:
            country = transaction["country"]

            if country not in country_counts:
                country_counts[country] = 0

            country_counts[country] += 1

        return country_counts

    def country_wise_revenue(self):

        country_revenues = {}

        for transaction in self.transactions:
            country = transaction["country"]

            if country not in country_revenues:
                country_revenues[country] = 0

            country_revenues[country] += transaction["amount"]

        return country_revenues