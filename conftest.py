import pytest
from linear_arbitrage.data_structure_ccxt import ResponseApiCcxt, InfoFromResponseApiCcxt

response_api_from_cctx_1 = {'ask': 31.11,
                            'askVolume': 1.87,
                            'average': 29.81,
                            'baseVolume': 16151.75,
                            'bid': 31.04,
                            'bidVolume': 46.59,
                            'change': 2.46,
                            'close': 31.04,
                            'datetime': '2022-03-09T20:12:59.838Z',
                            'high': 31.24,
                            'info': {'askPrice': '31.11000000',
                                     'askQty': '1.87000000',
                                     'bidPrice': '31.04000000',
                                     'bidQty': '46.59000000',
                                     'closeTime': '1646856779838',
                                     'count': '4616',
                                     'firstId': '3994498',
                                     'highPrice': '31.24000000',
                                     'lastId': '3999113',
                                     'lastPrice': '31.04000000',
                                     'lastQty': '28.45000000',
                                     'lowPrice': '28.38000000',
                                     'openPrice': '28.58000000',
                                     'openTime': '1646770379838',
                                     'prevClosePrice': '28.61000000',
                                     'priceChange': '2.46000000',
                                     'priceChangePercent': '8.607',
                                     'quoteVolume': '486467.52730000',
                                     'symbol': 'BTGUSDT',
                                     'volume': '16151.75000000',
                                     'weightedAvgPrice': '30.11856469'},
                            'last': 31.04,
                            'low': 28.38,
                            'open': 28.58,
                            'percentage': 8.607,
                            'previousClose': '28.61000000',
                            'quoteVolume': 486467.5273,
                            'symbol': 'BTG/USDT',
                            'timestamp': 1646856779838,
                            'vwap': 30.11856469}

response_api_from_cctx_2 = {'ask': 31.11,
                            'askVolume': 1.87,
                            'average': 29.81,
                            'baseVolume': 16151.75,
                            'bid': 31.04,
                            'bidVolume': 46.59,
                            'change': 2.46,
                            'close': 33.04,
                            'datetime': '2022-03-09T20:12:59.838Z',
                            'high': 31.24,
                            'info': {'askPrice': '31.11000000',
                                     'askQty': '1.87000000',
                                     'bidPrice': '31.04000000',
                                     'bidQty': '46.59000000',
                                     'closeTime': '1646856779838',
                                     'count': '4616',
                                     'firstId': '3994498',
                                     'highPrice': '31.24000000',
                                     'lastId': '3999113',
                                     'lastPrice': '31.04000000',
                                     'lastQty': '28.45000000',
                                     'lowPrice': '28.38000000',
                                     'openPrice': '28.58000000',
                                     'openTime': '1646770379838',
                                     'prevClosePrice': '28.61000000',
                                     'priceChange': '2.46000000',
                                     'priceChangePercent': '8.607',
                                     'quoteVolume': '486467.52730000',
                                     'symbol': 'BTGUSDT',
                                     'volume': '16151.75000000',
                                     'weightedAvgPrice': '30.11856469'},
                            'last': 31.04,
                            'low': 28.38,
                            'open': 28.58,
                            'percentage': 8.607,
                            'previousClose': '28.61000000',
                            'quoteVolume': 486467.5273,
                            'symbol': 'BTG/USDT',
                            'timestamp': 1646856779838,
                            'vwap': 30.11856469}


@pytest.fixture
def fixture_response_api_from_cctx_1():
    return response_api_from_cctx_1


@pytest.fixture
def fixture_response_api_from_cctx_2():
    return response_api_from_cctx_2


@pytest.fixture
def fixture_datastrure_response_api_from_cctx_1():
    return ResponseApiCcxt(exchange_id="binance", **response_api_from_cctx_1)


@pytest.fixture
def fixture_datastrure_response_api_from_cctx_2():
    return ResponseApiCcxt(exchange_id="okex", **response_api_from_cctx_2)


@pytest.fixture
def list_of_exchange():
    return ["binance", "okex"]


@pytest.fixture
def symbols():
    return ["BTG/USDT"]
