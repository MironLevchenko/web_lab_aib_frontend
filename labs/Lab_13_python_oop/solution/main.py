from writer import XlsAnalyticPaymentWriter
import json
from datetime import datetime
import os

def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        some_data = json.load(file)
        return some_data

def main():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_clients = os.path.join(current_directory, '../clients.json')
    file_payments = os.path.join(current_directory, '../payments.json')
    write_file = f"my_payments_analytics_{datetime.now().strftime('%Y-%m-%d')}.xlsx"

    data_clients = read_file(file_clients)
    data_payments = read_file(file_payments)
    some_data = {'clients': data_clients['clients'], 'payments': data_payments['payments']}

    output_directory = os.path.join(current_directory, '..', 'solution')
    output_file = os.path.join(output_directory, write_file)

    analytic_writer = XlsAnalyticPaymentWriter(some_data)
    analytic_writer.writer(output_file)

if __name__ == '__main__':
    main()
