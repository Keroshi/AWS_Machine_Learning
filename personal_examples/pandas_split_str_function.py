import pandas as pd

# Create the DataFrame
data = {'name': ['Jason Ndirangu']}
df = pd.DataFrame(data)


# Function to split the name column into first_name and last_name
def split_names(df):
    df[['first_name', 'last_name']] = df['name'].str.split(' ', n=1, expand=True)
    return df


# Apply the function
df = split_names(df)

print(df)
