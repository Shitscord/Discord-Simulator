import asyncio, time, os, errno

def log(message):
    
    blocked_text = [" .",".","$simulate"]
    
    async def asyncscript(message):
        if str(message.author)=="DiscordSimulator#3905" or str(message.author)=="Discord Simulator Dev#4642":
            pass
        else:
            messagestr = " "+str(message.content)
            messageser = str(message.server.id)
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
                    append_write = 'a'
                else:
                    append_write = 'w'
                
                corpus = open(filename,append_write)
                corpus.write(messagestr)
                corpus.close()                  

    asyncio.ensure_future(asyncscript(message))