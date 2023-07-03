from django.urls import path, include
from .views import RoomDetailView,RoomListView,NewMessage,MessageListView
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:room_id>/', consumers.ChatConsumer.as_asgi()),
]

urlpatterns = [ 
    # Include the WebSocket URL pattern
    path('', include(websocket_urlpatterns)),
    path('rooms/<int:pk>', RoomListView.as_view(), name='rooms'),
    # path('rooms/<int:room_id>/', RoomDetailView.as_view(), name='room-detail'),
    
    
    
    path('messages/<int:room_id>', MessageListView.as_view(), name='messages'),
    path('new_messages', NewMessage.as_view(), name='new_messages')
    
    
    # path('rooms/<int:room_id>/messages/<int:message_id>/', MessageDetailView.as_view(), name='message-detail'),

 
]
