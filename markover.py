import constants, asyncio, markovify, time

def mscript(command, client, message):

    async def asyncscript(command,client,message):
        await client.send_typing(message.channel)
        messageser = str(message.server.id)
        messagecha = str(message.channel.id)
        corpusFile = "data/"+messageser+"/"+messagecha+".txt"
        corpusRead = open(corpusFile, "r")
        corpusText = corpusRead.read()
        print(corpusText)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    asyncio.ensure_future(asyncscript(command, client, message))