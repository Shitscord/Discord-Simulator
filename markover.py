async def mscript(command, client, message):
    import markovify, constants
    async def get_logs_from(channel):
        async for m in client.logs_from(channel):
            print(m.clean_content)
    get_logs_from(message.channel)