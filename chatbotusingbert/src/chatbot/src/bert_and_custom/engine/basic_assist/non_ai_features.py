def find_longest_sentence(context):
    # Find the longest sentence in the context
    sentences = context.split('.')
    longest_sentence = max(sentences, key=len)
    return longest_sentence.strip()

def count_sentences(context):
    # Count the number of sentences in the context
    sentences = context.split('.')
    return len(sentences)

def find_keywords_in_context(question, context):
    # Find keywords from the question in the context
    keywords = []
    for word in question.split():
        if word.lower() in context.lower():
            keywords.append(word)
    return keywords
