import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_str = os.environ["SESSION"]
target = os.environ["TARGET"]  # username без @ или ID

client = TelegramClient(StringSession(session_str), api_id, api_hash)

@client.on(events.NewMessage(from_users=target, func=lambda e: e.is_private))
async def handler(event):
    text = event.message.message or ""
    if not text:
        return
    await event.reply(f'Все говорят «{text}», а ты возьми и купи слона')

print("Бот запущен")
client.start()
client.run_until_disconnected()