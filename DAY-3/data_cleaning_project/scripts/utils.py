"""utils.py - small helper utilities for the data cleaning project"""
import pandas as pd

def save_df(df, path):
    df.to_csv(path, index=False)

def load_df(path):
    return pd.read_csv(path)
