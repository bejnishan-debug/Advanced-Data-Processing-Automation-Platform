import csv
from models.transaction import Transaction

class FileService:
    def __init__(self, file_path):
        self.file_path=file_path
    
    def read_transactions(self):
        transactions=[] 
        with open(self.file_path,"r",newline="")  as file:
            reader =csv.reader(file)
            next(reader)
            for row in reader:
                transaction=Transaction(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    float(row[8]),
                    row[9]
                )

                transactions.append(transaction)
            return transactions