# This entrypoint file to be used in development. Start by reading README.md
import medical_data_visualizer
from unittest import main

# # Test your function by calling it here
# medical_data_visualizer.draw_cat_plot()
# medical_data_visualizer.draw_heat_map()

# # Run unit tests automatically
# main(module='test_module', exit=False)

import pandas as pd

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmis = []

for index, person in df.iterrows():
  height = person['height']
  weight = person['weight']
  bmi = weight / ((height / 100)**2)
  bmis.append(bmi)

df['overweight'] = [1 if bmi > 25 else 0 for bmi in bmis]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = [
    0 if cholesterol <= 1 else 1 for cholesterol in df['cholesterol']
]
df['gluc'] = [0 if gluc <= 1 else 1 for gluc in df['gluc']]

# Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
df_cat = pd.melt(df,
                 value_vars=[
                     'cholesterol', 'gluc', 'smoke', 'alco', 'active',
                     'overweight'
                 ])

# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
df_cat = df.groupby('cardio').count()
print(df_cat)
