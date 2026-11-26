import pandas as pd


def first_look(df):
    out = pd.DataFrame({
        'column' : df.columns.tolist(),
        'dtype' : df.dtypes.astype(str).tolist(),
        'missing' : df.isna().sum(),
        'unique' : df.nunique()
    })
    return df.shape, out
