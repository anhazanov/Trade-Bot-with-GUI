import logging, time

from kucoin_futures.client import Trade, MarketData, User, Market

logging.basicConfig(filename='loging.log', level=logging.ERROR)


class Kucoin_rest:
    def __init__(self, symbol: str, apis: dict):
        self.symbol = 'XBT' if symbol.upper() == 'BTC' else symbol
        self.trade = Trade(key=apis.get('api_key'), secret=apis.get('api_secret'), passphrase=apis.get('api_passphrase'),
                      is_sandbox=False, url='https://api-futures.kucoin.com')
        self.user = User(key=apis.get('api_key'), secret=apis.get('api_secret'), passphrase=apis.get('api_passphrase'),
                      is_sandbox=False, url='https://api-futures.kucoin.com')
        self.market = Market()
        self.max_leverage = self._get_max_leverage()
        self.min_size = self.get_min_size()

    def _get_max_leverage(self) -> int:
        try:
            info = self.trade.get_contracts_risk_limit(f'{self.symbol.upper()}USDTM')
            return info[0].get('maxLeverage')
        except Exception as error:
            logging.error(
                "Found error. error message: {}".format(error)
            )

    def get_min_size(self) -> float:
        market_data = MarketData()
        responce = market_data.get_contract_detail(f'{self.symbol.upper()}USDTM')
        return float(responce['multiplier'])

    def get_price(self):
        resp = self.market.get_ticker(f'{self.symbol.upper()}USDTM')
        return float(resp.get('price'))

    def futures_market(self, side, quantity):
        if type(quantity) == str and ',' in quantity:
            quantity = quantity.replace(',', '.')
        flag = True
        while flag:
            try:
                response = self.trade.create_market_order(f'{self.symbol.upper()}USDTM', side.lower(), self.max_leverage,
                                                     size=abs(int(float(quantity) / self.min_size)))
                logging.info(response)
            except Exception as er:
                print(er)
                logging.error("Found error. error message: {}".format(er))
                response = {}
            finally:
                print('Kucoin -- ', response)
                if type(response) == dict and response.get('orderId'):
                    flag = False
                    break
                else:
                    continue

    def get_balance(self):
        flag = True
        while flag:
            try:
                resp = self.user.get_account_overview('USDT')
                flag = False
                return resp.get('accountEquity')
            except Exception as er:
                logging.error(er)
                continue

    def get_open_positions(self):
        flag = True
        while flag:
            try:
                resp = self.trade.get_all_position()
                answer = {}
                if type(resp) == dict and resp.get('data'):
                    return answer
                elif type(resp) == list and resp[0]:
                    for el in resp:
                        if self.symbol in el.get("symbol"):
                            answer = {
                                'symbol': el.get("symbol"),
                                'side': "SELL" if el.get("currentQty") < 0 else "BUY",
                                'qty': abs(el.get("currentQty")) * self.min_size,
                                'profit': el.get("unrealisedPnl")
                            }
                    return answer
                else:
                    return answer
            except Exception as er:
                logging.error(er)
                continue