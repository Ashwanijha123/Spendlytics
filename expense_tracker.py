import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load expense data
exp_df = pd.read_csv('data/expense_data.csv')

# Create SQLite in-memory database
conn = sqlite3.connect(':memory:')
exp_df.to_sql('expenses', conn, if_exists='replace', index=False)

# Query 1: Total spending by category
query1 = "SELECT Category, SUM(Amount) as Total FROM expenses GROUP BY Category;"
category_totals = pd.read_sql_query(query1, conn)
print("💰 Total Spend by Category:\n", category_totals)

# Query 2: Spending level classification per user
query2 = '''
SELECT UserID,
  CASE
    WHEN SUM(Amount) > 50000 THEN 'High'
    WHEN SUM(Amount) BETWEEN 20000 AND 50000 THEN 'Medium'
    ELSE 'Low'
  END AS Spending_Level
FROM expenses
GROUP BY UserID;
'''
spending_levels = pd.read_sql_query(query2, conn)
print("\n📊 Spending Level by User:\n", spending_levels)

# Unsupervised Learning: K-Means clustering on user spending
user_spending = exp_df.groupby('UserID')['Amount'].sum().reset_index()
kmeans = KMeans(n_clusters=3, random_state=0)
user_spending['Cluster'] = kmeans.fit_predict(user_spending[['Amount']])

# Visualize Clusters
plt.figure(figsize=(8, 5))
sns.scatterplot(data=user_spending, x='UserID', y='Amount', hue='Cluster', palette='Set2', s=100)
plt.title('User Spending Clusters (K-Means)')
plt.xlabel('User ID')
plt.ylabel('Total Amount Spent')
plt.grid(True)
plt.tight_layout()
plt.show()

# Close DB connection
conn.close()
