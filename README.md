# Improved Detection of Fraud Cases for E-Commerce and Bank Transactions

## Business Need

As a data scientist at Adey Innovations Inc., a leader in the financial technology sector, the focus is on enhancing the detection of fraud cases in e-commerce and banking transactions. This project aims to create accurate fraud detection models that address the unique challenges associated with both transaction types. By leveraging advanced machine learning techniques, geolocation analysis, and transaction pattern recognition, the goal is to improve transaction security, prevent financial losses, and foster trust with customers and financial institutions.

## Project Overview

The project will span two weeks and offers flexibility for those wishing to engage with new material or catch up on previous challenges. Key components include:

- Analyzing and preprocessing transaction data.
- Engineering features to identify fraud patterns.
- Building and training machine learning models.
- Evaluating model performance and making selections based on justification.
- Interpreting model decisions using modern explainability techniques.

## Data and Features

### Datasets

1. **Fraud_Data.csv**
   - Contains e-commerce transaction data.
   - Features:
     - `user_id`: Unique identifier for the user.
     - `signup_time`: Timestamp of user signup.
     - `purchase_time`: Timestamp of purchase.
     - `purchase_value`: Value of the purchase.
     - `device_id`: Unique identifier for the device.
     - `source`: Source through which the user accessed the site.
     - `browser`: Browser used for the transaction.
     - `sex`: Gender of the user (M/F).
     - `age`: Age of the user.
     - `ip_address`: IP address of the transaction.
     - `class`: Target variable (1 for fraudulent, 0 for non-fraudulent).

2. **IpAddress_to_Country.csv**
   - Maps IP addresses to countries.
   - Features:
     - `lower_bound_ip_address`: Lower bound of the IP address range.
     - `upper_bound_ip_address`: Upper bound of the IP address range.
     - `country`: Corresponding country.

3. **creditcard.csv**
   - Contains bank transaction data.
   - Features:
     - `Time`: Seconds since the first transaction.
     - `V1 to V28`: Anonymized features from PCA transformation.
     - `Amount`: Transaction amount.
     - `Class`: Target variable (1 for fraudulent, 0 for non-fraudulent).

### Critical Challenge

Both datasets exhibit class imbalance, with significantly fewer fraudulent transactions than legitimate ones. This imbalance will influence the choice of evaluation metrics and modeling techniques.

## Learning Outcomes

### Skills
- Clean, preprocess, and merge complex datasets.
- Engineer meaningful features from raw data.
- Implement techniques for handling highly imbalanced datasets.
- Train and evaluate models using appropriate metrics for imbalanced classification (e.g., AUC-PR, F1-Score).
- Visualize model predictions using explainability tools like SHAP.

### Knowledge
- Understand the business and technical challenges of fraud detection.
- Grasp the importance of model explainability (XAI) for building trust and deriving insights.
- Justify model selection based on performance metrics and business context.

### Behaviors
- Adopt a business-centric approach to problem-solving.
- Demonstrate a systematic workflow from data analysis to final interpretation.

### Communication
- Report on statistically complex issues clearly and effectively.

## Project Tasks

### Task 1 - Data Analysis and Preprocessing
- **Handle Missing Values**: Impute or drop missing values.
- **Data Cleaning**: Remove duplicates and correct data types.
- **Exploratory Data Analysis (EDA)**: Conduct univariate and bivariate analyses.
- **Merge Datasets for Geolocation Analysis**: Convert IP addresses to integer format and merge datasets.
- **Feature Engineering**: 
  - Analyze transaction frequency and velocity.
  - Create time-based features (`hour_of_day`, `day_of_week`, `time_since_signup`).
- **Data Transformation**:
  - Handle class imbalance using sampling techniques (e.g., SMOTE, Random Undersampling).
  - Normalize and scale data.
  - Encode categorical features (e.g., One-Hot Encoding).

### Task 2 - Model Building and Training
- **Data Preparation**: Separate features and target; perform train-test split.
- **Model Selection**: 
  - Build and compare two models: 
    - Logistic Regression (baseline).
    - An ensemble model (Random Forest or Gradient Boosting).
- **Model Training and Evaluation**: 
  - Train models on both datasets.
  - Use metrics suitable for imbalanced data (AUC-PR, F1-Score, Confusion Matrix).
  - Justify the selection of the best model.

### Task 3 - Model Explainability
- **Use SHAP (Shapley Additive exPlanations)**: Interpret the best-performing model.
- **Generate SHAP Plots**: Create Summary and Force plots to understand feature importance.
- **Final Report**: Explain insights derived from SHAP plots regarding key drivers of fraud.

## Conclusion

This project aims to enhance fraud detection capabilities for e-commerce and banking transactions. By addressing class imbalance, employing robust machine learning models, and utilizing explainability techniques, Adey Innovations Inc. can significantly improve transaction security and foster customer trust.
