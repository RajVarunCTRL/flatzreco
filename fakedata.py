import random
from faker import Faker
import pandas as pd
from datetime import datetime, timedelta


fake = Faker()


usrs = []
communities = ['BlockA', 'BlockB', 'BlockC', 'BlockD', 'BlockE', 'BlockF', 'BlockG', 'BlockH', 'BlockI', 'BlockJ']
intersts = ['Reading', 'Gaming', 'Cooking', 'Traveling', 'Fitness', 'Yoga', 'Photography', 'Music', 'Art', 'Technology', 'Sports', 'Movies', 'Fashion', 'Gardening', 'Writing', 'Dancing', 'Hiking', 'Cycling', 'Fishing', 'Camping']


for i in range(1,101):
    usrs.append({
        
        "id": i,
        "name": fake.name(),
        "community": random.choice(communities),
        "interests": ",".join(random.sample(intersts,3))
    })
    
    
items = []
for i in range(1,501):
    items.append({
        "id": i,
        "title": fake.sentence(nb_words=3),
        "description": fake.text(max_nb_chars=100),
        "tags": ",".join(random.sample(intersts, 2)),
        "creator_id": random.randint(1, 100),
        "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
    })


interactions = []
for i in range(1,1001):
    interactions.append({
        "id": i,
        "title": fake.sentence(nb_words=3),
        "description": fake.text(max_nb_chars=100),
        "tags": ",".join(random.sample(intersts, 2)),
        "creator_id": random.randint(1, 100),
        "timestamp": (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d")
    })

pd.DataFrame(usrs).to_csv('data/users.csv', index=False)
pd.DataFrame(items).to_csv('data/items.csv', index=False)
pd.DataFrame(interactions).to_csv('data/interactions.csv', index=False)
