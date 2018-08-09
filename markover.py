import constants, asyncio, recursivemarkov

def mscript(command, client, message):
    mlist=[]
    
    
    async def asyncscript(command,client,message):
        async def get_logs_from(channel):
            async for m in client.logs_from(channel):
                mstr=str(m.clean_content)
                mauthor=str(m.author)
                if mauthor=="DiscordSimulator#3905" or mauthor=="Discord Simulator Dev#4642":
                    print("DiscordSim Message. Skipping")
                else:
                    if mstr.endswith("."):
                        mlist.append(mstr)
                    else:
                        mstr=mstr+"."
                        mlist.append(mstr)
            print(mlist)
        await get_logs_from(message.channel)
        mfullstr=str(" ".join(str(s) for s in mlist))
        mlistlen=len(mlist)
        markov_final = recursivemarkov.recursive_markov(mfullstr,mlistlen)


        print(markov_final)
        constants.run_coro(client.send_message(message.channel, str(markov_final)), client)
    
    asyncio.ensure_future(asyncscript(command, client, message))