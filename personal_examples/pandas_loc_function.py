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

#%%
# Select multiple rows by label
print(df.loc[['wine1', 'wine3']])

#%%
# Select specific rows and columns
print(df.loc[['wine1', 'wine3'], ['fixed_acidity', 'quality']])

#%%
# Select rows where 'quality' is greater than 5
print(df.loc[df['quality'] > 5])

#%%
# Set the value of 'quality' for 'wine1' to 6
df.loc['wine1', 'quality'] = 6
print(df)

#%%
# Select a slice of rows and specific columns
print(df.loc['wine1':'wine2', 'fixed_acidity':'citric_acid'])
