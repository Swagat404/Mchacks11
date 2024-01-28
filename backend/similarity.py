from sklearn.metrics.pairwise import cosine_similarity
 
def get_similarity(target,candidates):
  # Calculate cosine similarity
  similarity_scores = cosine_similarity(target,candidates)
 
  # Sort by descending order in similarity
  similarity_scores = list(enumerate(similarity_scores))
  similarity_scores = sorted(similarity_scores, key=lambda x:x[1], reverse=True)
 
  # Return similarity scores
  return similarity_scores