from config.paths import PRICE_PRECISION_PATH
import pandas as pd

def get_price_precisions():
    return pd.read_csv(PRICE_PRECISION_PATH)