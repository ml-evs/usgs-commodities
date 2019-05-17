""" This module creates a pandas dataframe containing the USGS
data from this repository, currently only for the example of
lithium.

"""

import pathlib
import pandas as pd

DATA_PATH = pathlib.Path(__file__).parents[1].joinpath('data')

def scrape_data():

    data = {}
    data['lithium'] = pd.read_csv(DATA_PATH.joinpath('lithium/lithium_summary.csv'))

    return data
