def handle_missing_values(df):
    missing_ratio = df.isnull().mean()
    to_drop = missing_ratio[missing_ratio > 0.5].index
    df.drop(columns=to_drop, inplace=True)
    df.dropna(inplace=True)  # For small missing ratios
    return df