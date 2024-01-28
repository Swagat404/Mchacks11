import cohere
import pandas as pd
import umap
import altair as alt
from bertopic import BERTopic
from datasets import load_dataset
from typing import Optional, List
import numpy as np
#a=open("finalcorrected.json","r")
#original_string = a.read()
#df = pd.read_json("finalcorrected.json")
co = cohere.Client('N6QiQiluGSigbLtBJgUogrjhW3SZQmSFiK8Npgit')


import json

with open("finalcorrected.json", "r") as file:
    data = json.load(file)

print(type(data))
print(len(data))
df = pd.DataFrame.from_dict(data)
print(df)
text_columns = ['Name', 'Description']

# Concatenate text from specified columns into a new column 'combined_text'
df['combined_text'] = df[text_columns].apply(lambda row: ' '.join(row), axis=1)
embeddings = co.embed(texts=list(df['combined_text']), truncate="RIGHT").embeddings
embeddings = np.array(embeddings)



title = "Commands to AI personal assistant"

from sklearn.cluster import KMeans


n_clusters = 15

# Load and initialize BERTopic to use KMeans clustering with 8 clusters only.
cluster_model = KMeans(n_clusters=n_clusters)
topic_model = BERTopic(hdbscan_model=cluster_model)

# df is a dataframe. df['title'] is the column of text we're modeling
df['topic'], probabilities = topic_model.fit_transform(df['combined_text'], embeddings)
keywords = topic_model.generate_topic_labels()
df['cluster_keywords'] = df['topic'].map(lambda x: keywords[x])
df.to_csv('dataframe1.csv', index=False)

print(df)
def interactive_clusters_scatterplot(
        df: pd.DataFrame,
        fields_in_tooltip: List[str] = None,
        title: str = '',
        title_column: str = 'keywords'
):
    if fields_in_tooltip is None:
        fields_in_tooltip = ['']

    selection = alt.selection_multi(fields=[title_column], bind='legend')

    chart = alt.Chart(df).transform_calculate(
    ).mark_circle(size=20, stroke='#666', strokeWidth=1, opacity=0.1).encode(
        x= 
        alt.X('x',
              scale=alt.Scale(zero=False),
              axis=alt.Axis(labels=False, ticks=False, domain=False)
              ),
        y=
        alt.Y('y',
              scale=alt.Scale(zero=False),
              axis=alt.Axis(labels=False, ticks=False, domain=False)
              ),

        color=alt.Color(f'{title_column}:N',
                        legend=alt.Legend(columns=2,
                                          symbolLimit=0,
                                          orient='right',
                                          labelFontSize=12)
                        ),
        opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
        tooltip=fields_in_tooltip
    ).properties(
        width=600,
        height=400
    ).add_selection(
        selection
    ).configure_legend(labelLimit=0).configure_view(
        strokeWidth=0
    ).configure(background="#F6f6f6").properties(
        title=title
    ).configure_range(
        category={'scheme': 'category20'}
    )
    return chart 

# Reduce dimensions to be able to plot the embeddings
n_neighbors = 15
reducer = umap.UMAP(n_neighbors=n_neighbors)
umap_embeds = reducer.fit_transform(embeddings)
df['x'] = umap_embeds[:, 0]
df['y'] = umap_embeds[:, 1]

# Specify the names of columns to plot

title_column = 'cluster_keywords'
fields_in_tooltip = ['combined_text', 'topic', 'cluster_keywords']


title = "Commands to AI personal assistant"

chart = interactive_clusters_scatterplot(df,
                                            fields_in_tooltip=fields_in_tooltip,
                                            title=title + " - " + str(n_clusters) + " clusters",
                                            title_column=title_column)
chart.save("chart3.html")

