import constants, asyncio, markovify

def mscript(command, client, message):

    async def asyncscript(command,client,message):
        await client.send_typing(message.channel)
        messageser = str(message.server.id)
        messagecha = str(message.channel.id)
        corpusFile = "data/"+messageser+"/"+messagecha+".txt"
        corpusRead = open(corpusFile, "r",encoding='utf-8')
        corpusText = corpusRead.read()
        
        corpusModel = markovify.Text(corpusText)
        
        markovString=""
        for i in range(3):
            markovString += str(corpusModel.make_short_sentence(140))
            markovString += " "
            
        constants.run_coro(client.send_message(message.channel, markovString), client)
   
    asyncio.ensure_future(asyncscript(command, client, message))