import constants, asyncio, markovify, time

def mscript(command, client, message):
    mlist=[]

    
    async def asyncscript(command,client,message):
        async def get_logs_from(channel):
            async for m in client.logs_from(channel):
                mstr=str(m.clean_content)
                mauthor=str(m.author)
                if mauthor=="DiscordSimulator#3905" or mauthor=="Discord Simulator Dev#4642":
                    pass
                else:
                    if mstr.endswith("."):
                        mlist.append(mstr)
                    else:
                        mstr=mstr+"."
                        mlist.append(mstr)
                        
                        
        await get_logs_from(message.channel)
        mfullstr=str(" ".join(str(s) for s in mlist))
        
        x=True
        while x:
            final_gen=markovify.Text(mfullstr)
            final_sent=final_gen.make_sentence()
            time.sleep(.0025)
            if "None" not in str(final_sent):
                print(final_sent)
                x=False
            else:
                print("None")          
        constants.run_coro(client.send_message(message.channel, str(final_sent)), client)
    
    asyncio.ensure_future(asyncscript(command, client, message))