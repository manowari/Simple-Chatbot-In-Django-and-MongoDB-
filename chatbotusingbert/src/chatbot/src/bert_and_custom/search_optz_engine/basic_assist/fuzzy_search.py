from fuzzywuzzy import fuzz

def fuzzy_search(question, context, threshold=70):
    # Implement fuzzy search logic
    best_match = None
    best_score = 0

    # Split the context into sentences and search for the best match
    for sentence in context.split('.'):
        score = fuzz.partial_ratio(question.lower(), sentence.lower())
        if score > best_score:
            best_score = score
            best_match = sentence.strip()

    if best_score >= threshold:
        return best_match
    else:
        return None
