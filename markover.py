import constants, asyncio, markovify, random, json

def mscript(command, client, message):

    async def asyncscript(command,client,message):
        await client.send_typing(message.channel)
        
        #Randomly select 1 of 48 pieces of wikipedia corpus to include for extra entropy
        wikinum=random.randint(1,1500)
        wikicorpus="json/"+str(wikinum)+".txt.json"
        print(wikicorpus)
        with open(wikicorpus) as jsonFile:
            wikicorpjson=json.load(jsonFile)
        wikiimport=markovify.Text.from_json(wikicorpjson)
        
        #Get message channel and server and read/analyze contents of log
        messageser = str(message.server.id)
        messagecha = str(message.channel.id)
        discordText = open("data/"+messageser+"/"+messagecha+".txt", "r",encoding='utf-8').read()
        discordChain = markovify.Text(discordText, state_size=3)
        
        
        
        corpusModel = markovify.combine([discordChain, wikiimport], [3,.25])
        
        markovString=""
        for i in range(3):
            markovString += str(corpusModel.make_short_sentence(140))
            markovString += " "
            
        constants.run_coro(client.send_message(message.channel, markovString), client)
   
    asyncio.ensure_future(asyncscript(command, client, message))