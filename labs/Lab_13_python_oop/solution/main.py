<<<<<<< HEAD
from writer import XlsAnalyticPaymentWriter
import json
from datetime import datetime
def read_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        some_data = json.load(file)
        return some_data

def main():
    file_clients = 'clients.json'
    file_payments = 'payments.json'
    write_file =f"my_payments_analytics_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
    data_clients = read_file(file_clients)
    data_payments = read_file(file_payments)
    some_data = {'clients': data_clients['clients'], 'payments': data_payments['payments']}
    analytic_writer = XlsAnalyticPaymentWriter(some_data)
    analytic_writer.writer(write_file)

if __name__ == '__main__':
    main()
    
=======
import xlsxwriter
import json
from datetime import datetime
from writer import XlsAnalyticPaymentWriter

if __name__ == '__main__':
    with open('clients.json', 'r', encoding='utf-8') as f:
        data_clients = json.load(f)
    with open('payments.json', 'r', encoding='utf-8') as f:
        data_payments = json.load(f)
    data = {'clients': data_clients['clients'], 'payments': data_payments['payments']}

    output = XlsAnalyticPaymentWriter(data)
    output.write_excel_report(f'payments_analytics_{datetime.now().strftime("%Y-%m-%d")}.xlsx')
>>>>>>> 8ca2eeef386c20360bbb5f6b8ed0abfe4c98dbf7
