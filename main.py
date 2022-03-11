from linear_arbitrage import vanilla_arbitrage

list_of_exchange = ["binance", "okex"]
symbols = ["BTG/USDT"]

if __name__ == "__main__":
    obj_lineare_arbitrage = vanilla_arbitrage.LinearModelArbitrage(list_of_exchange, symbols)
    print(obj_lineare_arbitrage)
    print(obj_lineare_arbitrage.compute_opportunity())

