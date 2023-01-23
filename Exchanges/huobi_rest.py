import logging

from huobi.linear_swap.rest.account import Account
from huobi.linear_swap.rest.order import Order
from huobi.linear_swap.rest.market import Market

logging.basicConfig(filename='loging.log', level=logging.ERROR)


class Huobi_rest:
    def __init__(self, symbol: str, apis: dict):
        self.symbol = symbol
        self.client = Account(apis.get('api_key'), apis.get('api_secret'))
        self.order = Order(apis.get('api_key'), apis.get('api_secret'))

        self.max_leverage = self.get_max_leverage()
        self.market = Market()
        self.min_size = self.get_min_size()

    def get_max_leverage(self) -> int:
        try:
            info = self.client.cross_get_available_level_rate({'contract_code': f'{self.symbol.upper()}-USDT'})
            max_leverage = info['data'][0]['available_level_rate'].split(',')[-1]
            return max_leverage
        except Exception as error:
            logging.error(
                "Found error. error message: {}".format(error)
            )


    def set_max_leverage(self) -> None:
        try:
            resp = self.order.cross_switch_lever_rate({
                'contract_code': f'{self.symbol.upper()}-USDT'.lower(),
                'lever_rate': self.max_leverage
            })
            print('Huobi: Set leverage - ', self.max_leverage)
        except Exception as error:
            logging.error(
                "Found error. error message: {}".format(error)
            )


    def get_min_size(self) -> float:
        try:
            info = self.market.get_contract_info({
                    'contract_code': f'{self.symbol.upper()}-USDT'.lower(),
                })
            return info['data'][0].get('contract_size')
        except Exception as error:
            logging.error(
                "Found error. error message: {}".format(error)
            )
            return error

    def futures_market(self, side: str, quantity) -> str:
        # Get minimum order size
        if type(self.min_size) == KeyError:
            return f'Huobi: invalid input {self.min_size}'

        if type(quantity) == str and ',' in quantity:
            quantity = quantity.replace(',', '.')
        flag = True
        while flag:
            try:
                response = self.order.cross_order(
                    {
                        'contract_code': f'{self.symbol.upper()}-USDT'.lower(),
                        'volume': abs(int(float(quantity) / self.min_size)),
                        'direction': side.lower(),
                        'lever_rate': self.max_leverage,
                        'order_price_type': 'opponent',
                        # 'price': 19500.00
                }
                )
                logging.info(response)
            except Exception as error:
                print('ERROR???', error)
                logging.error(
                    "Found error. error message: {}".format(error)
                )
                response = {}
            finally:
                print('Huobi -- ', response)
                if type(response) == dict and response.get('status') == 'ok' and response.get('data'):
                    flag = False
                    break
                else:
                    continue

    def get_balance(self):
        flag = True
        while flag:
            try:
                resp = self.client.get_balance_valuation({'valuation_asset': 'USDT'})
                flag = False
                return float(resp['data'][0].get('balance'))
            except Exception as er:
                logging.error(er)
                continue

    def get_open_positions(self):
        resp = self.client.cross_get_position_info()
        answer = {}
        flag = True
        while flag:
            try:
                for el in resp['data']:
                    if self.symbol in el.get("contract_code").replace("-", ""):
                        answer = {
                            'symbol': el.get("contract_code").replace("-", ""),
                            'side': el.get("direction").upper(),
                            'qty': el.get("volume") * self.min_size,
                            'profit': el.get("profit_unreal")
                        }
                flag = False
                return answer
            except Exception as er:
                logging.error(er)
                continue
