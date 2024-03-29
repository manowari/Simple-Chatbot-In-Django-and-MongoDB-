from django.shortcuts import render
from .models import ChatMessage

def chat_history(request):
    chat_messages = ChatMessage.objects.all()
    return render(request, 'chat_history.html', {'chat_messages': chat_messages})
