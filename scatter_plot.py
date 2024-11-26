import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load data
df = pd.read_csv('stress_prediction_data.csv')

# Scatter plot with size mapped to body movements
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Heart Rate', y='Limb Movement', hue='Stress Level', size='Limb Movement', sizes=(40, 400), palette='coolwarm', alpha=0.8)
plt.title('Heart rate vs. Limb Movement with Size Mapping')
plt.xlabel('Heart Rate')
plt.ylabel('Limb Movement')
plt.legend(title='Stress level', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
