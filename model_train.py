import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

# load data
df = pd.read_csv('game_data.csv')
df = df.dropna(subset=['genre', 'console', 'critic_score'])

# features
features = df[['genre', 'console', 'critic_score']]

# One-hot encode
encoder = OneHotEncoder()
encoded = encoder.fit_transform(features[['genre', 'console']]).toarray()

# normalize
scaler = MinMaxScaler()
scaled = scaler.fit_transform(features[['critic_score']])


import numpy as np
X = np.concatenate([encoded, scaled], axis=1)

# calculate Cosine Similarity
similarity = cosine_similarity(X)

# save
df['index'] = df.index
df.to_csv("game_index.csv", index=False)
np.save("similarity_matrix.npy", similarity)
