import cohere
co = cohere.Client('N6QiQiluGSigbLtBJgUogrjhW3SZQmSFiK8Npgit')
import pandas as pd



# Specify the path to your CSV file
csv_file_path = 'group_Upperwear.csv'

# Use read_csv to load the DataFrame from the CSV file
df = pd.read_csv(csv_file_path)
import pandas as pd

# Get the total number of rows in the DataFrame
total_rows = df.shape[0]

# Calculate the midpoint to split the DataFrame into two halves
midpoint = total_rows // 2

# Split the DataFrame into two halves
df_first_half = df.iloc[:midpoint]
df_second_half = df.iloc[midpoint:]

# Display the two halves
print("First Half:")
print(df_first_half)

print("\nSecond Half:")
print(df_second_half)

articles = df_first_half['Color'].tolist()

output = co.embed(
            model ='embed-english-v3.0',
            input_type='search_document',
            texts = articles)
embeds = output.embeddings
df_first_half['Color_embeddings']=embeds

import time

# Wait for 1 minute
time.sleep(60)
print("1 minute has passed!")



articles = df_second_half['Color'].tolist()

output = co.embed(
            model ='embed-english-v3.0',
            input_type='search_document',
            texts = articles)
embeds = output.embeddings
df_second_half['Color_embeddings']=embeds
combined_df = pd.concat([df_first_half, df_second_half], ignore_index=True)


combined_df.to_csv('group_Upperwear.csv', index=False)
