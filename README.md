Credit Score Classification Project

Welcome to my Credit Score Classification Project. This project aims to classify credit scores using a Support Vector Machine (SVM) model. It includes 

comprehensive data preprocessing, model training, hyperparameter tuning, and deployment of the classification model as a web application.

Project Files

app.py: The main Flask application file that serves the model.

best_credit_score_model.pkl: The trained machine learning model.

credit_scores.csv: The dataset used for training and testing.

requirements.txt: A list of dependencies required to run the project.

runtime.txt: Specifies the Python version for the project.

Procfile: Specifies the commands to run the application on Heroku.

.slugignore: File to exclude unnecessary files during deployment.


Kaggle Notebook

For detailed analysis and model training, please refer to my Kaggle notebook: 

(https://www.kaggle.com/code/mussiehaileselassie/mussie-girmay-5)

How to Run Locally

To run the project locally, follow these steps:

Clone the repository:

git clone

https://github.com/M-ussie/credit-score-app.git

cd credit-score-app

Create a virtual environment and install dependencies:

python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

Run the application:

python app.py


API Usage

You can use Postman or CURL to test the API. Below is an example of how to use CURL:

curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d 


'{
    "Age": 45,
    
    "Annual_Income": 120000,
    
    "Monthly_Inhand_Salary": 10000,
    
    "Num_Bank_Accounts": 2,
    
    "Num_Credit_Card": 3,
    
    "Interest_Rate": 5,
    
    "Delay_from_due_date": 2,
    
    "Num_of_Delayed_Payment": 1,
    
    "Changed_Credit_Limit": 10000,
    
    "Num_Credit_Inquiries": 2,
    
    "Outstanding_Debt": 5000,
    
    "Credit_Utilization_Ratio": 30,
    
    "Credit_History_Age": 10,
    
    "Total_EMI_per_month": 2000,
    
    "Amount_invested_monthly": 1500,
    
    "Monthly_Balance": 8000,
    
    "Count_Auto Loan": 1,
    
    "Count_Credit-Builder Loan": 0,
    
    "Count_Personal Loan": 1,
    
    "Count_Home Equity Loan": 0,
    
    "Count_Not Specified": 0,
    
    "Count_Mortgage Loan": 1,
    
    "Count_Student Loan": 0,
    
    "Count_Debt Consolidation Loan": 0,
    
    "Count_Payday Loan": 0,
    
    "Month": "January",
    
    "Occupation": "Engineer",
    
    "Credit_Mix": "Good",
    
    "Payment_of_Min_Amount": "Yes",
    
    "Payment_Behaviour": "Regular"
}'


 Screenshots
 
 Postman

  The following screenshot shows a successful request made using Postman:
 
 ![image](https://github.com/M-ussie/credit-score-app/assets/108830669/af9466f1-29f4-4088-9c29-69f2ec0b0601)
 ![image](https://github.com/M-ussie/credit-score-app/assets/108830669/c177643a-8a55-4b29-a5f8-766da11c2055)

 
 ## Deployed Application

The web application is deployed on Heroku: 

The following screenshot shows the application successfully deployed on Heroku:

 Heroku

 
 ![Screenshot 2024-05-23 144355](https://github.com/M-ussie/credit-score-app/assets/108830669/9c5a6133-eca9-4b62-a9dc-da035791ef6a)

![Screenshot 2024-05-23 144440](https://github.com/M-ussie/credit-score-app/assets/108830669/b427d359-28e2-49bb-aba1-f6e508274df4)





Links

GitHub Repository: https://github.com/M-ussie/credit-score-app

Kaggle Notebook: https://www.kaggle.com/code/mussiehaileselassie/mussie-girmay-5









