from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
from course.models import Course
from account.models import User

class RoomListView(APIView):
    def get(self, request,pk):
        rooms = Room.objects.get(course=pk)
        serializer = RoomSerializer(rooms)
        return Response(serializer.data)
    # def post(self, request):
    #     serializer = RoomSerializer(data=request.data)
    #     if serializer.is_valid():
    #         room = serializer.save()
    #         return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomDetailView(APIView):
    def get(self, request, room_id):
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response({"error": "Room not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    # Add logic for updating and deleting a room if needed
    

class MessageListView(APIView):
    def get(self, request, room_id):
        messages = Message.objects.filter(room=room_id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class NewMessage(APIView):
#     def get(self, request, room_id):
#         print(room_id)
#         try:
#             room = Room.objects.get(id=room_id)
#         except Room.DoesNotExist:
#             return Response({"error": "Room not found."}, status=status.HTTP_404_NOT_FOUND)
#         messages = room.messages.all()
#         serializer = MessageSerializer(messages, many=True)
#         return Response(serializer.data)

    def post(self, request):
        room = request.data.get('room')
        author = request.data.get('author')
        content = request.data.get('content')
        current_user = User.objects.get(id=author)
        
        print("sended roomid:",room)
        try:
            room = Room.objects.get(id=room)
        except Room.DoesNotExist:
            return Response({"error": "Room not found."}, status=status.HTTP_404_NOT_FOUND)
        
        message = Message.objects.create(room=room,
                                    author=current_user,
                                    content=content,)

        serializer = MessageSerializer(message)
        
        messages = Message.objects.filter(room=room)
        serializer1 = MessageSerializer(messages, many=True)
        return Response(serializer1.data)


class MessageDetailView(APIView):
    def get(self, request, room_id, message_id):
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response({"error": "Room not found."}, status=status.HTTP_404_NOT_FOUND)
        try:
            message = room.messages.get(id=message_id)
        except Message.DoesNotExist:
            return Response({"error": "Message not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = MessageSerializer(message)
        return Response(serializer.data)
