import json
import sys
import os
# import platform
import logging, random, datetime
import time
from threading import Thread

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import QtWidgets
from PySide6.QtCore import QThread

from PyQt5 import QtGui
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
from collections import deque
from datetime import datetime as dtime

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
import matplotlib.animation as animation

# from widget_final_different import MplCanvas, Different_charts
# from Exchanges.current_positions import get_current_positions

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

from Exchanges.trade_logic import Trade_logic

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
logging.basicConfig(filename='loging.log', level=logging.ERROR)


# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MplCanvas(FigureCanvas, QThread):
    def __init__(self, parent=None, width=5, height=4, dpi=100, trade_logic=None):
        self.trade_logic = trade_logic
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(211)
        self.axes2 = fig.add_subplot(212)
        # fig, self.axes1 = plt.subplots()
        n_data = 120
        self.xdata = [dtime.now() - datetime.timedelta(seconds=i) for i in range(n_data)]
        self.ydata1 = [0] * n_data
        self.ydata2 = [0] * n_data
        # self.axes2 = self.axes1.twinx()
        self.axes1.plot(self.xdata, self.ydata1, color='r')
        self.axes1.yaxis.tick_right()
        self.axes2.plot(self.xdata, self.ydata2, color='b')
        self.axes2.yaxis.tick_right()

        super(MplCanvas, self).__init__(fig)
        QThread.__init__(self)

    def run(self) -> None:
        while True:
            self.xdata = self.xdata[1:] + [dtime.now()]
            self.ydata1 = self.ydata1[1:] + [(self.trade_logic.balance_bybit + self.trade_logic.balance_binance + self.trade_logic.balance_huobi + self.trade_logic.balance_kucoin)]
            self.axes1.cla()  # Clear the canvas.

            self.axes1.plot(self.xdata, self.ydata1, color='r', label='Баланс')
            self.axes1.set_ylabel('Балансы')
            self.axes1.legend()

            self.ydata2 = self.ydata2[1:] + [self.trade_logic.sum_different]
            self.axes2.cla()  # Clear the canvas.
            self.axes2.plot(self.xdata, self.ydata2, color='b', label='Сумма')
            self.axes2.set_ylabel('Cумма разниц')
            self.axes2.legend()


            # Trigger the canvas to update and redraw.
            self.draw()


