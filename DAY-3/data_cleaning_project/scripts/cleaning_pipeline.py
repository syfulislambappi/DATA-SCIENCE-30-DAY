"""cleaning_pipeline.py
Reusable functions to run the text/data cleaning pipeline from scripts.
"""
import pandas as pd
import numpy as np

def load_data(path):
    return pd.read_csv(path)

def basic_profile(df):
    return {
        'shape': df.shape,
        'dtypes': df.dtypes.to_dict(),
        'missing': df.isna().sum().to_dict()
    }

def normalize_text(df, cols=None):
    if cols is None:
        cols = df.select_dtypes(include='object').columns.tolist()
    for c in cols:
        df[c] = df[c].astype(str).str.strip()
    return df

def parse_dates(df, date_cols):
    for c in date_cols:
        df[c] = pd.to_datetime(df[c], errors='coerce')
    return df

def to_numeric(df, cols):
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df

def impute_median(df, cols):
    for c in cols:
        df[c] = df[c].fillna(df[c].median())
    return df

def deduplicate_by(df, key, sort_col=None):
    if sort_col:
        df = df.sort_values(sort_col).drop_duplicates(subset=key, keep='last')
    else:
        df = df.drop_duplicates(subset=key)
    return df
