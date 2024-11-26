import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the data
df = pd.read_csv('stress_prediction_data.csv')

# Set Seaborn style
sns.set(style="whitegrid")

# Group by Stress Level and count the occurrences
stress_level_counts = df['Stress Level'].value_counts().reset_index()
stress_level_counts.columns = ['Stress Level', 'Count']

# Plot the pie chart
plt.figure(figsize=(8,8))
plt.pie(stress_level_counts['Count'], labels=stress_level_counts['Stress Level'], 
        autopct='%1.1f%%', colors=sns.color_palette('coolwarm', len(stress_level_counts)), 
        startangle=140, explode=[0.05]*len(stress_level_counts), shadow=True)

# Title for the chart
plt.title('Distribution of Stress Levels')

# Display the pie chart
plt.show()
