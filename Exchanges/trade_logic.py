import json, logging, datetime, time
import asyncio
from threading import Thread

from PySide6.QtCore import QThread

from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient
from pybit import usdt_perpetual
from kucoin_futures.client import WsToken
from kucoin_futures.ws_client import KucoinFuturesWsClient
from huobi.linear_swap.ws.market import Market

from Exchanges.binance_rest import Binance_rest
from Exchanges.kucoin_rest import Kucoin_rest
from Exchanges.bybit_rest import Bybit_rest
from Exchanges.huobi_rest import Huobi_rest

logging.basicConfig(filename='loging.log', level=logging.ERROR)


class Trade_logic(QThread):

    binance_price_1 = 0
    binance_price_2 = 0
    bybit_price_1 = 0
    bybit_price_2 = 0
    kucoin_price_1 = 0
    kucoin_price_2 = 0
    huobi_price_1 = 0
    huobi_price_2 = 0

    final_different_1 = 0
    final_different_2 = 0
    final_different_3 = 0
    final_different_4 = 0
    final_different_5 = 0
    final_different_6 = 0

    sum_different = 0

    scores_binance_1 = 0
    scores_kucoin_1 = 0
    scores_bybit_1 = 0
    scores_huobi_1 = 0
    scores_binance_2 = 0
    scores_kucoin_2 = 0
    scores_bybit_2 = 0
    scores_huobi_2 = 0

    balance_binance = 0
    balance_bybit = 0
    balance_kucoin = 0
    balance_huobi = 0

    positions_binance = 'загрузка...'
    positions_kucoin = 'загрузка...'
    positions_bybit = 'загрузка...'
    positions_huobi = 'загрузка...'

    start_balances = 0
    current_balances = 0

    def __init__(self):
        QThread.__init__(self)
        # Получение параметров
        # while True:
        #     try:
        with open('Exchanges/params.json', 'r') as file:
            self.params = json.load(file)
        with open('Exchanges/api_keys.json', 'r') as apis_file:
            self.apis = json.load(apis_file)
            #     break
            # except:
            #     continue


    # Главная лугика. Заупск start() в main.py
    def run(self) -> None:
        time.sleep(3)
        # Начинаю случать курсы
        thread_websocket = Thread(target=self.run_get_prices)
        thread_websocket.start()

        # Устанавливаю REST API подключение к биржам и максимальное плечо
        self.binance_r_1 = self.create_rest_binance('1', self.params, self.apis)
        self.binance_r_1.set_max_leverage()
        self.binance_r_2 = self.create_rest_binance('2', self.params, self.apis)
        self.binance_r_2.set_max_leverage()

        self.bybit_r_1 = self.create_rest_bybit('1', self.params, self.apis)
        self.bybit_r_1.set_max_leverage()
        self.bybit_r_2 = self.create_rest_bybit('2', self.params, self.apis)
        self.bybit_r_2.set_max_leverage()

        self.kucoin_r_1 = self.create_rest_kucoin('1', self.params, self.apis)
        self.kucoin_r_2 = self.create_rest_kucoin('2', self.params, self.apis)

        self.huobi_r_1 = self.create_rest_huobi('1', self.params, self.apis)
        self.huobi_r_1.set_max_leverage()
        self.huobi_r_2 = self.create_rest_huobi('2', self.params, self.apis)
        self.huobi_r_2.set_max_leverage()
        print("Подключение установлено!")
        time.sleep(2)

        # Курсы с бирж по REST API
        Thread(target=self.get_binance_price_1).start()
        Thread(target=self.get_binance_price_2).start()
        Thread(target=self.get_kucoin_price_1).start()
        Thread(target=self.get_kucoin_price_2).start()

        # Поток получения балансов с бирж
        thread_balances = Thread(target=self.get_balances)
        thread_balances.start()

        # Поток получения открытых позиций с бирж
        thread_positions = Thread(target=self.get_positions)
        thread_positions.start()

        # Поток открытия ордеров для первой проверки на подключение
        thread_orders = Thread()
        time.sleep(10)
        while True:
            # Проверка начала времени старта и пуск логики
            if self.get_while_command() and self.time_check(self.params['time_work']):
                print("Начало работы!")
            # if self.get_while_command():
                time.sleep(3)
                # Цикл расчета
                while self.get_while_command():
                    start_time = time.time()

                    # Стартовый расчет
                    binance_kucoin_1 = self.binance_price_1 - self.kucoin_price_1
                    binance_bybit_1 = self.binance_price_1 - self.bybit_price_1
                    binance_huobi_1 = self.binance_price_1 - self.huobi_price_1
                    kucoin_bybit_1 = self.kucoin_price_1 - self.bybit_price_1
                    kucoin_huobi_1 = self.kucoin_price_1 - self.huobi_price_1
                    bybit_huobi_1 = self.bybit_price_1 - self.huobi_price_1

                    binance_kucoin_2 = self.binance_price_2 - self.kucoin_price_2
                    binance_bybit_2 = self.binance_price_2 - self.bybit_price_2
                    binance_huobi_2 = self.binance_price_2 - self.huobi_price_2
                    kucoin_bybit_2 = self.kucoin_price_2 - self.bybit_price_2
                    kucoin_huobi_2 = self.kucoin_price_2 - self.huobi_price_2
                    bybit_huobi_2 = self.bybit_price_2 - self.huobi_price_2

                    # Решающий расчет
                    self.final_different_1 = binance_kucoin_1 - (binance_kucoin_2 * self.params.get('coefficient'))
                    self.final_different_2 = binance_bybit_1 - (binance_bybit_2 * self.params.get('coefficient'))
                    self.final_different_3 = binance_huobi_1 - (binance_huobi_2 * self.params.get('coefficient'))
                    self.final_different_4 = kucoin_bybit_1 - (kucoin_bybit_2 * self.params.get('coefficient'))
                    self.final_different_5 = kucoin_huobi_1 - (kucoin_huobi_2 * self.params.get('coefficient'))
                    self.final_different_6 = bybit_huobi_1 - (bybit_huobi_2 * self.params.get('coefficient'))

                    self.sum_different = self.final_different_1 + self.final_different_2 + self.final_different_3 + \
                                         self.final_different_4 + self.final_different_5 + self.final_different_6

                    # Размещение ордеров если модуль общей суммы больше дистанции и поток с открытием ордеров не запущен
                    # Общие суммы не переписываются, пока запущен поток с открытыми позициями
                    if abs(self.sum_different) > self.params.get('distance_num') and not thread_orders.is_alive():
                        # Обнуляю общий счет при новом цикле
                        self.scores_binance_1 = 0
                        self.scores_kucoin_1 = 0
                        self.scores_bybit_1 = 0
                        self.scores_huobi_1 = 0
                        self.scores_binance_2 = 0
                        self.scores_kucoin_2 = 0
                        self.scores_bybit_2 = 0
                        self.scores_huobi_2 = 0

                        if binance_kucoin_1 > 0:
                            self.scores_binance_1 += 1
                            self.scores_kucoin_1 -= 1
                        else:
                            self.scores_binance_1 -= 1
                            self.scores_kucoin_1 += 1

                        if binance_bybit_1 > 0:
                            self.scores_binance_1 += 1
                            self.scores_bybit_1 -= 1
                        else:
                            self.scores_binance_1 -= 1
                            self.scores_bybit_1 += 1

                        if binance_huobi_1 > 0:
                            self.scores_binance_1 += 1
                            self.scores_huobi_1 -= 1
                        else:
                            self.scores_binance_1 -= 1
                            self.scores_huobi_1 += 1

                        if kucoin_bybit_1 > 0:
                            self.scores_kucoin_1 += 1
                            self.scores_bybit_1 -= 1
                        else:
                            self.scores_kucoin_1 -= 1
                            self.scores_bybit_1 += 1

                        if kucoin_huobi_1 > 0:
                            self.scores_kucoin_1 += 1
                            self.scores_huobi_1 -= 1
                        else:
                            self.scores_kucoin_1 -= 1
                            self.scores_huobi_1 += 1

                        if bybit_huobi_2 > 0:
                            self.scores_bybit_1 += 1
                            self.scores_huobi_1 -= 1
                        else:
                            self.scores_bybit_1 -= 1
                            self.scores_huobi_1 += 1

                        if binance_kucoin_2 > 0:
                            self.scores_binance_2 += 1
                            self.scores_kucoin_2 -= 1
                        else:
                            self.scores_binance_2 -= 1
                            self.scores_kucoin_2 += 1

                        if binance_bybit_2 > 0:
                            self.scores_binance_2 += 1
                            self.scores_bybit_2 -= 1
                        else:
                            self.scores_binance_2 -= 1
                            self.scores_bybit_2 += 1

                        if binance_huobi_2 > 0:
                            self.scores_binance_2 += 1
                            self.scores_huobi_2 -= 1
                        else:
                            self.scores_binance_2 -= 1
                            self.scores_huobi_2 += 1

                        if kucoin_bybit_2 > 0:
                            self.scores_kucoin_2 += 1
                            self.scores_bybit_2 -= 1
                        else:
                            self.scores_kucoin_2 -= 1
                            self.scores_bybit_2 += 1

                        if kucoin_huobi_2 > 0:
                            self.scores_kucoin_2 += 1
                            self.scores_huobi_2 -= 1
                        else:
                            self.scores_kucoin_2 -= 1
                            self.scores_huobi_2 += 1

                        if bybit_huobi_2 > 0:
                            self.scores_bybit_2 += 1
                            self.scores_huobi_2 -= 1
                        else:
                            self.scores_bybit_2 -= 1
                            self.scores_huobi_2 += 1

                        self.scores_dict = {
                            '1': {
                                'Binance': self.scores_binance_1,
                                'Kucoin': self.scores_kucoin_1,
                                'Bybit': self.scores_bybit_1,
                                'Huobi': self.scores_huobi_1
                            },
                            '2': {
                                'Binance': self.scores_binance_2,
                                'Kucoin': self.scores_kucoin_2,
                                'Bybit': self.scores_bybit_2,
                                'Huobi': self.scores_huobi_2
                            }
                        }

                        # Запускаю поток с открытием и закрытием ордеров
                        thread_orders = Thread(target=self.main_open_orders)
                        thread_orders.start()

                    if (time.time() - start_time) < 0.5:
                        time.sleep(0.5 - (time.time() - start_time))
                self.final_different_1 = 0
                self.final_different_2 = 0
                self.final_different_3 = 0
                self.final_different_4 = 0
                self.final_different_5 = 0
                self.final_different_6 = 0
                self.sum_different = 0
                self.scores_binance_1 = 0
                self.scores_kucoin_1 = 0
                self.scores_bybit_1 = 0
                self.scores_huobi_1 = 0
                self.scores_binance_2 = 0
                self.scores_kucoin_2 = 0
                self.scores_bybit_2 = 0
                self.scores_huobi_2 = 0

                ################# Открытие и закрытие позицийй #########################
    def main_open_orders(self):
        self.start_balances = self.balance_binance + self.balance_kucoin + self.balance_bybit + self.balance_huobi

        # Открываю позиции на биржах
        thread_binance_1 = Thread(target=self.open_position, args=('Binance', '1', self.binance_r_1))
        thread_binance_1.start()
        thread_binance_2 = Thread(target=self.open_position, args=('Binance', '2', self.binance_r_2))
        thread_binance_2.start()

        thread_bybit_1 = Thread(target=self.open_position, args=('Bybit', '1', self.bybit_r_1))
        thread_bybit_1.start()
        thread_bybit_2 = Thread(target=self.open_position, args=('Bybit', '2', self.bybit_r_2))
        thread_bybit_2.start()

        thread_kucoin_1 = Thread(target=self.open_position, args=('Kucoin', '1', self.kucoin_r_1))
        thread_kucoin_1.start()
        thread_kucoin_2 = Thread(target=self.open_position, args=('Kucoin', '2', self.kucoin_r_2))
        thread_kucoin_2.start()

        thread_huobi_1 = Thread(target=self.open_position, args=('Huobi', '1', self.huobi_r_1))
        thread_huobi_1.start()
        thread_huobi_2 = Thread(target=self.open_position, args=('Huobi', '2', self.huobi_r_2))
        thread_huobi_2.start()

        thread_binance_1.join()
        thread_binance_2.join()
        thread_bybit_1.join()
        thread_bybit_2.join()
        thread_kucoin_1.join()
        thread_kucoin_2.join()
        thread_huobi_1.join()
        thread_huobi_2.join()
        time.sleep(3)

        # Цикл контроля условий - прибль или убыток либо нажатие кнопки "Закрыть все"
        flag = True
        while flag:
            self.current_balances = self.balance_binance + self.balance_kucoin + self.balance_bybit + self.balance_huobi

            if (self.start_balances - self.current_balances) > self.params.get('loss') \
                    or (self.current_balances - self.start_balances) > self.params.get('profit'):
                print('Close ALL POSITIONS!!!!!')
                self.close_all_positions()
                time.sleep(5)
                flag = False
                break

            if not self.get_while_command_all():
                print('Close ALL POSITIONS TRUE TRUE TRUE!!!!!')
                # self.close_all_positions()
                with open('Exchanges/run.json', 'r') as file:
                    run_data = json.load(file)
                run_data['close_all'] = True
                with open(f'Exchanges/run.json', 'w') as file:
                    file.write(json.dumps(run_data))
                time.sleep(5)
                flag = False
                break

    ################# Слушает изменение курсов #########################
    def run_get_prices(self) -> None:
        # asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        # asyncio.run(self.open_ws())
        self.open_ws()

    def open_ws(self) -> None:
        def close_ws():
            logging.debug("closing ws connection")
            UMFuturesWebsocketClient().stop()

        # Open Kucoin websocket
        # async def message_handler_kucoin(message):
        #     is_empty = self.is_empty_message(message)
        #     if is_empty:
        #         time.sleep(0.01)
        #     else:
        #         if message['data'].get('price') is not None:
        #             if self.params.get('kucoin_symbol_1') in message.get('topic').split(':')[-1]:
        #                 self.kucoin_price_1 = float(message['data'].get('price'))
        #             elif self.params.get('kucoin_symbol_2') in message.get('topic').split(':')[-1]:
        #                 self.kucoin_price_2 = float(message['data'].get('price'))
        #             elif self.params.get('kucoin_symbol_1') == 'BTC' and 'XBT' in message.get('topic').split(':')[-1]:
        #                 self.kucoin_price_1 = float(message['data'].get('price'))
        #             elif self.params.get('kucoin_symbol_2') == 'BTC' and 'XBT' in message.get('topic').split(':')[-1]:
        #                 self.kucoin_price_2 = float(message['data'].get('price'))
        #
        # client = WsToken()
        # ws_client = await KucoinFuturesWsClient.create(None, client, message_handler_kucoin, private=False)
        # await ws_client.subscribe(
        #     f'/contractMarket/execution:{self.params["kucoin_symbol_1"].upper() if self.params["kucoin_symbol_1"].upper() != "BTC" else "XBT"}USDTM')
        # await ws_client.subscribe(
        #     f'/contractMarket/execution:{self.params["kucoin_symbol_2"].upper() if self.params["kucoin_symbol_2"].upper() != "BTC" else "XBT"}USDTM')

        # # Open Binance websocket
        # def message_handler_binance(message):
        #     is_empty = self.is_empty_message(message)
        #     if is_empty:
        #         time.sleep(0.01)
        #     else:
        #         if message.get('c') is not None:
        #             if self.params.get('binance_symbol_1') in message.get('s'):
        #                 self.binance_price_1 = float(message.get('c'))
        #             elif self.params.get('binance_symbol_2') in message.get('s'):
        #                 self.binance_price_2 = float(message.get('c'))
        #
        # ws_binance = UMFuturesWebsocketClient()
        # ws_binance.start()
        # ws_binance.mini_ticker(id=1, callback=message_handler_binance,
        #                        symbol=f'{self.params["binance_symbol_1"].lower()}usdt')
        # ws_binance.mini_ticker(id=1, callback=message_handler_binance,
        #                        symbol=f'{self.params["binance_symbol_2"].lower()}usdt')

        # Open Bybit websocket
        def message_handler_bybit(message):
            is_empty = self.is_empty_message(message)
            if is_empty:
                time.sleep(0.01)
            else:
                if message['data'][0].get('price') is not None:
                    if self.params.get('bybit_symbol_1') in message['data'][0].get('symbol'):
                        self.bybit_price_1 = float(message['data'][0].get('price'))
                    elif self.params.get('bybit_symbol_2') in message['data'][0].get('symbol'):
                        self.bybit_price_2 = float(message['data'][0].get('price'))

        ws_bybit = usdt_perpetual.WebSocket(
            test=False,
            ping_interval=30,  # the default is 30
            ping_timeout=10,  # the default is 10
            domain="bybit"  # the default is "bybit"
        )
        ws_bybit.trade_stream(message_handler_bybit, f'{self.params["bybit_symbol_1"].upper()}USDT')
        ws_bybit.trade_stream(message_handler_bybit, f'{self.params["bybit_symbol_2"].upper()}USDT')

        # Open Huobi websocket
        def message_handler_huobi(message):
            is_empty = self.is_empty_message(message)
            if is_empty:
                time.sleep(0.01)
            else:
                if message['tick']['data'][0].get('price') is not None:
                    if self.params.get('huobi_symbol_1') in message.get('ch').split('.')[1].replace('-', ''):
                        self.huobi_price_1 = float(message['tick']['data'][0].get('price'))
                    elif self.params.get('huobi_symbol_2') in message.get('ch').split('.')[1].replace('-', ''):
                        self.huobi_price_2 = float(message['tick']['data'][0].get('price'))

        ws_huobi = Market()
        ws_huobi.sub({"sub": f'market.{self.params["huobi_symbol_1"]}-USDT.trade.detail'}, message_handler_huobi)
        ws_huobi.sub({"sub": f'market.{self.params["huobi_symbol_2"]}-USDT.trade.detail'}, message_handler_huobi)

        while self.get_websocket_command():
            time.sleep(5)
        close_ws()

    def get_binance_price_1(self):
        while self.get_websocket_command():
            try:
                self.binance_price_1 = self.binance_r_1.get_price()
            except:
                continue

    def get_binance_price_2(self):
        while self.get_websocket_command():
            try:
                self.binance_price_2 = self.binance_r_2.get_price()
            except:
                continue

    def get_kucoin_price_1(self):
        while self.get_websocket_command():
            try:
                self.kucoin_price_1 = self.kucoin_r_1.get_price()
            except:
                continue

    def get_kucoin_price_2(self):
        while self.get_websocket_command():
            try:
                self.kucoin_price_2 = self.kucoin_r_2.get_price()
            except:
                continue

    ################# Получение балансов с бирж #########################
    def get_balances(self):
        thread_binance = Thread(target=self.get_balances_binance)
        thread_binance.start()
        thread_bybit = Thread(target=self.get_balances_bybit)
        thread_bybit.start()
        thread_kucoin = Thread(target=self.get_balances_kucoin)
        thread_kucoin.start()
        thread_huobi = Thread(target=self.get_balances_huobi)
        thread_huobi.start()

    def get_balances_binance(self):
        while True:
            try:
                self.balance_binance = self.binance_r_1.get_balance()
            except:
                continue
            time.sleep(0.2)

    def get_balances_bybit(self):
        while True:
            try:
                self.balance_bybit = self.bybit_r_1.get_balance()
            except:
                continue
            time.sleep(0.5)

    def get_balances_kucoin(self):
        while True:
            try:
                self.balance_kucoin = self.kucoin_r_1.get_balance()
            except:
                continue
            time.sleep(0.2)

    def get_balances_huobi(self):
        while True:
            try:
                self.balance_huobi = self.huobi_r_1.get_balance()
            except:
                continue
            time.sleep(0.2)

    ################# Получение позиций с бирж #########################
    def get_positions(self):
        while True:
            try:
                pos_binance_1 = Thread(target=self.get_position_binance_1)
                pos_binance_2 = Thread(target=self.get_position_binance_2)
                pos_kucoin_1 = Thread(target=self.get_position_kucoin_1)
                pos_kucoin_2 = Thread(target=self.get_position_kucoin_2)
                pos_bybit_1 = Thread(target=self.get_position_bybit_1)
                pos_bybit_2 = Thread(target=self.get_position_bybit_2)
                pos_huobi_1 = Thread(target=self.get_position_huobi_1)
                pos_huobi_2 = Thread(target=self.get_position_huobi_2)

                pos_binance_1.start()
                pos_binance_2.start()
                pos_kucoin_1.start()
                pos_kucoin_2.start()
                pos_bybit_1.start()
                pos_bybit_2.start()
                pos_huobi_1.start()
                pos_huobi_2.start()

                pos_binance_1.join()
                pos_binance_2.join()
                pos_kucoin_1.join()
                pos_kucoin_2.join()
                pos_bybit_1.join()
                pos_bybit_2.join()
                pos_huobi_1.join()
                pos_huobi_2.join()

                self.positions_binance = f"Binance -> {self.curpos_binance_1.get('symbol')}, " \
                                        f"сторона: {self.curpos_binance_1.get('side')}, " \
                                        f"объем: {self.curpos_binance_1.get('qty')}, " \
                                        f"профит: {self.curpos_binance_1.get('profit')}   " \
                                        f"{self.curpos_binance_2.get('symbol')}, " \
                                        f"сторона: {self.curpos_binance_2.get('side')}, " \
                                        f"объем: {self.curpos_binance_2.get('qty')}, " \
                                        f"профит: {self.curpos_binance_2.get('profit')}   "

                self.positions_kucoin = f"Kucoin -> {self.curpos_kucoin_1.get('symbol')}, " \
                                         f"сторона: {self.curpos_kucoin_1.get('side')}, " \
                                         f"объем: {self.curpos_kucoin_1.get('qty')}, " \
                                         f"профит: {self.curpos_kucoin_1.get('profit')}   " \
                                         f"{self.curpos_kucoin_2.get('symbol')}, " \
                                         f"сторона: {self.curpos_kucoin_2.get('side')}, " \
                                         f"объем: {self.curpos_kucoin_2.get('qty')}, " \
                                         f"профит: {self.curpos_kucoin_2.get('profit')}   "

                self.positions_bybit = f"Bybit -> {self.curpos_bybit_1.get('symbol')}, " \
                                         f"сторона: {self.curpos_bybit_1.get('side')}, " \
                                         f"объем: {self.curpos_bybit_1.get('qty')}, " \
                                         f"профит: {self.curpos_bybit_1.get('profit')}   " \
                                         f"{self.curpos_bybit_2.get('symbol')}, " \
                                         f"сторона: {self.curpos_bybit_2.get('side')}, " \
                                         f"объем: {self.curpos_bybit_2.get('qty')}, " \
                                         f"профит: {self.curpos_bybit_2.get('profit')}   "

                self.positions_huobi = f"Huobi -> {self.curpos_huobi_1.get('symbol')}, " \
                                         f"сторона: {self.curpos_huobi_1.get('side')}, " \
                                         f"объем: {self.curpos_huobi_1.get('qty')}, " \
                                         f"профит: {self.curpos_huobi_1.get('profit')}   " \
                                         f"{self.curpos_huobi_2.get('symbol')}, " \
                                         f"сторона: {self.curpos_huobi_2.get('side')}, " \
                                         f"объем: {self.curpos_huobi_2.get('qty')}, " \
                                         f"профит: {self.curpos_huobi_2.get('profit')}   "
                time.sleep(1)
            except Exception as er:
                logging.error(er)
                continue

    def get_position_binance_1(self):
        self.curpos_binance_1 = self.binance_r_1.get_open_positions()

    def get_position_binance_2(self):
        self.curpos_binance_2 = self.binance_r_2.get_open_positions()

    def get_position_kucoin_1(self):
        self.curpos_kucoin_1 = self.kucoin_r_1.get_open_positions()

    def get_position_kucoin_2(self):
        self.curpos_kucoin_2 = self.kucoin_r_2.get_open_positions()

    def get_position_bybit_1(self):
        self.curpos_bybit_1 = self.bybit_r_1.get_open_positions()

    def get_position_bybit_2(self):
        self.curpos_bybit_2 = self.bybit_r_2.get_open_positions()

    def get_position_huobi_1(self):
        self.curpos_huobi_1 = self.huobi_r_1.get_open_positions()

    def get_position_huobi_2(self):
        self.curpos_huobi_2 = self.huobi_r_2.get_open_positions()

    ################# Служебные методы #########################
    def is_empty_message(self, message):
        if message is False:
            return True
        if '"result":null' in message:
            return True
        if '"result":None' in message:
            return True
        return False

    def time_check(self, time_work: int) -> bool:
        if time_work == 60:
            hour_start = datetime.datetime.now().hour + 1
        elif datetime.datetime.now().minute < time_work:
            hour_start = datetime.datetime.now().hour
        else:
            hour_start = datetime.datetime.now().hour + 1
        print(f'Time to start: {hour_start}:{time_work if time_work != 60 else 00}')
        while self.get_while_command():
            with open('Exchanges/run.json', 'r') as file:
                run_data = json.load(file)
            if datetime.datetime.now().hour == hour_start and (datetime.datetime.now().minute == time_work or time_work == 60):
                print('Start program!')
                return True
            elif run_data.get('start_now') == True:
                return True
            else:
                time.sleep(2)
                continue
        return False

    def close_all_positions(self):
        thread_binance_1 = Thread(target=self.close_position_binance_1)
        thread_binance_1.start()
        thread_binance_2 = Thread(target=self.close_position_binance_2)
        thread_binance_2.start()

        thread_bybit_1 = Thread(target=self.close_position_bybit_1)
        thread_bybit_1.start()
        thread_bybit_2 = Thread(target=self.close_position_bybit_2)
        thread_bybit_2.start()

        thread_kucoin_1 = Thread(target=self.close_position_kucoin_1)
        thread_kucoin_1.start()
        thread_kucoin_2 = Thread(target=self.close_position_kucoin_2)
        thread_kucoin_2.start()

        thread_huobi_1 = Thread(target=self.close_position_huobi_1)
        thread_huobi_1.start()
        thread_huobi_2 = Thread(target=self.close_position_huobi_2)
        thread_huobi_2.start()

        thread_binance_1.join()
        thread_binance_2.join()
        thread_bybit_1.join()
        thread_bybit_2.join()
        thread_kucoin_1.join()
        thread_kucoin_2.join()
        thread_huobi_1.join()
        thread_huobi_2.join()

    def close_position_binance_1(self):
        if self.curpos_binance_1.get('side') != None and self.curpos_binance_1.get('qty') != None:
            self.binance_r_1.futures_market(
                'BUY' if self.curpos_binance_1.get('side').upper() == 'SELL' else 'SELL',
                self.curpos_binance_1.get('qty')
            )

    def close_position_binance_2(self):
        if self.curpos_binance_2.get('side') != None and self.curpos_binance_2.get('qty') != None:
            self.binance_r_2.futures_market(
                'BUY' if self.curpos_binance_2.get('side').upper() == 'SELL' else 'SELL',
                self.curpos_binance_2.get('qty')
            )

    def close_position_bybit_1(self):
        if self.curpos_bybit_1.get('side') != None and self.curpos_bybit_1.get('qty') != None:
            self.bybit_r_1.futures_market(
                'BUY' if self.curpos_bybit_1.get('side').upper() == 'SELL' else 'SELL',
                self.curpos_bybit_1.get('qty'),
                True
            )

    def close_position_bybit_2(self):
        if self.curpos_bybit_2.get('side') != None and self.curpos_bybit_2.get('qty') != None:
            self.bybit_r_2.futures_market(
                'BUY' if self.curpos_bybit_2.get('side').upper() == 'SELL' else 'SELL',
                self.curpos_bybit_2.get('qty'),
                True
            )

    def close_position_kucoin_1(self):
        if self.curpos_kucoin_1.get('side') != None and self.curpos_kucoin_1.get('qty') != None:
            self.kucoin_r_1.futures_market(
                'BUY' if self.curpos_kucoin_1.get('side').upper() == 'SELL' else 'SELL',
                self.curpos_kucoin_1.get('qty')
            )

    def close_position_kucoin_2(self):
        if self.curpos_kucoin_2.get('side') != None and self.curpos_kucoin_2.get('qty') != None:
            self.kucoin_r_2.futures_market(
                'BUY' if self.curpos_kucoin_2.get('side').upper() == 'SELL' else 'SELL',
                self.curpos_kucoin_2.get('qty')
            )

    def close_position_huobi_1(self):
        if self.curpos_huobi_1.get('side') != None and self.curpos_huobi_1.get('qty') != None:
            self.huobi_r_1.futures_market(
                'BUY' if self.curpos_huobi_1.get('side').upper() == 'SELL' else 'SELL',
                self.curpos_huobi_1.get('qty')
            )

    def close_position_huobi_2(self):
        if self.curpos_huobi_2.get('side') != None and self.curpos_huobi_2.get('qty') != None:
            self.huobi_r_2.futures_market(
                'BUY' if self.curpos_huobi_2.get('side').upper() == 'SELL' else 'SELL',
                self.curpos_huobi_2.get('qty')
            )

    # def close_position(self, exchange, num, objekt):
    #     if self.scores_dict[num].get(exchange) < 0:
    #         objekt.futures_market(
    #             self.params.get(f'{exchange.lower()}_side_{num}'),
    #             self.params.get(f'{exchange.lower()}_qty_{num}') * abs(self.scores_dict[num].get(exchange))
    #         )
    #     else:
    #         objekt.futures_market(
    #             'BUY' if self.params.get(f'{exchange.lower()}_side_{num}') == 'SELL' else 'SELL',
    #             self.params.get(f'{exchange.lower()}_qty_{num}') * abs(self.scores_dict[num].get(exchange))
    #         )

    def open_position(self, exchange, num, objekt):
        try:
            if self.scores_dict[num].get(exchange) > 0:
                objekt.futures_market(
                    self.params.get(f'{exchange.lower()}_side_{num}'),
                    self.params.get(f'{exchange.lower()}_qty_{num}') * self.scores_dict[num].get(exchange)
                )
            else:
                objekt.futures_market(
                    'BUY' if self.params.get(f'{exchange.lower()}_side_{num}') == 'SELL' else 'SELL',
                    self.params.get(f'{exchange.lower()}_qty_{num}') * abs(self.scores_dict[num].get(exchange))
                )
        except Exception as er:
            logging.error(er)

    def get_while_command_all(self):
        while True:
            try:
                with open('Exchanges/run.json', 'r') as file:
                    run_data = json.load(file)
                if run_data['close_all']:
                    return True
                else:
                    return False
            except:
                pass

    def get_while_command(self):
        while True:
            try:
                with open('Exchanges/run.json', 'r') as file:
                    run_data = json.load(file)
                if run_data['stop']:
                    return True
                else:
                    return False
            except:
                pass

    def get_websocket_command(self):
        while True:
            try:
                with open('Exchanges/run.json', 'r') as file:
                    run_data = json.load(file)
                if run_data['websocket']:
                    return True
                else:
                    return False
            except:
                pass

    def create_rest_binance(self, num: str, params: dict, apis: dict):
        connect = Binance_rest(
            params.get(f'binance_symbol_{num}'),
            apis.get('Binance'),
        )
        return connect

    def create_rest_bybit(self, num: str, params: dict, apis: dict):
        connect = Bybit_rest(
            params.get(f'bybit_symbol_{num}'),
            apis.get('Bybit'),
        )
        return connect

    def create_rest_kucoin(self, num: str, params: dict, apis: dict):
        connect = Kucoin_rest(
            params.get(f'kucoin_symbol_{num}'),
            apis.get('Kucoin'),
        )
        return connect

    def create_rest_huobi(self, num: str, params: dict, apis: dict):
        connect = Huobi_rest(
            params.get(f'huobi_symbol_{num}'),
            apis.get('Huobi'),
        )
        return connect

