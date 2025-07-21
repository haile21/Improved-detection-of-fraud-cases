import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def ip_to_int(ip):
    try:
        return int(''.join([f"{int(i):02x}" for i in str(ip).split('.')]), 16)
    except:
        return np.nan

def load_and_preprocess_fraud_data():
    df = pd.read_csv("../../data/Fraud_Data.csv")

    print("Columns in Fraud_Data.csv:", df.columns.tolist())

    # Rename the label column to 'fraud' if needed
    if 'class' in df.columns:
        df.rename(columns={'class': 'fraud'}, inplace=True)

    # IP to integer
    df['ip_address'] = df['ip_address'].apply(ip_to_int)
    df.dropna(subset=['ip_address'], inplace=True)
    df['ip_address'] = df['ip_address'].astype(int)

    # Time processing
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    df['hour'] = df['purchase_time'].dt.hour.astype('category')
    df['day_of_week'] = df['purchase_time'].dt.dayofweek.astype('category')
    df['time_since_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()
    df.drop(['signup_time', 'purchase_time'], axis=1, inplace=True)

    # Encode categories
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))

    # Split features/target
    X = df.drop("fraud", axis=1)
    y = df["fraud"]

    # Normalize
    scaler = StandardScaler()
    X[X.columns] = scaler.fit_transform(X)

    return train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

