from discord.ext import commands
import discord, constants, tokens, markover, asyncio


Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")  # When Bot Connects

@client.event
async def on_message(message):
    if message.content.upper().startswith('!MARKOVIFY'):
        print("Beginning Markovify")
        command = message.content.split(" ")
       
        loop = asyncio.get_event_loop()
        loop.run_until_complete(markover.mscript(command, client, message))

client.run(tokens.discord)

# To send message: constants.run_coro(client.send_message(message.channel, "message"), client)