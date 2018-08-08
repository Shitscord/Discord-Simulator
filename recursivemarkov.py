def recursive_markov(markovstring,markovcount): #Markov count is # of iterations
    import markovify
    while True:
        gencount=1
        x=0
        y=True
        while y:
            model_text=markovify.Text(markovstring)
            strlist=[]
            for i in range(markovcount):
               strapp=model_text.make_sentence()
               strlist.append(strapp)   
            markovstring=str(" ".join(str(s) for s in strlist))
            print()
            print("Generation",str(gencount)," Complete")
            print()
            x=x+1
            gencount=gencount+1
            markovcount=markovcount-5
            if markovcount==10 or markovcount<=10:
                y=False
        model_text=markovify.Text(markovstring)
        finalstr=model_text.make_sentence()
        print(finalstr)
        input()