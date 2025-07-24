# import sys
# import os
#
# # Add the project root to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from scripts.preprocessing.fraud_data import load_and_preprocess_fraud_data
# from scripts.preprocessing.ecommerce_data import load_and_preprocess_ecommerce_data
# from scripts.preprocessing.creditcard_data import load_and_preprocess_creditcard_data
#
# def run_task_1():
#     print("\n🔹 Loading and preprocessing Fraud_Data.csv...")
#     X_train1, X_test1, y_train1, y_test1 = load_and_preprocess_fraud_data()
#
#     print("\n🔹 Loading and preprocessing ecommerce_data.csv...")
#     X_train2, X_test2, y_train2, y_test2 = load_and_preprocess_ecommerce_data()
#
#     print("\n🔹 Loading and preprocessing creditcard.csv...")
#     X_train3, X_test3, y_train3, y_test3 = load_and_preprocess_creditcard_data()
#
#     print("\n✅ All datasets preprocessed successfully.")
#     print(f"Fraud_Data split: {X_train1.shape}, {X_test1.shape}")
#     print(f"Ecommerce split: {X_train2.shape}, {X_test2.shape}")
#     print(f"CreditCard split: {X_train3.shape}, {X_test3.shape}")
#
# if __name__ == "__main__":
#     run_task_1()
