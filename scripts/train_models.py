""" Train Models using the data, CONTENT Based Modelling"""

import os
import pandas as pd
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# CONFIGURATION
DATA_DIR = 'data'
MODELS_DIR = 'trained_models'
os.makedirs(MODELS_DIR, exist_ok=True)


def train_content_based_model():
    print("Startin trainig for content based model")
    items_df = pd.read_csv(DATA_DIR, 'items.csv')
    
    model = SentenceTransformer('all-MiniLM-L6-v2') # Lightweight Model for training
    print("Generating items embeddings...")
    item_embeddings = model.encode(items_df['text_content'].tolist(), show_progress_bar=True)

    embeddings_path = os.path.join(MODELS_DIR, 'item_embeddings.npy')
    item_ids_path = os.path.join(MODELS_DIR, 'item_ids.pkl')
    np.save(embeddings_path, item_embeddings)
    with open(item_ids_path, 'wb') as f:
        pickle.dump(items_df['item_id'].tolist(), f)
        
    print(f"Content-based model assets saved to '{MODELS_DIR}'")
    
    
    # SVD
def train_collaborative_filtering_model():
    print("Starting training for collaborative filtering model")
    interactions_df = pd.read_csv(os.path.join(DATA_DIR, 'interactions.csv'))
    
    rating_map = {
        'like' : 3.0, 
        'comment' : 2.0,
        'view' : 1.0,
    }
    
    interactions_df['rating'] = interactions_df['interaction_type'].map(rating_map)
    interactions_df = interactions_df.dropna(subset=['rating'])
    
    reader = Reader(rating_scale=(1, 3))
    data = Dataset.load_from_df(interactions_df[['user_id', 'item_id', 'rating']], reader)
    
    trainset = data.build_full_trainset()
    
    algo = SVD(n_factors=50, n_epochs=20, random_state=42)
    algo.fit(trainset)
    
    model_path = os.path.join(MODELS_DIR, 'svd_model.pkl')
    
    with open(model_path, 'wb') as f:
        pickle.dump(algo, f)
    print(f"Collaborative filtering model saved to '{model_path}'")
    
if __name__ == "__main__":
    train_content_based_model()
    train_collaborative_filtering_model()
    print("Training completed successfully.")
    