class MplCanvas_balances(FigureCanvas, QThread):
    def __init__(self, parent=None, width=5, height=4, dpi=100, trade_logic=None):
        self.trade_logic = trade_logic
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes1 = fig.add_subplot(221)
        self.axes2 = fig.add_subplot(222)
        self.axes3 = fig.add_subplot(223)
        self.axes4 = fig.add_subplot(224)
        super(MplCanvas_balances, self).__init__(fig)
        QThread.__init__(self)
        n_data = 60
        self.xdata = list(range(n_data))
        self.ydata1 = [0] * n_data
        self.ydata2 = [0] * n_data
        self.ydata3 = [0] * n_data
        self.ydata4 = [0] * n_data

    def run(self) -> None:
        while True:
            self.ydata1 = self.ydata1[1:] + [self.trade_logic.balance_binance]
            self.axes1.cla()  # Clear the canvas.
            self.axes1.plot(self.xdata, self.ydata1, 'r')
            self.axes1.title.set_text('Binance')

            self.ydata2 = self.ydata2[1:] + [self.trade_logic.balance_bybit]
            self.axes2.cla()  # Clear the canvas.
            self.axes2.plot(self.xdata, self.ydata2, 'r')
            self.axes2.title.set_text('Bybit')

            self.ydata3 = self.ydata3[1:] + [self.trade_logic.balance_kucoin]
            self.axes3.cla()  # Clear the canvas.
            self.axes3.plot(self.xdata, self.ydata3, 'r')
            self.axes3.title.set_text('Kucoin')

            self.ydata4 = self.ydata4[1:] + [self.trade_logic.balance_huobi]
            self.axes4.cla()  # Clear the canvas.
            self.axes4.plot(self.xdata, self.ydata4, 'r')
            self.axes4.title.set_text('Huobi')

            # Trigger the canvas to update and redraw.
            self.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Futures trade"
        description = "Futures trade (test app)"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        with open('Exchanges/run.json', 'r') as file:
            run_data = json.load(file)
        run_data['websocket'] = True
        run_data['stop'] = False
        run_data['close_all'] = False
        with open(f'Exchanges/run.json', 'w') as file:
            file.write(json.dumps(run_data))

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.trade_logic = Trade_logic()
        self.trade_logic.start()
        self.get_trade_logic_data()

        self.timer = QTimer()
        self.timer.timeout.connect(self.get_trade_logic_data)
        self.timer.start(500)

        # Build Charts
        # ///////////////////////////////////////////////////////////////
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100, trade_logic=self.trade_logic)
        self.companovka = QVBoxLayout(widgets.chart_build)
        self.companovka.addWidget(self.canvas)
        self.canvas.start()

        self.canvas_balances = MplCanvas_balances(self, width=5, height=4, dpi=100, trade_logic=self.trade_logic)
        self.companovka_balances = QVBoxLayout(widgets.chart_build_2)
        self.companovka_balances.addWidget(self.canvas_balances)
        self.canvas_balances.start()

        # INPUT APIS
        # ///////////////////////////////////////////////////////////////
        try:
            with open('Exchanges/api_keys.json', 'r') as file:
                self.data = json.load(file)
        except Exception as error:
            logging.error(f"Found error. error message: {format(error)}")
            self.data = {
                'Binance': {},
                'Bybit': {},
                'Kucoin': {},
                'Huobi': {}
            }
        widgets.binance_key.setText(self.data['Binance'].get('api_key'))
        widgets.binance_secret.setText(self.data['Binance'].get('api_secret'))
        widgets.bybit_key.setText(self.data['Bybit'].get('api_key'))
        widgets.bybit_secret.setText(self.data['Bybit'].get('api_secret'))
        widgets.huobi_key.setText(self.data['Huobi'].get('api_key'))
        widgets.huobi_secret.setText(self.data['Huobi'].get('api_secret'))
        widgets.kucoin_key.setText(self.data['Kucoin'].get('api_key'))
        widgets.kucoin_secret.setText(self.data['Kucoin'].get('api_secret'))
        widgets.kucoin_uid.setText(self.data['Kucoin'].get('uid'))
        widgets.kucoin_passphrase.setText(self.data['Kucoin'].get('api_passphrase'))

        # SAVE PARAMS
        # ///////////////////////////////////////////////////////////////
        try:
            with open('Exchanges/params.json', 'r') as file:
                self.params = json.load(file)
        except Exception as error:
            logging.error(f"Found error. error message: {format(error)}")
            self.params = {
                'binance_symbol_1': ' ',
                'binance_symbol_2': ' ',
                'binance_side_1': ' ',
                'binance_side_2': ' ',
                'binance_qty_1': 0,
                'binance_qty_2': 0,

                'bybit_symbol_1': ' ',
                'bybit_symbol_2': ' ',
                'bybit_side_1': ' ',
                'bybit_side_2': ' ',
                'bybit_qty_1': 0,
                'bybit_qty_2': 0,

                'kucoin_symbol_1': ' ',
                'kucoin_symbol_2': ' ',
                'kucoin_side_1': ' ',
                'kucoin_side_2': ' ',
                'kucoin_qty_1': 0,
                'kucoin_qty_2': 0,

                'huobi_symbol_1': ' ',
                'huobi_symbol_2': ' ',
                'huobi_side_1': ' ',
                'huobi_side_2': ' ',
                'huobi_qty_1': 0,
                'huobi_qty_2': 0,

                'time_work': 15,
                'time_update': 0.5,
                'coefficient': 1,
                'distance_num': 100,
                'profit': 2,
                'loss': 2

            }
        widgets.binance_symbol_1.setText(self.params.get('binance_symbol_1'))
        widgets.binance_symbol_2.setText(self.params.get('binance_symbol_2'))
        widgets.binance_side_1.setCurrentText(self.params.get('binance_side_1'))
        widgets.binance_side_2.setCurrentText(self.params.get('binance_side_2'))
        widgets.binance_qty_1.setText(str(self.params.get('binance_qty_1')))
        widgets.binance_qty_2.setText(str(self.params.get('binance_qty_2')))

        widgets.bybit_symbol_1.setText(self.params.get('bybit_symbol_1'))
        widgets.bybit_symbol_2.setText(self.params.get('bybit_symbol_2'))
        widgets.bybit_side_1.setCurrentText(self.params.get('bybit_side_1'))
        widgets.bybit_side_2.setCurrentText(self.params.get('bybit_side_2'))
        widgets.bybit_qty_1.setText(str(self.params.get('bybit_qty_1')))
        widgets.bybit_qty_2.setText(str(self.params.get('bybit_qty_2')))

        widgets.kucoin_symbol_1.setText(self.params.get('kucoin_symbol_1'))
        widgets.kucoin_symbol_2.setText(self.params.get('kucoin_symbol_2'))
        widgets.kucoin_side_1.setCurrentText(self.params.get('kucoin_side_1'))
        widgets.kucoin_side_2.setCurrentText(self.params.get('kucoin_side_2'))
        widgets.kucoin_qty_1.setText(str(self.params.get('kucoin_qty_1')))
        widgets.kucoin_qty_2.setText(str(self.params.get('kucoin_qty_2')))

        widgets.huobi_symbol_1.setText(self.params.get('huobi_symbol_1'))
        widgets.huobi_symbol_2.setText(self.params.get('huobi_symbol_2'))
        widgets.huobi_side_1.setCurrentText(self.params.get('huobi_side_1'))
        widgets.huobi_side_2.setCurrentText(self.params.get('huobi_side_2'))
        widgets.huobi_qty_1.setText(str(self.params.get('huobi_qty_1')))
        widgets.huobi_qty_2.setText(str(self.params.get('huobi_qty_2')))

        widgets.time_work.setCurrentText(f"{self.params.get('time_work')} мин")
        widgets.time_update.setCurrentText(f"{self.params.get('time_work')} сек")
        widgets.coefficient.setText(str(self.params.get('coefficient')))
        widgets.distance_num.setText(str(self.params.get('distance_num')))
        widgets.profit.setText(str(self.params.get('profit')))
        widgets.loss.setText(str(self.params.get('loss')))

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        widgets.save_keys.clicked.connect(self.buttonClick)
        widgets.btn_save_params.clicked.connect(self.buttonClick)
        widgets.btn_start.clicked.connect(self.buttonClick)
        widgets.btn_start_now.clicked.connect(self.buttonClick)
        widgets.btn_stop.clicked.connect(self.buttonClick)
        widgets.btn_close_all.clicked.connect(self.buttonClick)
        widgets.closeAppBtn.clicked.connect(self.buttonClick)


        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    def get_apis(self):
        self.data['Binance']['api_key'] = widgets.binance_key.text()
        self.data['Binance']['api_secret'] = widgets.binance_secret.text()
        self.data['Bybit']['api_key'] = widgets.bybit_key.text()
        self.data['Bybit']['api_secret'] = widgets.bybit_secret.text()
        self.data['Huobi']['api_key'] = widgets.huobi_key.text()
        self.data['Huobi']['api_secret'] = widgets.huobi_secret.text()
        self.data['Kucoin']['api_key'] = widgets.kucoin_key.text()
        self.data['Kucoin']['api_secret'] = widgets.kucoin_secret.text()
        self.data['Kucoin']['uid'] = widgets.kucoin_uid.text()
        self.data['Kucoin']['api_passphrase'] = widgets.kucoin_passphrase.text()

        with open('Exchanges/api_keys.json', 'w') as file:
            file.write(json.dumps(self.data))
        with open('api_keys.json', 'w') as file:
            file.write(json.dumps(self.data))

    def save_params(self):
        self.params['binance_symbol_1'] = widgets.binance_symbol_1.text()
        self.params['binance_symbol_2'] = widgets.binance_symbol_2.text()
        self.params['binance_side_1'] = widgets.binance_side_1.currentText()
        self.params['binance_side_2'] = widgets.binance_side_2.currentText()
        self.params['binance_qty_1'] = float(widgets.binance_qty_1.text())
        self.params['binance_qty_2'] = float(widgets.binance_qty_2.text())

        self.params['bybit_symbol_1'] = widgets.bybit_symbol_1.text()
        self.params['bybit_symbol_2'] = widgets.bybit_symbol_2.text()
        self.params['bybit_side_1'] = widgets.bybit_side_1.currentText()
        self.params['bybit_side_2'] = widgets.bybit_side_2.currentText()
        self.params['bybit_qty_1'] = float(widgets.bybit_qty_1.text())
        self.params['bybit_qty_2'] = float(widgets.bybit_qty_2.text())

        self.params['kucoin_symbol_1'] = widgets.kucoin_symbol_1.text()
        self.params['kucoin_symbol_2'] = widgets.kucoin_symbol_2.text()
        self.params['kucoin_side_1'] = widgets.kucoin_side_1.currentText()
        self.params['kucoin_side_2'] = widgets.kucoin_side_2.currentText()
        self.params['kucoin_qty_1'] = float(widgets.kucoin_qty_1.text())
        self.params['kucoin_qty_2'] = float(widgets.kucoin_qty_2.text())

        self.params['huobi_symbol_1'] = widgets.huobi_symbol_1.text()
        self.params['huobi_symbol_2'] = widgets.huobi_symbol_2.text()
        self.params['huobi_side_1'] = widgets.huobi_side_1.currentText()
        self.params['huobi_side_2'] = widgets.huobi_side_2.currentText()
        self.params['huobi_qty_1'] = float(widgets.huobi_qty_1.text())
        self.params['huobi_qty_2'] = float(widgets.huobi_qty_2.text())

        self.params['time_work'] = int(widgets.time_work.currentText())
        self.params['time_update'] = float(widgets.time_update.currentText())
        self.params['coefficient'] = float(widgets.coefficient.text())
        self.params['distance_num'] = float(widgets.distance_num.text())
        self.params['profit'] = float(widgets.profit.text())
        self.params['loss'] = float(widgets.loss.text())
        with open('Exchanges/params.json', 'w') as file:
            file.write(json.dumps(self.params))

    def time_check(self, params: dict):
        time_work = params.get('time_work')
        if time_work == 60:
            hour_start = dtime.now().hour + 1
        elif dtime.now().minute < time_work:
            hour_start = dtime.now().hour
        else:
            hour_start = dtime.now().hour + 1
        widgets.command_status.setText(f'Программа начнет роботу в {hour_start}:{time_work if time_work != 60 else 00}')

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.connection_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            widgets.stackedWidget.setCurrentWidget(widgets.balances)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "save_keys":
            self.get_apis()

        if btnName == 'btn_save_params':
            self.save_params()

        if btnName == 'btn_start':
            self.time_check(self.params)
            with open('Exchanges/run.json', 'r') as file:
                run_data = json.load(file)
            run_data['stop'] = True
            run_data['close_all'] = True
            with open(f'Exchanges/run.json', 'w') as file:
                file.write(json.dumps(run_data))

        if btnName == 'btn_start_now':
            widgets.command_status.setText('Старт работы!')
            with open('Exchanges/run.json', 'r') as file:
                run_data = json.load(file)
            run_data['start_now'] = True
            run_data['stop'] = True
            run_data['close_all'] = True
            with open(f'Exchanges/run.json', 'w') as file:
                file.write(json.dumps(run_data))


        if btnName == 'btn_stop':
            widgets.command_status.setText('Остановка логики программы')
            try:
                with open('Exchanges/run.json', 'r') as file:
                    run_data = json.load(file)
            except Exception as error:
                logging.error(f"Found error. error message: {format(error)}")
                with open('Exchanges/run.json', 'r') as file:
                    run_data = json.load(file)
            run_data['stop'] = False
            run_data['start_now'] = False
            try:
                with open(f'Exchanges/run.json', 'w') as file:
                    file.write(json.dumps(run_data))
            except Exception as error:
                logging.error(f"Found error. error message: {format(error)}")
                with open(f'Exchanges/run.json', 'w') as file:
                    file.write(json.dumps(run_data))

        if btnName == 'btn_close_all':
            widgets.command_status.setText('Закрытие текущих позиций')
            try:
                with open('Exchanges/run.json', 'r') as file:
                    run_data = json.load(file)
            except Exception as error:
                logging.error(f"Found error. error message: {format(error)}")
                with open('Exchanges/run.json', 'r') as file:
                    run_data = json.load(file)
            run_data['close_all'] = False
            try:
                with open(f'Exchanges/run.json', 'w') as file:
                    file.write(json.dumps(run_data))
            except Exception as error:
                logging.error(f"Found error. error message: {format(error)}")
                with open(f'Exchanges/run.json', 'w') as file:
                    file.write(json.dumps(run_data))
            Thread(target=self.trade_logic.close_all_positions).start()

        if btnName == 'closeAppBtn':
            with open('Exchanges/run.json', 'r') as file:
                run_data = json.load(file)
            run_data['stop'] = False
            run_data['websocket'] = False
            with open(f'Exchanges/run.json', 'w') as file:
                file.write(json.dumps(run_data))
        #     self.output_field.setText(QCoreApplication.translate("MainWindow", ans, None))
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    def get_trade_logic_data(self):
        info_label_text = f"""
    Binance #1 - {self.trade_logic.binance_price_1}  
    Binance #2 - {self.trade_logic.binance_price_2}  
    
    Kucoin #1 - {self.trade_logic.kucoin_price_1}
    Kucoin #2 - {self.trade_logic.kucoin_price_2}
        
    Bybit #1 - {self.trade_logic.bybit_price_1}      
    Bybit #2 - {self.trade_logic.bybit_price_2}       
        
    Huobi #1 - {self.trade_logic.huobi_price_1}    
    Huobi #2 - {self.trade_logic.huobi_price_2}
    
Cумма расчетов - | {round(self.trade_logic.sum_different, 3)} |
Дистанция (из параметров) - {self.trade_logic.params.get('distance_num')}

Стартовый общий баланс - {round(float(self.trade_logic.start_balances), 2)}
Текущий общий баланс - {round(float(self.trade_logic.current_balances), 2)}

Общая сумма #1 Binance: {self.trade_logic.scores_binance_1}

Общая сумма #1 Kucoin: {self.trade_logic.scores_kucoin_1}

Общая сумма #1 Huobi: {self.trade_logic.scores_huobi_1}

Общая сумма #1 Bybit: {self.trade_logic.scores_bybit_1}

Общая сумма #2 Binance: {self.trade_logic.scores_binance_2}

Общая сумма #2 Kucoin: {self.trade_logic.scores_kucoin_2}

Общая сумма #2 Huobi: {self.trade_logic.scores_huobi_2}

Общая сумма #2 Bybit: {self.trade_logic.scores_bybit_2}
        """
        widgets.info_label.setText(info_label_text)

        positions_text = f"""
    {self.trade_logic.positions_binance}
    {self.trade_logic.positions_kucoin}
    {self.trade_logic.positions_bybit}
    {self.trade_logic.positions_huobi}
"""
        widgets.output_positions.setText(positions_text)

    def get_while_command(self):
        with open('Exchanges/run.json', 'r') as file:
            run_data = json.load(file)
        if run_data['stop']:
            return True
        else:
            return False


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
