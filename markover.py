import constants, asyncio, markovify, recursivemarkov

def mscript(command, client, message):
    mlist=[]
    
    
    async def asyncscript(command,client,message):
        async def get_logs_from(channel):
            async for m in client.logs_from(channel):
                mstr=str(m.clean_content)
                if mstr.endswith("."):
                    mlist.append(mstr)
                else:
                    mstr=mstr+"."
                    mlist.append(mstr)
        await get_logs_from(message.channel)
        mfullstr=str(" ".join(str(s) for s in mlist))
        mlistlen=len(mlist)
        markov_final = recursivemarkov.recursive_markov(mfullstr,mlistlen)
        
        #model_text=markovify.Text(mfullstr)
        #markov_final=model_text.make_sentence()

        constants.run_coro(client.send_message(message.channel, str(markov_final)), client)
    asyncio.ensure_future(asyncscript(command, client, message))