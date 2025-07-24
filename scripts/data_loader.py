import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

def load_fraud_data():
    return pd.read_csv(os.path.join(DATA_DIR, "Fraud_Data.csv"))

def load_ip_country_data():
    return pd.read_csv(os.path.join(DATA_DIR, "IpAddress_to_Country.csv"))

def load_credit_card_data():
    return pd.read_csv(os.path.join(DATA_DIR, "creditcard.csv"))
