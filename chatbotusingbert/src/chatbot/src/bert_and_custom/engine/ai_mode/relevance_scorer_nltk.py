import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class RelevanceScorer:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def calculate_relevance_score(self, bert_answer, context):
        # Tokenize and lemmatize the words in BERT answer and context
        bert_tokens = [self.lemmatizer.lemmatize(token.lower()) for token in word_tokenize(bert_answer) if token.lower() not in self.stop_words]
        context_tokens = [self.lemmatizer.lemmatize(token.lower()) for token in word_tokenize(context) if token.lower() not in self.stop_words]

        # Calculate Jaccard similarity between BERT answer and context
        bert_set = set(bert_tokens)
        context_set = set(context_tokens)
        intersection = bert_set.intersection(context_set)
        union = bert_set.union(context_set)
        relevance_score = len(intersection) / len(union)

        return relevance_score
