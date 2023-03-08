import discord
import responses

# Sends a message to the user either publicly or privately
async def send_message(message, user_message, private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if private else await message.channel.send(response)

    except Exception as e:
        print(e)

# Runs the discord bot
def run_discord_bot():
    # Insert discord bot token/key here!!!
    TOKEN = ''
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # Indicates when the bot is ready
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    # Waits reacts accordingly when a user sends a message
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, private=True)
        else:
            await send_message(message, user_message, private=False)

    client.run(TOKEN)