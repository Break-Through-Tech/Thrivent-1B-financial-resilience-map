# Understanding Musical Similarity: Building a Feature-Based Recommendation System with Graph-Based Interpretability

**Company / Org:** Thrivent   
**Challenge Advisor:** Nathan Rickert, naterick12@gmail.com   
**AI Studio Coach:** Julio Contreras, Julio.Contreras@breakthroughtech.org   
**Program:** Break Through Tech AI Studio - Fall 2026

---

## 🎯 The Challenge

### Project Summary
In this project, you will use audio feature data from 1.2M Spotify songs (e.g., danceability, energy, tempo, valence, acousticness, etc.) and machine learning techniques such as feature engineering, K-Nearest Neighbors, logistic regression, decision trees, clustering, and model evaluation methods to build and evaluate a music similarity and recommendation system that predicts and ranks similar songs based on audio characteristics. This will help a music streaming company (like Spotify) address the challenge of improving music discovery and understanding how song characteristics influence perceived similarity in recommendation systems.

### Success Criteria

Recommendation quality:   
- Precision@K	How many of the top K recommendations are relevant
- Recall@K	How many relevant songs were successfully retrieved
- F1@K	Balance of precision and recall
- NDCG@K	Rewards putting the most relevant songs higher in the ranking
- MAP@K	Ranking quality across multiple relevant songs	Useful
- Hit Rate@K	Whether at least one relevant song appears in top K	Useful

Model performance:   
- Comparison across KNN vs LR vs tree-based models
- Feature importance interpretability

Structural insight:   
- Whether graph structure improves interpretability of recommendations
- Whether clusters align with known musical groupings
 
### Stretch Goals

- Add PCA or UMAP visualization of song space
- Experiment with different distance metrics (cosine vs euclidean vs weighted features)
- Build interactive “song explorer” notebook
- Compare clustering vs graph communities quantitatively
  
### Project Milestones

| Month | Milestone | Key Activities |
|---|---|---|
| September | Data Understanding & Baseline Modeling | • Perform EDA (distributions, correlations, missingness)<br>• Engineer normalized feature set<br>• Build baseline similarity system |
| October | Model Comparison & Structured Similarity | • Train and compare ML models<br>• Introduce clustering (KMeans or DBSCAN)<br>• Compare clustering results vs known metadata (genre/artist) |
| November | Graph Interpretation & Final System | • Analyze song similarity graph using NetworkX:<br>• Compare graph-based neighborhoods vs feature-based recommendations<br>• Finalize recommendation system pipeline: |

> **Note for the team:** Please create a GitHub Projects board in this repository to break these milestones into weekly tasks. Go to the **Projects** tab → **New project** → Choose **Board** → Add columns for each month.

---

## 📊 Dataset

**Name and Source:** Audio feature data from Spotify  
**Format:** CSV/TSV  
**Size:** under 1gb  
**Location:** https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs

### Key Details
- The file tracks_features.csv (file too big to upload to git) contains audio features for over 1.2 million songs, obtained with the Spotify API.
- 24 Columns
- Dataset contains binary, text, and numerical features

---

## 🛠️ Suggested Approach

**ML Problem Type:** Classification,Regression,Clustering,Recommendation Systems,Graph-based data analysis / similarity modeling

**Recommended Libraries:**
- scikit-learn
- pandas / polars
- FAISS
- scikit-surprise
- yellowbrick
- umap-learn

---

## 📚 Resources to Get Started

## Background Reading
- [Google: Recommendation Systems](https://developers.google.com/machine-learning/recommendation) — Beginner-friendly introduction to how recommendation systems work.
- [IBM: Recommendation Engines](https://www.ibm.com/think/topics/recommendation-engine) — Overview of how recommendation systems are used in real-world applications.

## Technical Tutorials
- [Kaggle: Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) — Interactive introduction to core ML concepts used in the project.
- [Scikit-learn: Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html) — Tutorial and documentation for KNN and similarity-based approaches.
- [Scikit-learn: Clustering](https://scikit-learn.org/stable/modules/clustering.html) — Introduction to clustering and unsupervised learning.

---

## 🤝 How We'll Work Together

**Official check-ins:** During our biweekly 45-minute AI Studio Lab Section meeting block (2nd and 4th week of every month)

 **Other ways to reach out to me with questions:** 
* email: naterick12@gmail.com; discord: nathanrickert
* Note: I will aim to respond within 48 hours. Please reach out to your AI Studio Coach with urgent questions.

**Recommended free coding / collaboration tools**
* Google Colab
  
---

## 🚀 Getting Started

1. **Review this overview document** and note any questions for our first meeting
2. **Begin Exploring the Data!!** using the link above
3. **Read more on technical concepts that look unfamiliar**

I’m excited to work with you!

---

## ❓ Questions?

Please bring any questions to our first meeting during the week of August 24th (Break Through Tech’s Bridge to Studio - Session C). 
