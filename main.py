from services.file_service import FileService
from services.validation_service import ValidationService
from services.transaction_service import TransactionService
from services.data_cleaning_service import DataCleaningService
from services.data_transformation_service import DataTransformationService
from services.report_service import ReportService
from services.analytics_service import AnalyticsService
from services.transaction_generator import transaction_generator
from services.report_thread_service import ReportThreadService


# File Service
file_service = FileService("data/transactions.csv")


# Validation Service
validation_service = ValidationService()


# Transaction Service
transaction_service = TransactionService(
    file_service,
    validation_service
)


# Process Transactions
valid_transactions, invalid_transactions = (
    transaction_service.process_transactions()
)


# Transaction Generator
generated_transactions = transaction_generator(
    valid_transactions
)

valid_transactions = list(generated_transactions)


# Data Cleaning
data_cleaning_service = DataCleaningService()

clean_transactions = data_cleaning_service.clean_transactions(
    valid_transactions
)


# Data Transformation
data_transformation_service = DataTransformationService()

transformed_transactions = (
    data_transformation_service.transform_transactions(
        clean_transactions
    )
)


# Report Service
report_service = ReportService()


# Thread Service
report_thread_service = ReportThreadService()


# Analytics Service
analytics_service = AnalyticsService(
    transformed_transactions
)


# Report Threads

thread1 = report_thread_service.create_report_thread(
    report_service.generate_valid_transaction_report,
    "output/valid_transactions.txt",
    clean_transactions
)

thread2 = report_thread_service.create_report_thread(
    report_service.generate_invalid_transaction_report,
    "output/invalid_transactions.txt",
    invalid_transactions
)

thread3 = report_thread_service.create_report_thread(
    report_service.generate_transformed_transaction_report,
    "output/transformed_transactions.txt",
    transformed_transactions
)

thread4 = report_thread_service.create_report_thread(
    report_service.generate_summary_report,
    "output/transaction_summary.txt",
    valid_transactions,
    invalid_transactions
)

thread5 = report_thread_service.create_report_thread(
    report_service.generate_analytics_report,
    "output/analytics_report.txt",
    analytics_service
)


# Wait for all report threads to complete

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()


# Display Analytics Results

print("\nAnalytics Results:")

print(
    "Total Transactions:",
    analytics_service.total_transactions()
)

print(
    "Total Transaction Amount:",
    analytics_service.total_transaction_amount()
)

print(
    "Average Transaction Amount:",
    analytics_service.average_transaction_amount()
)

print(
    "Total Purchase Amount:",
    analytics_service.total_purchase_amount()
)

print(
    "Total Refund Amount:",
    analytics_service.total_refund_amount()
)

print(
    "Country-wise Transaction Count:",
    analytics_service.country_wise_transaction_count()
)

print(
    "Country-wise Revenue:",
    analytics_service.country_wise_revenue()
)


# Display Processing Results

print(
    "\nValid Transactions:",
    len(valid_transactions)
)

print(
    "Invalid Transactions:",
    len(invalid_transactions)
)


print("\nInvalid Transaction Details:")

for transaction, reason in invalid_transactions:

    print(
        transaction.get_transaction_id(),
        "->",
        reason
    )