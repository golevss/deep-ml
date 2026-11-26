import pandas as pd


def select_orders(df, countries, low, high):
    true_countries = df["country"].isin(countries)
    true_amount = df["amount"].between(low, high)
    true = true_countries & (true_amount | df["vip"])

    return df[true].drop(columns=['vip'])
