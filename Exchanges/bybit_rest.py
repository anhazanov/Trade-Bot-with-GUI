import logging

from pybit import usdt_perpetual, exceptions

logging.basicConfig(filename='loging.log', level=logging.ERROR)

class Bybit_rest:
    def __init__(self, symbol: str, apis: dict):
        self.symbol = symbol
        self.session = usdt_perpetual.HTTP(
            endpoint='https://api.bybit.com',
            api_key=apis.get('api_key'),
            api_secret=apis.get('api_secret')
        )

    def get_max_leverage(self) -> int:
        try:
            info = self.session.get_risk_limit(symbol=f'{self.symbol.upper()}USDT')
            return info['result'][0].get('max_leverage')
        except exceptions.InvalidRequestError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.status_code, error.message.capitalize()
                )
            )

    def set_max_leverage(self) -> None:
        self.max_leverage = self.get_max_leverage()
        try:
            self.session.set_leverage(symbol=f'{self.symbol.upper()}USDT', buy_leverage=self.max_leverage,
                                      sell_leverage=self.max_leverage)
            print('Bybit: Set leverage - ', self.max_leverage)
        except exceptions.InvalidRequestError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.status_code, error.message.capitalize()
                )
            )


    def futures_market(self, side, quantity, reduce=False) -> str:
        if type(quantity) == str and ',' in quantity:
            quantity = quantity.replace(',', '.')
        # New order
        flag = True
        while flag:
            try:
                response = self.session.place_active_order(
                    symbol=f"{self.symbol.upper()}USDT",
                    side=side.capitalize(),
                    order_type="Market",
                    qty=abs(float(quantity)),
                    time_in_force="GoodTillCancel",
                    reduce_only=reduce,
                    close_on_trigger=False
                )
                flag = False
                logging.info(response)
            except exceptions.InvalidRequestError as error:
                logging.error(
                    "Found error. status: {}, error code: {}, error message: {}".format(
                        error.status_code, error.status_code, error.message
                    )
                )
                response = {}
            finally:
                print('Bybit -- ', response)
                if type(response) == dict and response.get('ret_msg') == 'OK' and response.get('result'):
                    flag = False
                    break
                else:
                    continue

    def get_balance(self):
        flag = True
        while flag:
            try:
                resp = self.session.get_wallet_balance()
                flag = False
                return resp['result']['USDT'].get('equity')
            except Exception as er:
                logging.error(er)
                continue

    def get_open_positions(self):
        flag = True
        while flag:
            try:
                resp = self.session.my_position()
                answer = {}
                for el in resp.get('result'):
                    if el['data'].get('size') != 0 and self.symbol in el["data"].get("symbol"):
                        answer = {
                            'symbol': el["data"].get("symbol"),
                            'side': el["data"].get("side"),
                            'qty': el["data"].get("size"),
                            'profit': el["data"].get("cum_realised_pnl")
                        }
                flag = False
                return answer
            except Exception as er:
                logging.error(er)
                continue