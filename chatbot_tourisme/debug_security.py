#!/usr/bin/env python3
"""Debug security question matching"""

from pathlib import Path
from src.chatbot import TunisiaChatbot
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

data_path = Path(__file__).parent / 'data' / 'tunisia_tourism_data.json'
chatbot = TunisiaChatbot(str(data_path))

# Test the security question
question = "La Tunisie est-elle sûre pour les touristes?"
print(f"Question: {question}")

# Check TF-IDF matching directly
print("\n" + "="*60)
print("TF-IDF Similarity Scores:")
print("="*60)

user_vector = chatbot.tfidf_vectorizer.transform([question.lower()])
similarities = cosine_similarity(user_vector, chatbot.tfidf_matrix)[0]

for i, (q, a) in enumerate(chatbot.faq_database):
    print(f"\nScore: {similarities[i]:.4f} - Question: {q}")
    
best_idx = np.argmax(similarities)
best_score = similarities[best_idx]
print(f"\n{'='*60}")
print(f"BEST MATCH (Score: {best_score:.4f})")
print(f"Question: {chatbot.faq_database[best_idx][0]}")
print(f"Answer: {chatbot.faq_database[best_idx][1][:100]}...")

print(f"\n{'='*60}")
print(f"Chatbot Response:")
print(f"\nRéponse: {chatbot.chat(question)}")

