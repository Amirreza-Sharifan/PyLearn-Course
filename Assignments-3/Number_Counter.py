while 1==1:
    sentence = input("Please type your sentence or exit for ending: ")
    if sentence == "exit":
        break
    else:
        words = sentence.split()
        word_count = len(words)
        print("the number of words in your sentence is:", word_count)