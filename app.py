from linear_arbitrage import vanilla_arbitrage
from pathlib import Path
import yaml
import plotly.express as px
import pandas as pd
import streamlit as st

PATH_TO_FOLDER = Path(".").resolve() / "config.yml"

with open(PATH_TO_FOLDER) as file:
    CONFIG_YAML = yaml.load(file, Loader=yaml.FullLoader)

list_of_exchange = CONFIG_YAML["list_of_exchange"]
symbols = CONFIG_YAML["symbols"]

if __name__ == "__main__":
    cmp = 0
    st.title("Plotly Graphs with containers")
    plot_spot = st.empty()
    while True:
        dataframe_for_dashboard = pd.DataFrame()
        while cmp < 1000000:
            obj_arbitrage = vanilla_arbitrage.LinearModelArbitrage(list_of_exchange, symbols)
            response = obj_arbitrage.compute_opportunity()
            dataframe_for_dashboard = pd.concat([dataframe_for_dashboard, pd.DataFrame(response)], ignore_index=True)
            dataframe_for_dashboard["info"] = (
                dataframe_for_dashboard.exchange_1
                + "/"
                + dataframe_for_dashboard.exchange_2
                + " "
                + dataframe_for_dashboard.symbol
            )
            fig = px.line(dataframe_for_dashboard.drop_duplicates(), x="date", y="percentage", color="info")
            with plot_spot:
                st.plotly_chart(fig)
            cmp = dataframe_for_dashboard.drop_duplicates().shape[0]
