import xlsxwriter
<<<<<<< HEAD
from block import Parameters,Report,Geography,Status
class XlsAnalyticPaymentWriter:
    ANALYTICS_BLOCKS_CLASSES = [
        Parameters,
        Report,
        Geography,
        Status
    ]
    def __init__(self, some_data):
        self.data = some_data
        self.position = 0
    def writer(self, write_file):
        workbook = xlsxwriter.Workbook(write_file)
        worksheet = workbook.add_worksheet()
        worksheet.set_column('A:Z', 35)
        row = 0
        col = 0
        for items in self.ANALYTICS_BLOCKS_CLASSES:
            item_init = items(workbook, worksheet, row, col, self.data)
            item_init.writer_header()
            item_init.writer_some_data()
        workbook.close()
=======
from datetime import datetime
from base import BaseXlsBlock
from block import HeaderBlock, QuartetPaymentBlock, CustomerGeographyBlock, BankAccountBlock

class XlsAnalyticPaymentWriter:
    ANALYTICS_BLOCKS_CLASSES = [
        HeaderBlock,
        QuartetPaymentBlock,
        CustomerGeographyBlock,
        BankAccountBlock,
    ]

    def __init__(self, data):
        self.data = data

    def write_excel_report(self, output_file):
        workbook = xlsxwriter.Workbook(output_file)
        worksheet = workbook.add_worksheet('analytics')
        worksheet.set_column(0, 0, 40)
        worksheet.set_column(1, 5, 40)

        row = 0
        col = 0

        for block_class in self.ANALYTICS_BLOCKS_CLASSES:
            block_instance = block_class(worksheet, workbook, row, col, self.data)
            block_instance.writeHeaderCol()
            block_instance.writeData()
            if row == 0:
                row -= 9
            row += 14

        workbook.close()
>>>>>>> 8ca2eeef386c20360bbb5f6b8ed0abfe4c98dbf7
