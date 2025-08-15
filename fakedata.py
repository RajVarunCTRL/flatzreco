
"""fakedata.py - GENERATED FAKE DATA FOR TESTING
This script generates fake user, item, and interaction data for testing purposes."""
import os
import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta


fake = Faker()
Faker.seed(42)

num_users = 100
num_items = 500
num_interactions = 2000

communities = ['BlockA', 'BlockB', 'BlockC', 'BlockD', 'BlockE']
interests = ['Reading', 'Gaming', 'Cooking', 'Traveling', 'Fitness', 'Yoga', 'Photography', 'Music', 'Art', 'Technology', 'Sports', 'Movies', 'Fashion', 'Gardening', 'Writing', 'Dancing', 'Hiking', 'Cycling', 'Fishing', 'Camping']
interactions_types = ['view', 'like', 'comment', 'report'] # Interaction types


# Generate fake user data here
users=[]
for i in range(1,num_users + 1):
    users.append({
        
        "user_id": i,
        "name": fake.name(),
        "community_id": random.choice(communities),
        "interests": ",".join(random.sample(interests,3))   
    })
    
# Generate fake items data here    
items = []
for i in range(1,num_items + 1):
    items.append({
        "item_id": i,
        "text_content": fake.sentence(nb_words=15),
        "tags": ",".join(random.sample(interests, 2)),
        "creator_id": random.randint(1, num_users),
        "community_id": random.choice(communities),
        "created_at": (datetime.now() - timedelta(days=random.randint(0, 60))).strftime("%Y-%m-%d %H:%M:%S"),
    })

# Generate fake interactions data here
interactions = []
for i in range(1,num_interactions+1):
    interactions.append({
        "interactions_id": i,
        "user_id": random.randint(1, num_users),
        "item_id": random.randint(1, num_items),
        "interaction_type": random.choices(interactions_types, weights=[0.7, 0.2, 0.08, 0.02], k=1)[0],
        "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S")
    })

print("saving data to csv files")

output_dir = 'data'
os.makedirs(output_dir, exist_ok=True)


pd.DataFrame(users).to_csv(f'{output_dir}/users.csv', index=False)
pd.DataFrame(items).to_csv(f'{output_dir}/items.csv', index=False)
pd.DataFrame(interactions).to_csv(f'{output_dir}/interactions.csv', index=False)
