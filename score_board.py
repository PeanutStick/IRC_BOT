def main(text,channel):
    print("text: "+text)
    user = text.split(":")[1]
    user = user.split("!")[0]
    print(user)# Take the user
    text = text.split("PRIVMSG "+channel+" :")[1]
    print(text)
    nbword = len(list(text.split(" ")))
    print(nbword)# count the number of words

    #and them put it in CSV file
if __name__ == "__main__":
    main(text,channel)

