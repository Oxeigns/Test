import asyncio
from pyrogram import Client, filters
from app import WORDS_TO_SEND, DELAY

# Deploy ke time input maangne ke liye
print("--- Telegram Automation Setup ---")
API_ID = input("Enter API ID: ")
API_HASH = input("Enter API HASH: ")
SESSION_STR = input("Enter Session String (Leave blank if not available): ")

if SESSION_STR.strip() == "":
    # Phone number se login karega agar session string nahi hai
    app = Client("my_account", api_id=API_ID, api_hash=API_HASH)
else:
    # Session string se login karega
    app = Client("my_account", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STR)

is_running = False

@app.on_message(filters.me & filters.text)
async def auto_sender(client, message):
    global is_running
    msg_text = message.text.lower()

    if msg_text == "start":
        if is_running:
            await message.edit("⚠️ Loop is already running!")
            return
        
        is_running = True
        await message.edit("✅ Automation Started!")
        
        while is_running:
            for word in WORDS_TO_SEND:
                if not is_running:
                    break
                await client.send_message(message.chat.id, word)
                await asyncio.sleep(DELAY)

    elif msg_text == "stop":
        is_running = False
        await message.edit("🛑 Automation Stopped.")

print("\nBot is starting...")
app.run()
