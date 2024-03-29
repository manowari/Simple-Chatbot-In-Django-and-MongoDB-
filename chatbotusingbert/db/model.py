from .models import ChatMessage

def save_chat_message(user, message):
    chat_message = ChatMessage(user=user, message=message)
    chat_message.save()

def get_chat_history():
    return ChatMessage.objects.all()
