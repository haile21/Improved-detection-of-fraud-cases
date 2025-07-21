import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_creditcard_data(path='data/creditcard.csv'):
    df = pd.read_csv(path)

    # Drop 'Time' column
    df = df.drop(columns=['Time'])

    X = df.drop('Class', axis=1)
    y = df['Class']

    # Scale 'Amount'
    scaler = StandardScaler()
    X['Amount'] = scaler.fit_transform(X[['Amount']])

    return train_test_split(X, y, test_size=0.2, random_state=42)
