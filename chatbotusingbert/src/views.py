from django.shortcuts import render
from .qa_utils import answer_question
from .pdf_utils import extract_text_from_pdf

def home(request):
    return render(request, 'home.html')

def qa_result(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        pdf_file = request.FILES['pdf_file']
        context = extract_text_from_pdf(pdf_file)

        answer = answer_question(question, context)
        return render(request, 'result.html', {'answer': answer})

    return render(request, 'home.html')
