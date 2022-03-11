from dataclasses import dataclass
import datetime
import typing as t


@dataclass
class InfoFromResponseApiCcxt:
    askPrice: float
    askQty: float
    bidPrice: float
    bidQty: float
    closeTime: float
    count: float
    firstId: float
    highPrice: float
    lastId: float
    lastPrice: float
    lastQty: float
    lowPrice: float
    openPrice: float
    openTime: float
    prevClosePrice: float
    priceChange: float
    priceChangePercent: float
    quoteVolume: float
    symbol: str
    volume: float
    weightedAvgPrice: float


@dataclass
class ResponseApiCcxt:
    exchange_id: str
    ask: float
    askVolume: float
    average: float
    baseVolume: float
    bid: float
    bidVolume: float
    change: float
    close: float
    datetime: t.Union[str, datetime.datetime]
    high: float
    info: InfoFromResponseApiCcxt
    last: float
    low: float
    open: float
    percentage: float
    previousClose: float
    quoteVolume: float
    symbol: float
    timestamp: float
    vwap: float
