<<<<<<< HEAD
from base import BaseXlsBlock
import xlsxwriter
from datetime import datetime
# класс записывает в Excel-файл информацию о параметрах запроса, включая дату выгрузки и период, за который сделана выгрузка
class Parameters(BaseXlsBlock):
    TITLE = 'Параметры запроса'
    DATE = 'Дата выгрузки'
    SUBTITLE = 'Период, за который сделана выгрузка'
    def writer_some_data(self):
        all_column = self.workbook.add_format(self.column_format)
        all_column.set_text_wrap()
        self.row += 1
        self.worksheet.write(self.row, self.col, self.DATE )
        self.col += 1
        formatted_date = datetime.now().strftime("%Y-%m-%d")
        self.worksheet.write(self.row, self.col, formatted_date, all_column)
        self.col -= 1
        self.row += 1
        self.worksheet.write(self.row, self.col, self.SUBTITLE)
        self.col += 1
        some_dates = []
        for pay in self.some_data['payments']:
            some_dates.append(pay['created_at'])
        some_dates = [datetime.fromisoformat(date[:-1]) for date in some_dates]
        some_dates.sort()
        data_min = some_dates[0].strftime("%Y-%m-%d")
        data_max = some_dates[-1].strftime("%Y-%m-%d")
        some_data = f'{data_min} - {data_max}'
        self.worksheet.write(self.row, self.col, some_data, all_column )

    def writer_header(self):
        hd = self.workbook.add_format(self.header_format)
        hd.set_text_wrap()
        self.worksheet.write(self.row, self.col, self.TITLE,  hd)
# класс создает отчет по активным клиентам, включая топ клиентов по количеству платежей. Он также группирует данные по кварталам
class Report(BaseXlsBlock):
    TITLE = 'Отчет по активным клиентам'
    SUBTITLE = 'Топ клиентов по количеству платежей'

    def writer_header(self):
        hd = self.workbook.add_format(self.header_format)
        hd.set_text_wrap()
        self.row = 5
        self.worksheet.write(self.row, self.col, self.TITLE, hd)
    def writer_some_data(self):
        h1 = self.workbook.add_format(self.title_format)
        h1.set_text_wrap()

        h2 = self.workbook.add_format(self.title2_format)
        h2.set_text_wrap()
        all_column = self.workbook.add_format(self.column_format)
        all_column.set_text_wrap()
        self.row += 1
        self.worksheet.write(self.row, self.col, self.SUBTITLE, h1)
        self.col += 1
        clients_and_payments = []
        for client in self.some_data['clients']:
            for payment in self.some_data['payments']:
                if client['id'] == payment['client_id']:
                    clients_and_payments.append({
                        'fio': client['fio'],
                        'amount': payment['amount'],
                        'created_at' : payment['created_at']
                    })
        clients_and_payments.sort(key=lambda amount:datetime.fromisoformat(amount['created_at']), reverse=True)

        quarters = {}
        for client_payment in clients_and_payments:
            payment_date = datetime.fromisoformat(client_payment['created_at'])
            q = f'Q{(payment_date.month%4 + 1)} {payment_date.year}'
            quarters.setdefault(q, []).append({
                'fio': client_payment['fio'],
                'amount': client_payment['amount']
                })

        for q in quarters:
            self.worksheet.write(self.row, self.col, q, h2)
            srt = sorted(quarters[q], key=lambda amount:amount['amount'])[:10]
            count =0
            for s in srt:
                self.row += 1
                count += 1
                self.worksheet.write(self.row, self.col, f"{count}. { s['fio']}", all_column)
            self.row -= 10
            self.col += 1
