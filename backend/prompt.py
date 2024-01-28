import cohere
#from similarity import get_similarity
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import ast

import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os
def configure():
     load_dotenv()

configure()
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
headers = {"Authorization": f"Bearer {os.getenv('hugging_key')}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

# You can access the image with PIL.Image for example








co = cohere.Client(os.getenv('cohere_key'))

def extract_tags(article):
    prompt = f"""Given an article, extract a list of tags containing Name of colours, type of clothing that is, whether formal/informal,
    and weather, whether summer(hot) or winter(cold)
    laptop\n--\nArticle:{article}\n\nTags:"""
  
    prediction = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=50,
        temperature=0.3
    )

    return prediction.generations[0].text

a = extract_tags("I need a dress for a summer wedding. The weather will be hot, so I want something lightweight and breathable.A floral pattern would be nice, and I prefer vibrant colors like pink or yellow. I'm thinking of a midi length with a flowy fit. Also, I need comfortable sandals to go with the dress.")
print(a)
print(type(a))
articles=[]
articles.append(a)
print(articles)
print(type(articles))
output = co.embed(
    model='embed-english-v3.0',
    input_type='search_document',
    texts=articles
)

embeds = output.embeddings

print('Number of articles:', len(embeds))

reading=embeds

def get_similarity(reading,candidates):
  # Turn list into array
  candidates = np.array(candidates)
  reading = np.expand_dims(np.array(reading),axis=0)

  # Calculate cosine similarity
  similarity_scores = cosine_similarity(reading,candidates)
  similarity_scores = np.squeeze(similarity_scores).tolist()

  # Sort by descending order in similarity
  similarity_scores = list(enumerate(similarity_scores))
  similarity_scores = sorted(similarity_scores, key=lambda x:x[1], reverse=True)

  # Return similarity scores
  return similarity_scores

df = pd.read_csv("group_Upperwear.csv")
candidates=df['Color_embeddings']
print(candidates)
print(len(candidates))
print("/n/n/n/n")
reading=reading[0]
print(reading)
print(type(reading))
print(candidates)
reading=np.array(reading)
candidates=np.array(candidates)
candidates = [ast.literal_eval(candidate) for candidate in candidates]
candidates=np.array(candidates)
reading_shape = reading.shape
candidates_shape = candidates.shape
#reading.tolist()
#candidates.tolist()

print("Reading Array Shape:", reading_shape)
print("Candidates Array Shape:", candidates_shape)
similarity = get_similarity(reading,candidates)
# View the top 5 articles
print('Target:')
print(articles)

print('Candidates:')
# Assuming similarity is a list of tuples where each tuple contains (index, similarity_score)
top_5_candidates = similarity[1:6]  # Exclude the target article

# Print the top 5 candidates
print('Top 5 Candidates:')
for i, score in top_5_candidates:
    candidate_data = df.drop(columns='Color_embeddings').loc[i]
    print(f'Candidate ID: {i}, Similarity Score: {score}')
    print(candidate_data)
    print('\n')
    description = candidate_data['Merged_description']  # Assuming 'Description' is the column with descriptions
    color=candidate_data['Color']
    name=candidate_data['Name']
    image_prompt=description+color
    # Generate image based on the description
    image_bytes = query({
	"inputs": image_prompt})

    image = Image.open(io.BytesIO(image_bytes))
    file_name = f'output_image_{i+score}.png'

     #Save the image to the file
    image.save(file_name)
