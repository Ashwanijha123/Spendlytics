# Spendlytics
“Smart analytics pipeline for churn prediction &amp; expense tracking”

💼 Spendlytics: Smart Insights from Churn and Expense Data
Spendlytics is a dual-purpose data analytics project combining Customer Churn Prediction (Supervised Learning) with a Personal Expense Tracker (Unsupervised Insights + SQL + Visualisation). It’s designed to showcase a comprehensive data analytics pipeline used in real-world business and personal finance scenarios.

🔍 Modules Covered

🔮 Customer Churn Prediction
Logistic Regression and Decision Tree classifiers
Handling missing data
Model comparison and evaluation (confusion matrix, classification report)

💰 Personal Expense Tracker
SQL queries on expense data (e.g., total spend by category)
K-Means clustering of user spending patterns
Visualizations using matplotlib/seaborn

🛠 Techniques Used
Supervised & Unsupervised Learning
SQL querying using SQLite
Data cleaning & feature engineering
Data visualization

📂 Project Structure

spendlytics/

├── data/

│   ├── churn_data.csv

│   └── expense_data.csv

├── churn_prediction.py

├── expense_tracker.py

├── spendlytics.ipynb

├── README.md

├── requirements.txt

⚙️ Requirements

pip install -r requirements.txt

🚀 To Run
Run
churn_prediction.py
for classification models.
Run
expense_tracker.py
to load and analyze expense data via SQL & clustering.
Open the
.ipynb
notebook for a step-by-step walkthrough.

📈 Sample SQL Queries

SELECT Category, SUM(Amount) as Total FROM expenses GROUP BY Category;

SELECT UserID,
  CASE
    WHEN SUM(Amount) > 50000 THEN 'High'
    WHEN SUM(Amount) BETWEEN 20000 AND 50000 THEN 'Medium'
    ELSE 'Low'
  END AS Spending_Level
FROM expenses

👨‍💻 Author
Ashwani Jha
📍 India
📫 GitHub: Ashwanijha123

