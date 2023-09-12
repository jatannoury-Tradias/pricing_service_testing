import os
from os.path import join as join_path

MAIN_PATH = join_path(os.path.dirname(__file__), '..\\')
CONFIG_PATH = join_path(MAIN_PATH, 'config')
PRICE_PRECISION_PATH = join_path(CONFIG_PATH,"price_precision.csv")
PRICING_DF = join_path(CONFIG_PATH,"pricing_df.csv")