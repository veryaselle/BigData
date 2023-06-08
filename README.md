From https://git.informatik.uni-leipzig.de/dbs/big-data-praktikum/-/blob/master/05_playlist_link_prediction.md


Predict tracks that could belong to a playlist with Knowledge Graph Embeddings

Motivation
Link prediction aims to predict relations that likely are missing in a knowledge graph. A variety of models exist nowadays that encode entities and relations of a knowledge graph in a low-dimensional vector space in order to predict missing links.
The structure of information from the music domain is well fitted to be represented as a knowledge graph, with artists, albums, tracks and playlists as nodes and a variety of relationship types connecting them.
Several datasets exist, where spotify playlist data was shared, with the goal of performing music recommendation.

Goal
Your task is to transform this data into a knowledge graph in order to use the pykeen framework for link prediction.

Work packages

1. Transformation
Transform the dataset into a knowledge graph with a pipeline suitable for this amount of data.

2. Loading, Training and Evaluating
Create a dataset class in order to load the data into pykeen and train and evaluate knowledge graph embedding models.

3. Presentation
Present your results in 10-minute presentation.
