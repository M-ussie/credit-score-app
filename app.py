import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Load the trained model
best_model = joblib.load('best_credit_score_model.pkl')

# Initialize Flask app
app = Flask(__name__)

# Define the expected columns based on the training data
expected_columns = [
    'Age', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts',
    'Num_Credit_Card', 'Interest_Rate', 'Delay_from_due_date',
    'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 'Num_Credit_Inquiries',
    'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Credit_History_Age',
    'Total_EMI_per_month', 'Amount_invested_monthly', 'Monthly_Balance',
    'Count_Auto Loan', 'Count_Credit-Builder Loan', 'Count_Personal Loan',
    'Count_Home Equity Loan', 'Count_Not Specified', 'Count_Mortgage Loan',
    'Count_Student Loan', 'Count_Debt Consolidation Loan', 'Count_Payday Loan',
    'Month', 'Occupation', 'Credit_Mix', 'Payment_of_Min_Amount', 'Payment_Behaviour'
]

# Define preprocessing function
def preprocess_data(data):
    app.logger.debug(f"Original Data: {data}")

    df = pd.DataFrame([data])
    app.logger.debug(f"DataFrame created from data: {df}")

    # Log column names for debugging
    app.logger.debug(f"DataFrame columns: {df.columns.tolist()}")

    # Add any missing columns with default values
    for col in expected_columns:
        if col not in df.columns:
            if col in ['Month', 'Occupation', 'Credit_Mix', 'Payment_of_Min_Amount', 'Payment_Behaviour']:
                df[col] = 'Unknown'
            else:
                df[col] = 0
    app.logger.debug(f"DataFrame with all expected columns: {df}")

    # Define categorical features
    categorical_features = ['Month', 'Occupation', 'Credit_Mix', 'Payment_of_Min_Amount', 'Payment_Behaviour']

    # Convert categorical features to category dtype
    for feature in categorical_features:
        if feature in df.columns:
            try:
                df[feature] = df[feature].astype('category')
                app.logger.debug(f"Converted {feature} to categorical: {df[feature]}")
            except Exception as e:
                app.logger.error(f"Error converting {feature} to categorical: {e}")

    app.logger.debug(f"DataFrame with categorical features converted: {df}")

    return df

# Define a prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        app.logger.debug(f"Received request data: {data}")

        if not data:
            app.logger.error("No data provided")
            return jsonify({'error': 'No data provided'}), 400

        # Preprocess the input data
        input_data = preprocess_data(data)

        # Log the preprocessed data for debugging
        app.logger.debug(f"Preprocessed Data: {input_data}")

        # Use the fitted model to transform and predict
        prediction = best_model.predict(input_data)
        app.logger.debug(f"Prediction: {prediction}")

        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)