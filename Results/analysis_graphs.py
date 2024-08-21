import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the medquad.csv dataset
medquad_df = pd.read_csv('medquad.csv')

# Set up the plotting style
plt.style.use('ggplot')  # Using a different style
plt.figure(figsize=(15, 10))

# 1. Unique Values per Column
unique_values = medquad_df.nunique()
plt.subplot(2, 2, 1)
sns.barplot(x=unique_values.index, y=unique_values.values)
plt.title('Unique Values per Column')
plt.xticks(rotation=45)
plt.ylabel('Count')

# 2. Missing Values per Column
missing_values = medquad_df.isnull().sum()
plt.subplot(2, 2, 2)
sns.barplot(x=missing_values.index, y=missing_values.values)
plt.title('Missing Values per Column')
plt.xticks(rotation=45)
plt.ylabel('Count')

# 3. Distribution of Answer Lengths
medquad_df['answer_length'] = medquad_df['answer'].str.len()
plt.subplot(2, 2, 3)
sns.histplot(data=medquad_df, x='answer_length', kde=True)
plt.title('Distribution of Answer Lengths')
plt.xlabel('Length (characters)')

# 4. Distribution of Question Lengths
medquad_df['question_length'] = medquad_df['question'].str.len()
plt.subplot(2, 2, 4)
sns.histplot(data=medquad_df, x='question_length', kde=True)
plt.title('Distribution of Question Lengths')
plt.xlabel('Length (characters)')

plt.tight_layout()
plt.show()

# Display summary statistics for answer and question lengths
print("Summary Statistics for Answer Lengths:")
print(medquad_df['answer_length'].describe())
print("\
Summary Statistics for Question Lengths:")
print(medquad_df['question_length'].describe())