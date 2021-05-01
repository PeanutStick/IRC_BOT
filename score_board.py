import pandas as pd
def main(text,channel):
    print("text: "+text)
    user = text.split(":")[1]
    user = user.split("!")[0]# Take the user
    text = text.split("PRIVMSG "+channel+" :")[1]# Take the text
    nbword = len(list(text.split(" ")))# Take the nb of words
    data =  pd.read_csv('score.csv')# red the data from the csv file
    if user in data["Names"].values:
        #print("I will add "+str(nbword)+" points to "+user)
        user = [user] # I convert the string to list, because of panda with isin(user)
#print the row of the collums where the collumn == Names
        data.loc[data['Names'].isin(user), 'Words'] += nbword
        print(data)
        
    else:
        print("create it")
        new_row = {'Names':user,'Words':nbword}# the new row
        data = data.append(new_row, ignore_index=True)# I add it to the data
    data.to_csv(r'score.csv', index = False)# save into csv
    
    #and them put it in CSV file

def top():
    print("here ! ")
    data =  pd.read_csv('score.csv') # Open the CSV
    top3 = data.head(3) # Take 3 fist values
    data_list = top3.values.tolist()# Convert to list

    return data_list


##def me(text):
##    user = text.split(":")[1]
##    user = user.split("!")[0]# Take the user
##    data =  pd.read_csv('score.csv')# Open the CSV
##    data.loc[data['Names'] == user]
##    print(data)
##    print(data[['Words']])
##    #data_list = top3.values.tolist()
##    #print(data_list[0][1])
##
##    return score



if __name__ == "__main__":
    main(text,channel)

