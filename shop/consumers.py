import json
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import os
from asgiref.sync import sync_to_async
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab.settings")





@sync_to_async
def get_value_from_database():
    from shop.models import Counter
    update_database_value()
    return Counter.objects.get(id=1).value


@sync_to_async
def update_database_value():
    from shop.models import Counter
    counter = Counter.objects.filter(id=1)
    return Counter.objects.filter(id=1).update(value=int(counter[0].value) + 1)







class YourConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.accept()
        

        # запускаем цикл для отправки данных каждую секунду
        # while True:
        await asyncio.sleep(1)
        await update_database_value()
        counter = await get_value_from_database()
        data = {"counter": counter}
        await self.send(json.dumps(data))
        await asyncio.sleep(1)





    async def disconnect(self, close_code):
        print('disconnected ws')
        pass

    async def receive(self):
        print('received ws')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))