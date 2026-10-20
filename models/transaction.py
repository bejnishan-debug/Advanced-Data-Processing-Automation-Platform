class Transaction:

    def __init__(
        self,
        transaction_id,
        customer_id,
        customer_name,
        email,
        phone,
        country,
        transaction_date,
        transaction_type,
        amount,
        payment_status
    ):
        self.__transaction_id = transaction_id
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__email = email
        self.__phone = phone
        self.__country = country
        self.__transaction_date = transaction_date
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__payment_status = payment_status

    def display_info(self):
        return (
            f"transaction_id : {self.__transaction_id}\n"
            f"customer_id : {self.__customer_id}\n"
            f"customer_name : {self.__customer_name}\n"
            f"email : {self.__email}\n"
            f"phone : {self.__phone}\n"
            f"country : {self.__country}\n"
            f"transaction_date : {self.__transaction_date}\n"
            f"transaction_type : {self.__transaction_type}\n"
            f"amount : {self.__amount}\n"
            f"payment_status : {self.__payment_status}"
        )

    def get_transaction_id(self):
        return self.__transaction_id

    def set_transaction_id(self, transaction_id):
        self.__transaction_id = transaction_id

    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_customer_name(self):
        return self.__customer_name

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_transaction_date(self):
        return self.__transaction_date

    def set_transaction_date(self, transaction_date):
        self.__transaction_date = transaction_date

    def get_transaction_type(self):
        return self.__transaction_type

    def set_transaction_type(self, transaction_type):
        self.__transaction_type = transaction_type

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_payment_status(self):
        return self.__payment_status

    def set_payment_status(self, payment_status):
        self.__payment_status = payment_status