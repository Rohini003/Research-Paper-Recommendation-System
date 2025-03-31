from flask import Flask, request, render_template, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load your research paper data
df = pd.read_csv('research_papers.csv')  # Ensure this CSV is correct

# Vectorize the abstracts using TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['Abstract'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend')
def recommend():
    query = request.args.get('query')
    
    if query:
        recommended_papers = recommend_papers(query, df, tfidf_matrix)
        
        # Check if recommendation is empty or None
        if not recommended_papers:  # This checks for both None and empty list
            return jsonify({"message": "Sorry, we couldn't find any results."}), 200
        
        return jsonify(recommended_papers)
    return jsonify({"error": "No query provided"}), 400

def recommend_papers(query, df, tfidf_matrix):
    # Vectorize the query using the same vectorizer
    query_vec = vectorizer.transform([query])
    
    # Calculate cosine similarities between the query and all papers
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    # Get indices of the top 5 most similar papers
    top_indices = similarities.argsort()[-5:][::-1]
    
    # If all similarity scores are zero, return empty results
    if all(similarity == 0 for similarity in similarities):
        return []

    # Return the recommended papers as a list of titles, abstracts, and similarity scores
    recommended = [
        {"title": df.iloc[i]["Title"], "abstract": df.iloc[i]["Abstract"], "similarity": similarities[i]}
        for i in top_indices
    ]
    
    # Check if the recommendations list is empty or None
    if not recommended:
        return []
    
    return recommended

if __name__ == '__main__':
    app.run(debug=True)
