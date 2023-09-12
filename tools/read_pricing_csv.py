import pandas as pd

from config.paths import PRICING_DF

def read_pricing_df():
    return pd.read_csv(PRICING_DF)