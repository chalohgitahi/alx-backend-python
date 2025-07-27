from django.urls import path
# Import from the new auth.py file
from . import auth 
# Import the rest of the views from views.py
from .views import (
    ConversationListView,
    MessageListView,
    SendMessageView,
)

urlpatterns = [
    # The registration path now points to the view in auth.py
    path('register/', auth.UserRegisterView.as_view(), name='user-register'),
    
    # These paths remain the same
    path('conversations/', ConversationListView.as_view(), name='conversation-list'),
    path('messages/<int:user_id>/', MessageListView.as_view(), name='message-list'),
    path('messages/send/', SendMessageView.as_view(), name='send-message'),
]