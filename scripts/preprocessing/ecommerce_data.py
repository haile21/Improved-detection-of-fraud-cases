import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_ecommerce_data(path='data/ecommerce_data.csv'):
    df = pd.read_csv(path)

    # Drop missing values
    df.dropna(inplace=True)

    # Drop irrelevant columns
    df = df.drop(columns=['user_id'])

    X = df.drop('is_fraud', axis=1)
    y = df['is_fraud']

    # One-hot encode categorical columns
    X = pd.get_dummies(X, drop_first=True)

    # Scale numeric features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)
