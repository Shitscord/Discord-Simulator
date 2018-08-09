from discord.ext import commands
import discord, tokens, markover


Client = discord.Client()
client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")  # When Bot Connects

@client.event
async def on_message(message):
    if message.content.upper().startswith('$SIMULATE'):
        print("Beginning Markovify")
        command = message.content.split(" ")
        markover.mscript(command, client, message)

client.run(tokens.discord)

