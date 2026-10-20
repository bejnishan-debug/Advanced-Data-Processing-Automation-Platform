class DataTransformationService:
    def transform_transactions(self, transactions):
        transformed_transactions=[]
        
        for transaction in transactions:
            amount=transaction.get_amount()
            country = transaction.get_country().strip().title()
            transaction_type = transaction.get_transaction_type().strip().capitalize()
            payment_status = transaction.get_payment_status().strip().capitalize()
            if amount <= 3000:
                amount_category = "Low"
            elif  amount <= 7000:
                amount_category = "medium"
            else:
                amount_category = "high"
            transformed_data={"transaction_id": transaction.get_transaction_id(),
                "customer_id": transaction.get_customer_id(),
                "customer_name": transaction.get_customer_name(),
                "email": transaction.get_email(),
                "phone": transaction.get_phone(),
                "country": country,
                "transaction_date": transaction.get_transaction_date(),
                "transaction_type": transaction_type,
                "amount": amount,
                "payment_status": payment_status,
                "amount_category": amount_category
            }
            transformed_transactions.append(transformed_data)
        return transformed_transactions
        