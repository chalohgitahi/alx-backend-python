
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message
from .serializers import MessageSerializer, UserSerializer # We still need UserSerializer for the conversation list

# Note: UserRegisterView has been moved to auth.py

# 1. View to list all conversations for the logged-in user
class ConversationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        messages = Message.objects.filter(Q(sender=user) | Q(receiver=user))
        
        participants = set()
        for msg in messages:
            if msg.sender == user:
                participants.add(msg.receiver)
            else:
                participants.add(msg.sender)

        user_serializer = UserSerializer(list(participants), many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

# 2. View to get messages between the logged-in user and another user
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view returns a list of all the messages between the logged-in
        user and the user specified by the `user_id` in the URL.
        This remains the most secure and efficient way to handle permissions
        for a list view, as it filters at the database level.
        """
        user = self.request.user
        other_user_id = self.kwargs['user_id']
        return Message.objects.filter(
            (Q(sender=user) & Q(receiver_id=other_user_id)) |
            (Q(sender_id=other_user_id) & Q(receiver=user))
        )

# 3. View to send a message
class SendMessageView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # The sender is automatically set to the logged-in user.
        serializer.save(sender=self.request.user)