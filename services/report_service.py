from utils.context_manager import FileContextManager


class ReportService:

    def generate_valid_transaction_report(
        self,
        file_path,
        transactions
    ):
        with FileContextManager(file_path, "w") as file:
            for transaction in transactions:
                file.write(
                    transaction.display_info()
                    + "\n\n"
                )

    def generate_invalid_transaction_report(
        self,
        file_path,
        invalid_transactions
    ):
        with FileContextManager(file_path, "w") as file:
            for transaction, reason in invalid_transactions:
                file.write(
                    f"Transaction ID: "
                    f"{transaction.get_transaction_id()}\n"
                )

                file.write(
                    f"Reason: {reason}\n"
                )

                file.write(
                    transaction.display_info()
                    + "\n\n"
                )

    def generate_transformed_transaction_report(
        self,
        file_path,
        transactions
    ):
        with FileContextManager(file_path, "w") as file:
            for transaction in transactions:
                for key, value in transaction.items():
                    file.write(
                        f"{key}: {value}\n"
                    )

                file.write("\n")

    def generate_summary_report(
        self,
        file_path,
        valid_transactions,
        invalid_transactions
    ):
        with FileContextManager(file_path, "w") as file:
            file.write(
                f"Total Transactions: "
                f"{len(valid_transactions) + len(invalid_transactions)}\n"
            )

            file.write(
                f"Valid Transactions: "
                f"{len(valid_transactions)}\n"
            )

            file.write(
                f"Invalid Transactions: "
                f"{len(invalid_transactions)}\n"
            )
    def generate_analytics_report(
        self,
        file_path,
        analytics_service
    ):
        with FileContextManager(file_path, "w") as file:

            file.write("Analytics Report\n\n")

            file.write(
                f"Total Transactions: "
                f"{analytics_service.total_transactions()}\n"
            )

            file.write(
                f"Total Transaction Amount: "
                f"{analytics_service.total_transaction_amount()}\n"
            )

            file.write(
                f"Average Transaction Amount: "
                f"{analytics_service.average_transaction_amount()}\n"
            )

            file.write(
                f"Total Purchase Amount: "
                f"{analytics_service.total_purchase_amount()}\n"
            )

            file.write(
                f"Total Refund Amount: "
                f"{analytics_service.total_refund_amount()}\n\n"
            )

            file.write("Country-wise Transaction Count:\n")

            file.write(
                f"Country-wise Transaction Count:\n"
            )

            for country, count in (
                analytics_service.country_wise_transaction_count().items()
            ):
                file.write(
                    f"{country}: {count}\n"
                )

            file.write("\nCountry-wise Revenue:\n")

            for country, revenue in (
                analytics_service.country_wise_revenue().items()
            ):
                file.write(
                    f"{country}: {revenue}\n"
                )