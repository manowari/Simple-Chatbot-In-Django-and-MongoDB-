from .qa_utils import answer_question
from .pdf_utils import extract_text_from_pdf
from .relevance_scorer import RelevanceScorer

def qa_result(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        pdf_file = request.FILES['pdf_file']
        additional_contexts = [request.POST.get('additional_context1'), request.POST.get('additional_context2')]

        # Extract text from the PDF file
        context = extract_text_from_pdf(pdf_file)

        # Use BERT to answer the question
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
