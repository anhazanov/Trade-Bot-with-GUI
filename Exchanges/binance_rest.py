import logging

from binance.um_futures import UMFutures
from binance.error import ClientError

logging.basicConfig(filename='loging.log', level=logging.ERROR)


class Binance_rest:
    def __init__(self, symbol, apis):
        self.symbol = symbol
        self.apis = apis
        self.connect = UMFutures(key=self.apis.get('api_key'), secret=self.apis.get('api_secret'))
        self.min_size = self.get_min_size()


    def get_min_size(self):
        resp = self.connect.exchange_info()
        for el in resp['symbols']:
            if el.get('symbol') == f'{self.symbol.upper()}USDT':
                return el['filters'][1].get('minQty')

    def _get_max_leverage(self) -> int:
        try:
            info = self.connect.leverage_brackets(symbol=f'{self.symbol}USDT')
            return info[0]['brackets'][0].get('initialLeverage')
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
            return error.error_message

    def set_max_leverage(self) -> None:
        self.max_leverage = self._get_max_leverage()
        try:
            self.connect.change_leverage(f'{self.symbol}USDT', self.max_leverage)
            print('Set leverage - ', self.max_leverage)
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
            try:
                self.max_leverage = str(error).split('more than')[1][1:4].strip(' ').strip('x')
                self.connect.change_leverage(f'{self.symbol}USDT', self.max_leverage)
                print('Set leverage - ', self.max_leverage)
            except:
                pass

    def futures_market(self, side, quantity) -> str:
        if type(quantity) == str and ',' in quantity:
            quantity = quantity.replace(',', '.')
        quantity = round(float(quantity), len(str(float(self.min_size)).split('.')[-1]) if '.' in str(self.min_size) else 0)
        # New order
        flag = True
        while flag:
            try:
                response = self.connect.new_order(
                    symbol=f"{self.symbol}USDT",
                    side=side.upper(),
                    type="MARKET",
                    quantity=abs(quantity),
                )
                logging.info(response)
            except ClientError as error:
                logging.error(
                    "Found error. status: {}, error code: {}, error message: {}".format(
                        error.status_code, error.error_code, error.error_message
                    )
                )
                response = {}
            finally:
                print('Binance -- ', response)
                if type(response) == dict and response.get('symbol') == f"{self.symbol}USDT" and response.get('status') == "NEW":
                    flag = False
                    break
                else:
                    continue

    def get_price(self):
        resp = self.connect.ticker_price(f'{self.symbol.upper()}USDT')
        return float(resp.get('price'))

    def get_balance(self):
        flag = True
        while flag:
            try:
                resp = self.connect.balance()
                for el in resp:
                    if el.get('asset') == 'USDT':
                        flag = False
                        return float(el.get('crossWalletBalance')) + float(el.get('crossUnPnl'))
            except Exception as er:
                logging.error(er)
                continue

    def get_open_positions(self):
        flag = True
        while flag:
            try:
                resp = self.connect.get_position_risk()
                answer = {}
                for el in resp:
                    if float(el.get('positionAmt')) != 0 and self.symbol in el.get("symbol"):
                        answer = {
                            'symbol': el.get("symbol"),
                            'side': "SELL" if "-" in el.get("positionAmt") else "BUY",
                            'qty': el.get("positionAmt"),
                            'profit': el.get("unRealizedProfit")
                        }
                flag = False
                return answer
            except Exception as er:
                logging.error(er)
                continue
