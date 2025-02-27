from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

# step 0: load our token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

# step 1: Bot setup
intents = Intents.default()
intents.message_content = True  # NOQA
client = Client(intents=intents)


# Step 2: message functionnality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print(
            '( "message was empty because intents were not enabled probably")'
        )
        return

    is_private = user_message[0] == "$"
    if is_private:
        user_message = user_message[1:]

    try:
        response = get_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        await message.channel.send(f"An error occurred: {e}")
        print(e)


# Step 3: HANDLING THE STARTUP FOR OUR BOT


@client.event
async def on_ready() -> None:
    print(f"{client.user} has connected to Discord!")


# Step 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    await send_message(message, message.content)

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f"{username} in {channel} sent: {user_message}")


def get_response(user_message: str) -> str:
    # Dummy implementation of get_response function
    return f"Response to: {user_message}"


# step 5: MAIN ENTRY POINT
def main() -> None:
    client.run(TOKEN)


main()
