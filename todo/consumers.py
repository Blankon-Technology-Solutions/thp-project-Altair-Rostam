import json

from channels.generic.websocket import AsyncWebsocketConsumer


class TodoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join todo group
        await self.channel_layer.group_add("todo_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave todo group
        await self.channel_layer.group_discard("todo_updates", self.channel_name)

    async def todo_update(self, event):
        # Send todo update to the client
        await self.send(text_data=json.dumps(event["data"]))

    async def update_todos(self, event):
        # Send updated todos to connected clients
        await self.channel_layer.group_send(
            "todo_updates", {"type": "todo_update", "data": event["data"]}
        )
