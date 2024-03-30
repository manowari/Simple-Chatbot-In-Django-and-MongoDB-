
'''
plans to handle routine tasks 
'''

from django.shortcuts import render
from .qa_utils import answer_question
from .pdf_utils import extract_text_from_pdf

def home(request):
    return render(request, 'home.html')