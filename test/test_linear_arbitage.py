from linear_arbitrage import vanilla_arbitrage
import pytest


def test_initialisation(list_of_exchange, symbols):
    obj_lineare_arbitrage = vanilla_arbitrage.LinearModelArbitrage(list_of_exchange, symbols)
    assert str(obj_lineare_arbitrage) == f"List of exchange : {list_of_exchange} \n" \
                                         f"List of cypto : {symbols}"


@pytest.mark.parametrize("exchanges, symbols",
                         [(['lol_exchange_1', 'lol_exchange_2'], "lol_symbol_1"), ('lol_exchange_1', ["lol_symbol_1"])])
def test_initialisation_fail(exchanges, symbols):
    with pytest.raises(TypeError):
        vanilla_arbitrage.LinearModelArbitrage(exchanges, symbols)


def test_compute_opportunity_diff(list_of_exchange, symbols, mocker,
                                  fixture_datastrure_response_api_from_cctx_1,
                                  fixture_datastrure_response_api_from_cctx_2):
    mocker.patch('linear_arbitrage.vanilla_arbitrage.LinearModelArbitrage._call_api', return_value=None)
    mocker.patch('linear_arbitrage.vanilla_arbitrage.LinearModelArbitrage._multiple_call_concurrency',
                 return_value=[fixture_datastrure_response_api_from_cctx_1,
                               fixture_datastrure_response_api_from_cctx_2])
    obj_lineare_arbitrage = vanilla_arbitrage.LinearModelArbitrage(list_of_exchange, symbols)
    list_output = obj_lineare_arbitrage.compute_opportunity()
    for dict_output in list_output:
        assert dict_output["percentage"] > 0
        assert dict_output["symbol"] == "BTG/USDT"
        assert dict_output["exchange_1"] == "binance"
        assert dict_output["exchange_2"] == "okex"
