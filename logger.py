import asyncio, time, os, errno

def log(client, message):
    
    blocked_text = [" .","."," $simulate."] #Must have period at end
    
    async def asyncscript(client, message):
        if str(message.author)=="DiscordSimulator#3905" or str(message.author)=="Discord Simulator Dev#4642":
            pass
        else:
            messagestr = str(message.content)
            messageser = str(message.guild.id)
            messagecha = str(message.channel.id)
    
            if not messagestr.endswith(".") and not messagestr.endswith("!") and not messagestr.endswith("?"):
                messagestr = messagestr+"."
    
            print("Message: ", messagestr)
            print("Server: ", messageser)
            print("Channel: ", messagecha)
    
            if messagestr.lower() in blocked_text:
                pass
            else:
            
                try:
                    os.makedirs("data/"+messageser)
                except OSError as e:
                    if e.errno != errno.EEXIST:
                        raise       
                filename = "data/"+messageser+"/"+messagecha+".txt"
                time.sleep(.05)
                if os.path.exists(filename):
                    print("Appending to existing dataset")
                    corpus = open(filename,"a",encoding='utf-8')
                    corpus.write(messagestr+"\n")
                    corpus.close() 
                else:
                    print("Capturing old messages to fill dataset")
                    oldData=""
                    oldList=[]
                    corpus = open(filename,"w",encoding='utf-8')
                    async for old in message.channel.history(limit=100000):
                        print(old.content)
                        oldList.append(old)
                    
                    for old in oldList:
                        if str(old.author)=="DiscordSimulator#3905" or str(old.author)=="Discord Simulator Dev#4642":
                            pass
                        else:
                            oldstr = str(old.content)                   
                            if not oldstr.endswith(".") and not oldstr.endswith("!") and not oldstr.endswith("?"):
                                oldstr = oldstr+"." 
                                
                            if oldstr.lower() in blocked_text:
                                pass
                            else:
                                oldData = oldData+oldstr+"\n" 
                    corpus.write(oldData)
                    corpus.close()
                 
    asyncio.ensure_future(asyncscript(client, message))