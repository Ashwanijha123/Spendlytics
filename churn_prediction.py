import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
churn_df = pd.read_csv('data/churn_data.csv')

# Handle missing values
churn_df.fillna(churn_df.mean(numeric_only=True), inplace=True)

# Encode categorical variables
churn_df['Gender'] = churn_df['Gender'].map({'Male': 0, 'Female': 1})

# Feature and target separation
X = churn_df.drop(['CustomerID', 'Churn'], axis=1)
y = churn_df['Churn']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression model
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)
log_preds = log_model.predict(X_test)

# Decision Tree model
tree_model = DecisionTreeClassifier(max_depth=4)
tree_model.fit(X_train, y_train)
tree_preds = tree_model.predict(X_test)

# Evaluation Reports
print("🔍 Logistic Regression Report:\n", classification_report(y_test, log_preds))
print("🌳 Decision Tree Report:\n", classification_report(y_test, tree_preds))

# Confusion Matrix Plots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.heatmap(confusion_matrix(y_test, log_preds), annot=True, fmt='d', cmap='Blues')
plt.title('Logistic Regression Confusion Matrix')

plt.subplot(1, 2, 2)
sns.heatmap(confusion_matrix(y_test, tree_preds), annot=True, fmt='d', cmap='Greens')
plt.title('Decision Tree Confusion Matrix')

plt.tight_layout()
plt.show()
