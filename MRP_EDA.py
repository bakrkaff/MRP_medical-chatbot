import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'medquad.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
data.head(), data.info()

# Summary statistics for the dataset
summary_statistics = {
    'Unique Values per Column': data.nunique(),
    'Missing Values per Column': data.isnull().sum(),
    'Length of Answers': data['answer'].str.len().describe(),
    'Length of Questions': data['question'].str.len().describe()
}

summary_statistics

# Optimized histogram of the top 20 focus areas
plt.figure(figsize=(10, 6))
data['focus_area'].value_counts().nlargest(20).plot(kind='bar')
plt.title('Top 20 Focus Areas')
plt.xlabel('Focus Area')
plt.ylabel('Count')
plt.show()

# Optimized box plot for answer lengths
plt.figure(figsize=(10, 6))
data['answer'].str.len().plot(kind='box')
plt.title('Box Plot of Answer Lengths')
plt.ylabel('Length of Answer (characters)')
plt.show()

# Sample the data for scatter plot to reduce plotting time
sampled_data = data.sample(n=1000, random_state=1)

# Scatter plot of question lengths vs. answer lengths
plt.figure(figsize=(10, 6))
plt.scatter(sampled_data['question'].str.len(), sampled_data['answer'].str.len(), alpha=0.5)
plt.title('Scatter Plot of Question Lengths vs. Answer Lengths (Sampled Data)')
plt.xlabel('Question Length (characters)')
plt.ylabel('Answer Length (characters)')
plt.show()

