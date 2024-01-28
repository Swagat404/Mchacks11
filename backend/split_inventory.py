import pandas as pd

# Load your DataFrame from the CSV file
csv_file_path = 'inventory.csv'
df = pd.read_csv(csv_file_path)

# Assuming 'Label' is the column representing group labels
grouped = df.groupby('Group')

# Iterate over groups and save each group to a separate CSV file
for group_label, group_df in grouped:
    group_df.to_csv(f'group_{group_label}.csv', index=False)
