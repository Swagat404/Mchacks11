import cohere
co = cohere.Client('N6QiQiluGSigbLtBJgUogrjhW3SZQmSFiK8Npgit')
import pandas as pd



# Specify the path to your CSV file
csv_file_path = 'group_Non-Clothing.csv'

# Use read_csv to load the DataFrame from the CSV file
df = pd.read_csv(csv_file_path)
articles = df['Color'].tolist()

output = co.embed(
            model ='embed-english-v3.0',
            input_type='search_document',
            texts = articles)
embeds = output.embeddings
df['Color_embeddings']=embeds
df.to_csv('group_Non-Clothing.csv', index=False)

import time

# Wait for 1 minute
time.sleep(60)
print("1 minute has passed!")




# Specify the path to your CSV file
csv_file_path = 'group_Accessories.csv'

# Use read_csv to load the DataFrame from the CSV file
df = pd.read_csv(csv_file_path)
articles = df['Color'].tolist()

output = co.embed(
            model ='embed-english-v3.0',
            input_type='search_document',
            texts = articles)
embeds = output.embeddings
df['Color_embeddings']=embeds
df.to_csv('group_Accessories.csv', index=False)


# Wait for 1 minute
time.sleep(60)
print("1 minute has passed!")




# Specify the path to your CSV file
csv_file_path = 'group_Bottomwear.csv'

# Use read_csv to load the DataFrame from the CSV file
df = pd.read_csv(csv_file_path)
articles = df['Color'].tolist()

output = co.embed(
            model ='embed-english-v3.0',
            input_type='search_document',
            texts = articles)
embeds = output.embeddings
df['Color_embeddings']=embeds
df.to_csv('group_Bottomwear.csv', index=False)


# Wait for 1 minute
time.sleep(60)
print("1 minute has passed!")




# Specify the path to your CSV file
csv_file_path = 'group_Non-Clothing.csv'

# Use read_csv to load the DataFrame from the CSV file
df = pd.read_csv(csv_file_path)
articles = df['Color'].tolist()

output = co.embed(
            model ='embed-english-v3.0',
            input_type='search_document',
            texts = articles)
embeds = output.embeddings
df['Color_embeddings']=embeds
df.to_csv('group_Non-Clothing.csv', index=False)
