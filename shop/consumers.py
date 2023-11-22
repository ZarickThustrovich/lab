import os
import django
# django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lab.settings')

import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync




def set_session_state(session_uuid, is_active):
    from .models import Sessions
    current_session = Sessions.objects.get(session_uuid=session_uuid)
    current_session.is_active = is_active
    current_session.save()




class ChatConsumer(WebsocketConsumer):
    def connect(self):
        from .models import Sessions
        self.room_name = self.scope["url_route"]["kwargs"]["session_uuid"]
        self.room_group_name = "chat_%s" % self.room_name
        current_session, created = Sessions.objects.get_or_create(session_uuid=self.room_name)
        if (created):
            current_session.is_active = True
            current_session.save()
        else:
            set_session_state(self.room_name, True)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        set_session_state(self.room_name, False)
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))