#  класс записывает в Excel-файл статистику распределения клиентов по городам
class Geography(BaseXlsBlock):
    TITLE = 'География клиентов'
    SUBTITLE = 'Статистика распределения клиентов'
    CITY = 'Города'
    KOL = 'Количество городов'
    RUSSIA = 'РОССИЯ'
    def writer_header(self):
        h1 = self.workbook.add_format(self.title_format)
        h1.set_text_wrap()
        h1.set_align('center')
        hd = self.workbook.add_format(self.header_format)
        hd.set_text_wrap()
        hd.set_align('center')

        h2 = self.workbook.add_format(self.title2_format)
        h2.set_text_wrap()
        h2.set_align('center')
        self.row =19
        self.worksheet.write(self.row, self.col, self.TITLE, hd)
        self.row +=1
        self.worksheet.write(self.row, self.col, self.SUBTITLE, h1)
        self.worksheet.merge_range('B20:C20', self.RUSSIA, h2)
        self.col+=1
        self.worksheet.write(self.row, self.col, self.CITY, h2)
        self.col+=1
        self.worksheet.write(self.row, self.col, self.KOL, h2)
    def writer_some_data(self):
        all_column = self.workbook.add_format(self.column_format)
        all_column.set_text_wrap()
        self.col -= 1
        self.row += 1
        cities = {}
        for client in self.some_data['clients']:
            city = client['city']
            if city in cities:
                cities[city] += 1
            else:
                cities[city] = 1
        sort_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)
        for city, count in sort_cities[:10]:
            self.worksheet.write(self.row, self.col, city, all_column)
            self.col += 1
            self.worksheet.write(self.row, self.col, count, all_column)
            self.col -= 1
            self.row += 1
# класс создает анализ состояния счета клиентов, включая информацию о задолженности и прибыли
class Status(BaseXlsBlock):
    TITLE = 'АНАЛИЗ СОСТОЯНИЯ СЧЕТА'
    SUBTITLE = 'Статистика состояния счета'
    CLIENT = 'Клиент'
    STATE = 'Состояние счета'
    DEBT = 'Задолженность'
    PROFIT = 'Прибыль'

    def writer_header(self):
        hd = self.workbook.add_format(self.header_format)
        hd.set_text_wrap()
        hd.set_align('center')
        h1 = self.workbook.add_format(self.title_format)
        h1.set_text_wrap()
        h1.set_align('center')
        h2 = self.workbook.add_format(self.title2_format)
        h2.set_text_wrap()
        h2.set_align('center')
        self.col=0
        self.row=33
        self.worksheet.write(self.row,self.col,self.TITLE, hd)
        self.worksheet.merge_range('A35:A36',self.SUBTITLE, h1)
        self.worksheet.merge_range('B35:C35',self.DEBT,h2)
        self.worksheet.merge_range('E35:D35',self.PROFIT, h2)
        self.col+=1
        self.row+=2
        self.worksheet.write(self.row,self.col,self.CLIENT, h2)
        self.col+=1
        self.worksheet.write(self.row,self.col,self.STATE, h2)
        self.col+=1
        self.worksheet.write(self.row,self.col,self.CLIENT, h2)
        self.col+=1
        self.worksheet.write(self.row,self.col,self.STATE, h2)

    def writer_some_data(self):
        all_column = self.workbook.add_format(self.column_format)
        all_column.set_text_wrap()
        self.col=1
        self.row=36

        status = []
        for client in self.some_data['clients']:
            for payment in self.some_data['payments']:
                if client['id'] == payment['client_id']:
                    status.append({
                        'fio': client['fio'],
                        'payment_amount': payment['amount'],
                    })

        status.sort(key=lambda x:x['payment_amount'],reverse=True)

        for s in status[-10:]:
            self.worksheet.write(self.row,self.col,s['fio'], all_column)
            self.col+=1
            self.worksheet.write(self.row,self.col,s['payment_amount'], all_column)
            self.col-=1
            self.row+=1

        self.col=3
        self.row=36

        for s in status[:10]:
            self.worksheet.write(self.row, self.col, s['fio'], all_column)
            self.col += 1
            self.worksheet.write(self.row, self.col, s['payment_amount'], all_column)
            self.col -= 1
            self.row += 1
=======
import xlsxwriter
from datetime import datetime
from base import BaseXlsBlock
from collections import Counter


