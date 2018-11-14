from discord.ext import commands
import discord, tokens, markover, logger, os


Client = discord.Client()
client = commands.Bot(command_prefix="")

if not os.path.exists("data"):
    os.makedirs("data")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")  # When Bot Connects

@client.event
async def on_message(message):
    logger.log(client, message)
    if message.content.upper().startswith('$SIMULATE'):
        print("Beginning Markovify")
        command = message.content.split(" ")
        markover.mscript(command, client, message)

client.run(tokens.discord)

