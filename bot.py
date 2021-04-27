# Import some necessary libraries.
import socket, ssl, threading
 
# Some basic variables used to configure the bot
server = 'irc.evilcorp.ga' # Server
port = 6697 # Port
channel = "#lobby" # Channel
botnick = "Dovahkiin" # Your bots nick
password = "sjcur5!"
user = botnick + " " + botnick + " " + botnick + " " + "HODL !" #This is username, hostname, identity and description in the order

def ircsend(msg): #I had to make another function for send() because in python3 and above the socket incoming and outgoing messages are in bytes format. So you have to encode and decode it accordingly.
        ircsock.send(msg.encode('utf-8'))

def ping(ircbuff): # This is our first function! It will respond to server Pings.
        pongReply = ircbuff.split(':',1)[-1]	#This strips out ping reply and server name for pong. If not defined it can cause the bot to break in some servers
        ircsend("PONG :" + pongReply + '\r\n')
 
def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
        ircsend("PRIVMSG "+ chan +" :"+ msg +"\r\n")
 
def joinchan(chan): # This function is used to join channels.
        ircsend("JOIN "+ chan +"\r\n")
 
def hello(): # This function responds to a user that inputs "Hello Mybot"
        ircsend("PRIVMSG "+ channel +" :Hello!\r\n")
def coffee(): # This function responds to a user that inputs "Hello Mybot"
        ircsend("PRIVMSG "+ channel +" :  ,--.\r\n")
        ircsend("PRIVMSG "+ channel +" : C|<3| Here is your coffee !\r\n")
        ircsend("PRIVMSG "+ channel +" :  `=='\r\n")
  
def yt_title(buff): # This function responds to a user that inputs "Hello Mybot"
        import yt_title as title#https://youtu.be/Ss6qf7VbWqI?t=442
        buff = buff.split("watch?v=")
        buff = buff[1]
        print("after the watch?v="+buff)
        if "&list" in buff:
                buff = buff.split("&list")
                print("after the &list"+str(buff))
        elif "&t=" in buff:
                buff = buff.split("&t=")
                print("after the &t="+str(buff))
        


        ytidd=buff
        print(ytidd)
        ircsend("PRIVMSG "+ channel +" :Title: "+title.main(ytidd)+"\r\n")
        
def soundcloud_title(buff): # This function responds to a user that inputs "Hello Mybot"
        import soundcloud_title as title
        buff = buff.split("https://soundcloud.com")
        cloudlink = "https://soundcloud.com"+buff[1]
        ircsend("PRIVMSG "+ channel +" :Title: "+title.main(cloudlink)[0]+" Artist: "+title.main(cloudlink)[1]+"\r\n ")
def crypto(buff): # This function responds to a user that inputs "Hello Mybot"
        import market_cap as price
        buff = buff.split("$")[1]
        if " " in buff:
                buff = buff.split(" ")[0]
        print(buff)
        ircsend("PRIVMSG "+ channel +" :"+buff+": "+price.main(buff)+"  \r\n ")
def translat(ircbuff):
        import translator as tr
        text = ircbuff.split("PRIVMSG "+ channel +" :")[1] # to get only the text
        translate = tr.main(text) # he try to translate 
        if translate: # if he can translate
                ircsend("PRIVMSG "+ channel +" :"+str(translate)+"  \r\n ") # he send the message

                

socketHandler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#Opening up a normal socket.

socketHandler.connect((server,port))						#Binding socket to socket address(server ip and port).

ircsock = ssl.wrap_socket(socketHandler)					#Wraping the socket with ssl.

ircbuff = ircsock.recv(2048).decode('utf-8') #Receive buffer from the server.
        
ircbuff = ircbuff.strip('\r\n') # removing any unnecessary linebreaks.
print(ircbuff)	#Printing buffer for once.
del ircbuff	#Deleting buffer for re-use.

ircsend("NICK "+ botnick +"\r\n") # here we actually assign the nick to the bot
print("Sending Nick " + botnick + " to server")

ircsend("USER "+ user + "\r\n") # user authentication
print("Sending UserName and hostname and identity and description \"" + user + "\" to server")


while 1: # Be careful with these! it might send you to an infinite loop
    ircbuff = ircsock.recv(2048).decode('utf-8') #Receive buffer from the server.
    ircbuff = ircbuff.strip('\r\n') # removing any unnecessary linebreaks.
    print(ircbuff)	#Here we print the buffer from the server.
    if ircbuff.find("PING :") != -1: # if the server pings us then we've got to respond!
        ping(ircbuff)
    elif ircbuff.find("NOTICE " + botnick + " ::This nickname is registered") != -1:
        ircsend("/msg NickServ IDENTIFY "+password)
                
        
    elif ircbuff.find("NOTICE " + botnick + " :*** You are connected to") != -1: #If connected successfully, do the below functions and codes.
        joinchan(channel) # Join the channel using the functions we previously defined
        
    #if ircbuff.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
    #    hello()
    elif ircbuff.find("coffee") != -1: # Bring you a coffee
        coffee()

    elif ircbuff.find("$") != -1: # Bring you a coffee
        cryptothread = threading.Thread(target=crypto, args=(ircbuff,))
        cryptothread.start()
        #crypto(ircbuff)
        
    elif ircbuff.find("watch?v=") != -1: #https://www.youtube.com/watch?v=pxcI5g2iUCg
        ytthread = threading.Thread(target=yt_title, args=(ircbuff,))
        ytthread.start()
        #yt_title(ircbuff)
        
    elif ircbuff.find("https://soundcloud.com") != -1: #https://www.youtube.com/watch?v=pxcI5g2iUCg
        soundcloud_title(ircbuff)
    elif ircbuff.find("PRIVMSG "+ channel +" :") != -1:
        print("beffor thread")
        trthread = threading.Thread(target=translat, args=(ircbuff,))
        trthread.start()
        #translat(ircbuff)
        
    
    
    del ircbuff	#This will clear out the server incoming buffer so that it can be reused for upcoming buffer.


    #1 add a certain code to check whether the ssl connection is still active
    #  if not break the loop
    #2 create a tread to lunch my function 



    
    
