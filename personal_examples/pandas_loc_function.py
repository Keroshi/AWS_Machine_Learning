import pandas as pd

# Create a sample DataFrame
data = {
    'fixed_acidity': [7.4, 7.8, 7.8],
    'volatile_acidity': [0.7, 0.88, 0.76],
    'citric_acid': [0, 0, 0.04],
    'residual_sugar': [1.9, 2.6, 2.3],
    'quality': [5, 5, 5]
}

df = pd.DataFrame(data, index=['wine1', 'wine2', 'wine3'])

# Select a single row by label
print(df.loc['wine1'])
