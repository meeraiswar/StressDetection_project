import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Generate 100 rows of random data with floating-point values
data = {
     'Snoring Rate': np.random.uniform(46, 98, 100),  # Snoring rate between 0 and 15 (arbitrary scale)
      'Respiratory Rate': np.random.uniform(15, 30, 100),  # Respiratory rate between 12 and 25 breaths per minute
        'Body Temperature': np.random.uniform(86,98, 100),  # Skin temperature between 32 and 37 degrees Celsius
          'Limb Movement': np.random.uniform(5, 18, 100),  # Body movements between 0 and 30
           'Blood Oxygen': np.random.uniform(84,96, 100),  # Blood oxygen level between 90 and 100%
             'Eye Movement': np.random.uniform(60, 105, 100),  # Sleeping hours between 4 and 10 hours
              'Sleep Hours': np.random.uniform(0,9, 100),  # Sleeping hours between 4 and 10 hours
               'Heart Rate': np.random.uniform(52,84, 100),  # Heart rate between 60 and 100 bpm
                'Stress Level': np.random.randint(0, 2, 100),  # Stress level binary: 0 (no stress) or 1 (stress)
}

   
  
   
    
   
   
  
   
  
   

# Create a DataFrame from the generated data
df = pd.DataFrame(data)

# Round all numeric columns to 2 decimal places
df = df.round(2)

# Save the DataFrame to a CSV file
df.to_csv('stress_prediction_data.csv', index=False)

print("CSV file created: stress_prediction_data.csv")