class HeaderBlock(BaseXlsBlock):
    NAME = "Параметры запроса"
    colNames = ['Дата выгрузки', 'Период, за который сделана выгрузка']

    def writeHeaderCol(self):
        header_format = self.workbook.add_format(
            {'bold': True, 'font_size': '14', 'border': 2, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#fcd5b4'})
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.colNames):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def writeData(self):
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        maxDate, minDate = datetime(1, 1, 1), datetime(3000, 12, 31)
        self.worksheet.write(self.row, 0, datetime.now().strftime('%Y-%m-%d'), subheader_format)
        for payData in self.data['payments']:
            maxDate = max(datetime(*list(map(int, payData["created_at"][:10].split('-')))), maxDate)
            minDate = min(datetime(*list(map(int, payData["created_at"][:10].split('-')))), minDate)

        self.worksheet.write(self.row, 1, f'{minDate.strftime("%Y-%m-%d")} - {maxDate.strftime("%Y-%m-%d")}',
                             subheader_format)


class QuartetPaymentBlock(BaseXlsBlock):
    NAME = "Отчёт по активным клиентам"
    colNames = ['Топ клиентов по количеству платежей', 'Q4 2023', 'Q3 2023', 'Q2 2023', 'Q1 2023', 'Q4 2022']

    def writeHeaderCol(self):
        header_format = self.workbook.add_format(
            {'bold': True, 'font_size': '14', 'border': 2, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#fcd5b4'})
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.colNames):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def writeData(self):
        cell_format = self.workbook.add_format({'font_size': '11', 'align': 'center'})
        quarters = {
            'Q4 2023': [],
            'Q3 2023': [],
            'Q2 2023': [],
            'Q1 2023': [],
            'Q4 2022': [],
        }
        for payment in self.data['payments']:
            client_id = payment['client_id']
            created_at = datetime.strptime(payment['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ")
            quarter = f'Q{(created_at.month - 1) // 3 + 1} {created_at.year}'
            quarters[quarter].append(client_id)

        for quarter in quarters.values():
            self.col += 1
            most_common = Counter(quarter).most_common()[:10]
            for idx, most in enumerate(most_common):
                self.worksheet.write(self.row + idx, self.col, f'{idx + 1}. {self.data["clients"][most[0] - 1]["fio"]}',
                                     cell_format)


class CustomerGeographyBlock(BaseXlsBlock):
    NAME = "География клиентов"
    colNames = ['Статистика распределения клиентов', 'Города', 'Количество клиентов']

    def writeHeaderCol(self):
        header_format = self.workbook.add_format(
            {'bold': True, 'font_size': '14', 'border': 2, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#fcd5b4'})
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.colNames):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def writeData(self):
        cell_format = self.workbook.add_format({'font_size': '11', 'align': 'center'})
        city_counts = {}
        for client in self.data['clients']:
            city = client['city']
            city_counts[city] = city_counts.get(city, 0) + 1

        popular_cities = sorted(city_counts.items(), key=lambda x: x[1], reverse=True)[:10]

        idx = 0
        for city, count in popular_cities:
            self.worksheet.write(self.row + idx, 1, f'{idx + 1}. {city}', cell_format)
            self.worksheet.write(self.row + idx, 2, count, cell_format)
            idx += 1


class BankAccountBlock(BaseXlsBlock):
    NAME = "Анализ состояния счёта"
    colNames = ['Статистика состояния счёта клиента', 'Клиент', 'Состояние счёта', 'Клиент', 'Состояние счёта']

    def writeHeaderCol(self):
        header_format = self.workbook.add_format(
            {'bold': True, 'font_size': '14', 'border': 2, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#fcd5b4'})
        subheader_format = self.workbook.add_format(
            {'bold': True, 'font_size': '10', 'border': 3, 'align': 'center', 'font_name': 'Arial',
             'bg_color': '#c5d9f1'})
        self.worksheet.write(self.row, self.col, self.NAME, header_format)
        self.row += 1
        for idx, name in enumerate(self.colNames):
            self.worksheet.write(self.row, idx, name, subheader_format)
        self.row += 1

    def writeData(self):
        cell_format = self.workbook.add_format({'font_size': '11', 'align': 'center'})
        account_balances = {}
        for payment in self.data['payments']:
            client_id = payment['client_id']
            amount = payment['amount']
            account_balances[client_id] = account_balances.get(client_id, 0) + amount

        debtors = sorted(account_balances.items(), key=lambda x: x[1])[:10]
        rich = sorted(account_balances.items(), key=lambda x: x[1], reverse=True)[:10]

        for idx, debtor in enumerate(debtors):
            self.worksheet.write(self.row + idx, 1, f'{idx + 1}. {self.data["clients"][debtor[0] - 1]["fio"]}',
                                 cell_format)
            self.worksheet.write(self.row + idx, 2, debtor[1], cell_format)
            self.worksheet.write(self.row + idx, 3, f'{idx + 1}. {self.data["clients"][rich[idx][0] - 1]["fio"]}',
                                 cell_format)
            self.worksheet.write(self.row + idx, 4, rich[idx][1], cell_format)
>>>>>>> 8ca2eeef386c20360bbb5f6b8ed0abfe4c98dbf7
