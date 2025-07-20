from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

# The router will automatically generate the URLs for the ConversationViewSet
#router = DefaultRouter()
router.DefaultRouter().register(r'conversations', ConversationViewSet, basename='conversation')

# We need a custom URL for the nested MessageViewSet
message_list = MessageViewSet.as_view({'get': 'list', 'post': 'create'})

urlpatterns = [
    path('', include(router.urls)),
    path(
        'conversations/<int:conversation_pk>/messages/',
        message_list,
        name='conversation-messages'
    ),
]