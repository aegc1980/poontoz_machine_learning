# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Using sample cleaned data
data = [
    {"id": "1", "name": "Club One", "loyalty_details": "Basic loyalty program", "engagement_score": 9},
    {"id": "2", "name": "Club Two", "loyalty_details": "Advanced loyalty program", "engagement_score": 8},
    {"id": "3", "name": "Unknown Club", "loyalty_details": "Missing club name", "engagement_score": 11}
]
df = pd.DataFrame(data)
print("Data Preview:")
print(df.head())
print("\nData Summary:")
print(df.describe(include='all'))
print("\nMissing Values:")
print(df.isnull().sum())

# Create a bar chart and histogram
plt.figure(figsize=(8, 4))
sns.barplot(x='name', y='engagement_score', data=df, palette='viridis')
plt.title('Engagement Score by Club')
plt.xlabel('Club Name')
plt.ylabel('Engagement Score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(df['engagement_score'], bins=5, kde=True, color='blue')
plt.title('Distribution of Engagement Scores')
plt.xlabel('Engagement Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
