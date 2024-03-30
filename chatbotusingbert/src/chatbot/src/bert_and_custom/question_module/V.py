from django.shortcuts import render
from .qa_utils import answer_question
from .pdf_utils import extract_text_from_pdf
from .qa_utils import answer_question
from .pdf_utils import extract_text_from_pdf
from .fuzzy_search import fuzzy_search
from .non_ai_features import find_longest_sentence, count_sentences, find_keywords_in_context
from .relevance_scorer import RelevanceScorer

def qa_result(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        pdf_file = request.FILES['pdf_file']
        enable_profanity_filter = request.POST.get('enable_profanity_filter', False)

        # Filter out profanity from the question if profanity filter is enabled
        if enable_profanity_filter:
            question = filter_profanity(question)   
    
    
    if request.method == 'POST':
        question = request.POST.get('question')
        pdf_file = request.FILES['pdf_file']
        additional_contexts = [request.POST.get('additional_context1'), request.POST.get('additional_context2')]

        # Extract text from the PDF file
        context = extract_text_from_pdf(pdf_file)

        # Fuzzy search
        fuzzy_answer = fuzzy_search(question, context)

        if fuzzy_answer:
            longest_sentence = find_longest_sentence(context)
            num_sentences = count_sentences(context)
            keywords_in_context = find_keywords_in_context(question, context)

            return render(request, 'result.html', {
                'answer': fuzzy_answer,
                'longest_sentence': longest_sentence,
                'num_sentences': num_sentences,
                'keywords_in_context': keywords_in_context
            })

        # Use AI-based search system if enabled
        if request.POST.get('enable_ai'):
            ai_answer = ai_optimized_search(question, context)
            return render(request, 'result.html', {'answer': ai_answer})

        # Default: Use BERT QA system
        bert_answer = answer_question(question, context)

        # Initialize RelevanceScorer and calculate relevance score
        scorer = RelevanceScorer()
        relevance_score = scorer.calculate_relevance_score(bert_answer, context)

        # Define thresholds for relevance score
        if relevance_score < 0.3:  # Low relevance
            cautionary_response = "The relevance score is low. Here's an alternative answer from the extracted data."
            alternative_answer = find_alternative_answer(question, context)
            return render(request, 'result.html', {'answer': cautionary_response, 'alternative_answer': alternative_answer})
        elif relevance_score < 0.7:  # Average relevance
            bert_answer = "BERT Answer: " + bert_answer
            alternative_answer = find_alternative_answer(question, context)
            return render(request, 'result.html', {'answer': bert_answer, 'alternative_answer': alternative_answer})
        else:  # High relevance
            return render(request, 'result.html', {'answer': bert_answer})

    return render(request, 'home.html')

