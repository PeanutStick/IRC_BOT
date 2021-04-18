# Import some necessary libraries.
import socket, ssl
 
# Some basic variables used to configure the bot
server = 'irc.evilcorp.ga' # Server
port = 6697 # Port
channel = "#lobby" # Channel
botnick = "Dovahkiin" # Your bots nick
user = botnick + " " + botnick + " " + botnick + " " + "a simple irc bot written in python" #This is username, hostname, identity and description in the order

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
        import yt_title as title
        buff = buff.split("watch?v=")
        buff = buff[1]
        try:
                buff = buff.split("&list")
        except:
                print("not a list")
        try:
                buff = buff.split("?t=")
        except:
                print("not shared with time code")
        
        ytidd=buff[0] #I should grep btw "watch?v=" and if isset "&list" or "?t="
        
        
        #ytidd="dQw4w9WgXcQ"
        ircsend("PRIVMSG "+ channel +" :Title: "+title.main(ytidd)+"\r\n")

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

    if ircbuff.find("NOTICE " + botnick + " :*** You are connected to") != -1: #If connected successfully, do the below functions and codes.
        joinchan(channel) # Join the channel using the functions we previously defined

    #if ircbuff.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
    #    hello()
    if ircbuff.find("coffee") != -1: # Bring you a coffee
        coffee()
    if ircbuff.find("watch?v=") != -1: #https://www.youtube.com/watch?v=pxcI5g2iUCg
        yt_title(ircbuff)
        

    del ircbuff	#This will clear out the server incoming buffer so that it can be reused for upcoming buffer.
