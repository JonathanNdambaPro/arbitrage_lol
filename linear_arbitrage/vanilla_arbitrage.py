import concurrent.futures
import typing as t
from pathlib import Path
import ccxt
import yaml
from linear_arbitrage.data_structure_ccxt import ResponseApiCcxt
import logging

path_pwd = Path(".").resolve()
PATH_TO_FOLDER = path_pwd / "config.yml"

with open(PATH_TO_FOLDER) as file:
    CONFIG_YAML = yaml.load(file, Loader=yaml.FullLoader)


class LinearModelArbitrage:
    """
    Class define for vanilla arbitrage with the lib ccxt between exchange and


    Attributes
    ----------
    list_of_exchanges: List[str]|Tuple[str]
        List of all exchanges we want to detect arbitrage
    symbols: List[str]|Tuple[str]
        List of all symbols we want to detect arbitrage

    Methods
    -------
    compute_opportunity()
        compute all opportunities for exchange and return list of dictionaries (target min 1%)
    """
    def __init__(self, list_of_exchanges: t.List[str] | t.Tuple[str], symbols: t.List[str] | t.Tuple[str]) -> None:
        """
        Parameters
        ----------
        list_of_exchanges: List[str]|Tuple[str]
            List of all exchanges we want to detect arbitrage
        symbols: List[str]|Tuple[str]
            List of all symbols we want to detect arbitrage

        """
        if not isinstance(list_of_exchanges, t.List | t.Tuple):
            message = "The list of exchanges as to be a sequence"
            logging.error(message)
            raise TypeError(message)

        elif not isinstance(symbols, t.List | t.Tuple):
            message = "symbols as to be a list or tuple"
            logging.error(message)
            raise TypeError(message)

        else:
            self._exchange_id = list_of_exchanges
            self._exchanges = {}
            self._symbols = symbols

            for exchange_id in self._exchange_id:
                exchange_class = getattr(ccxt, exchange_id)
                self._exchanges[exchange_id] = exchange_class({
                    **CONFIG_YAML[f"conf_{exchange_id}"],
                    "enableRateLimit": True,
                })

                self._exchanges[exchange_id].load_markets()

    def __repr__(self):
        return f"List of exchange : {self.exchange_ids} \n" \
               f"List of cypto : {self.symbols}"

    @property
    def exchange_ids(self) -> t.List[str] | t.Tuple[str]:
        return self._exchange_id

    @property
    def exchanges(self) -> t.Dict:
        return self._exchanges

    @property
    def symbols(self) -> t.List[str] | t.Tuple[str]:
        return self._symbols

    def _call_api(self, exchange_id: str, symbol: str) -> ResponseApiCcxt:
        """
        call the api ccxt for specific exchange and symbol

        Parameters
        ----------
        exchange_id: str
            name of the exchange for the call
        symbol: str
            symbol which we want trade (ex : BTC/USDT)

        Returns
        -------
        ResponseApiCcxt
            reformation of the response with the dataclass ResponseApiCcxt for ease use
        """
        return ResponseApiCcxt(exchange_id=exchange_id, **self._exchanges[exchange_id].fetch_ticker(symbol))

    def _multiple_call_concurrency(self) -> t.List[ResponseApiCcxt]:
        """
        multi call with concurrency/multithread for specific symbal

        Returns
        -------
        List[ResponseApiCcxt]
            List of all response from api ccxt requested in concurrency
        """
        responses = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for exchange_id in self.exchange_ids:
                for symbol in self.symbols:
                    futures.append(executor.submit(self._call_api, exchange_id=exchange_id, symbol=symbol))
            for future in concurrent.futures.as_completed(futures):
                responses.append(future.result())
        return responses

    def compute_opportunity(self) -> t.List[t.Dict]:
        """
        Compute all opportunities and the pourcentage of rentability

        Returns
        -------
        List[Dict]:
            pourcentage opportunity computed for each pair of exchanges by symbol
            with all information
        """
        response_api_for_symbol = self._multiple_call_concurrency()

        consult = []
        global_arbitrage = []
        for element_1 in response_api_for_symbol:
            consult.append(element_1.exchange_id)
            for element_2 in response_api_for_symbol:
                condition_exchange = (element_1.exchange_id == element_2.exchange_id)
                condition_symbol = (element_1.symbol == element_2.symbol)
                if condition_exchange:
                    continue
                elif element_2.exchange_id in consult:
                    continue
                elif not condition_symbol:
                    continue
                else:
                    result = {"percentage": abs(1 - element_1.close / element_2.close)*100, "symbol": element_1.symbol,
                              "exchange_1": element_1.exchange_id, "exchange_2": element_2.exchange_id}
                global_arbitrage.append(result)

        return global_arbitrage
