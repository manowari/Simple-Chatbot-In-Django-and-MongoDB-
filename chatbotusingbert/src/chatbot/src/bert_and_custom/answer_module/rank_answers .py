from .qa_utils import answer_question
from .pdf_utils import extract_text_from_pdf
from .relevance_scorer import RelevanceScorer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_similarity(bert_answer, context):
    # Convert the strings into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([bert_answer, context])

    # Calculate cosine similarity between the vectors
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    # Cosine similarity matrix will be a 2x2 matrix
    # The similarity score is at index [0, 1] or [1, 0]
    similarity_score = similarity_matrix[0, 1]

    return similarity_score

 



def rank_answers(bert_answer, additional_contexts):
    ranked_answers = []

    # Apply custom logic to rank answers based on additional context
    for context in additional_contexts:
        # Implement your custom logic here (e.g., similarity scoring)
        relevance_score = calculate_similarity(bert_answer, context)
        ranked_answers.append((bert_answer, relevance_score))

    # Sort answers based on relevance score
    ranked_answers.sort(key=lambda x: x[1], reverse=True)
    
    return ranked_answers
