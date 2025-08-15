# READACTED - STOPPED_DEV
## Personalized Community & Service Recommendations


***Note*** : Tech stack to be used: python for AI models,fast API for backend,PostgreSQL
for databases and any choice of frontend as the main focus is on the backend
implementation and AI models for which the tech stack aligns with FlatZ.

### Goal
Build a production‑lean recommendation service that powers a “For You” feed for FlatZ
residents. The service must:
1) ingest & train on sample data,
2) generate personalized candidates,
3) rank items,
4) expose a FastAPI endpoint returning ranked recommendations with short “reason”
strings,
5) log user feedback events.

### Scope of Work
You will design and implement:
- Data layer (Postgres/SQLite) for users, items, interactions
- Content-based retrieval via text embeddings
- Collaborative filtering method
- Popularity and recency-based retrieval by community/block
- Ranking mechanism (L2R or rules+bandit)
- Policy & safety layer
- FastAPI endpoints: /v1/reco/homefeed, /v1/reco/feedback, optional
/v1/reco/explanations
- Documentation and design note
### Test Data
Prepare realistic CSV/JSON files for:
1) users.csv
2) items.csv
3) interactions.csv
These should simulate residents across communities, community content, and engagement
history.
### Technical Requirements
Candidate Generation:
1. Content-based retrieval with embeddings
2. Collaborative filtering
3. Popularity/recency retrieval
Ranking:
- Learning-to-rank model or justified hybrid approach
- Features: similarity scores, recency, tag overlap, popularity, block match
Policy & Safety:
- Community isolation
- Creator frequency caps
- Low-quality content filtering
FastAPI Endpoints:
- GET /v1/reco/homefeed
- POST /v1/reco/feedback
- GET /v1/reco/explanations (optional)
### Deliverables
1) Code repository (with backend, data, migrations, training scripts, tests)
2) README.md (setup, usage, training instructions)
3) Design Note (architecture, privacy & safety considerations)
4) Video recording walkthrough of 5 minutes (to be uploaded via drive and provide the link
in the google form provided in the assessment) covering:
 - Approach
 - Code implementation
 - Scope of scalability in case of real-time production data for the FlatZ app
5) Optional working demo video(to be shared same as walkthrough video)for Bonus
points(duration <=5 minutes)
### Acceptance Tests
- Data load & train must work via documented commands
- Homefeed returns relevant items for a given user
- Feedback changes recommendations after multiple events
- Cold-start users receive sensible recommendations
- Low-quality content is filtered or down-ranked
### Scoring Rubric (100 pts)
- Correctness & Completeness (25)
- Modeling Quality (20)
- Data & Cold-Start Strategy (10)
- Code Quality & Tests (15)
- Performance & Caching (10)
- Github history(pushes and commits)(5)
- Docs & Integration Plan (10)
- Polish & UX (5)
