from utils.decorators import log_execution
class TransactionService:

    def __init__(self, file_service, validation_service):
        self.file_service = file_service
        self.validation_service = validation_service

        self.valid_transactions = []
        self.invalid_transactions = []
    @log_execution
    def process_transactions(self):
        self.valid_transactions = []
        self.invalid_transactions = []

        transactions = self.file_service.read_transactions()

        seen_ids = set()

        for transaction in transactions:
            transaction_id = transaction.get_transaction_id()

            if transaction_id in seen_ids:
                self.invalid_transactions.append(
                    (transaction, "Duplicate Transaction ID")
                )
                continue

            seen_ids.add(transaction_id)

            try:
                self.validation_service.validate_transaction(
                    transaction
                )

                self.valid_transactions.append(transaction)

            except (ValueError, TypeError) as error:
                self.invalid_transactions.append(
                    (transaction, str(error))
                )

        return self.valid_transactions, self.invalid_transactions

    def find_transaction(self, transaction_id):
        for transaction in self.valid_transactions:
            if transaction.get_transaction_id() == transaction_id:
                return transaction

        return None

    def get_valid_transactions(self):
        return self.valid_transactions

    def get_invalid_transactions(self):
        return self.invalid_transactions