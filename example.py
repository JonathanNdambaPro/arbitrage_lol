from linear_arbitrage import vanilla_arbitrage
from pathlib import Path
import yaml
from pprint import pprint
PATH_TO_FOLDER = Path(".").resolve() / "config.yml"

with open(PATH_TO_FOLDER) as file:
    CONFIG_YAML = yaml.load(file, Loader=yaml.FullLoader)
ITERATION = 10000

list_of_exchange = CONFIG_YAML["list_of_exchange"]
symbols = CONFIG_YAML["symbols"]

if __name__ == "__main__":
    cmp = 0
    for _ in range(ITERATION):
        obj_arbitrage = vanilla_arbitrage.LinearModelArbitrage(list_of_exchange, symbols)
        response = obj_arbitrage.compute_opportunity()
        pprint(response)
        cmp += 1

