import pandas as pd
import json

# Read JSON data from the file
with open('finalviz.vl.json', 'r') as file:
    json_data = json.load(file)

# Extract the dataset from JSON
dataset = json_data['datasets']['data-68ebb9ac10e75cc52bcbbcf9f1da75dd']

# Convert to Pandas DataFrame
df = pd.DataFrame(dataset)
selected_columns = ['Color', 'Name', 'Description', 'combined_text', 'topic', 'Label']
df = df[selected_columns]
# Display the DataFrame
print(df)

Categories_minor={0:"casual pants,leggins,shorts",10:"Jackets,blazers",11:"accessories and combo packs",12:"Jeans",13:"Fragrances",14:"Jacket",1:"Dress,short skirt",2:"Footwear",3:"Shirt",4:"non-clothing stuff",5:"top,blouse,jumpsuit",6:"round-neck tshirt",7:"woolen articles,sweaters",8:"non clothing stuff",9:"bags"}


df['Categories_minor'] = df['topic'].map(Categories_minor)

# Display the DataFrame
print(df[["Name", "topic", "Categories_minor"]])

bottomwear_topics = [0, 12, 1]
upperwear_topics = [10, 14, 3, 5, 6, 7]
accessories_topics = [11, 13, 9]
non_clothing_topics = [4, 8]

# Assign groups based on topic values
df['Group'] = pd.cut(df['topic'],
                     bins=[-1, 1, 3, 7, 12],
                     labels=['Bottomwear', 'Upperwear', 'Accessories', 'Non-Clothing'])


df['Merged_description'] = df['combined_text'] + ' ' + df['Categories_minor']
# Display the DataFrame
print(df[["Name", "topic", "Categories_minor", "Group"]])
df.to_csv("inventory.csv", index=False)
