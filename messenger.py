from fbchat import Client
from fbchat.models import*
from getpass import getpass
email = str(input("Email:"))
password = str(input("Password:"))
client = Client('email','password')
no_of_friends = str(input("Enter Number of friends:"))
for i in range(no_of_friends):
    name = str(input("Name:"))
    friends = client.searchForUsers(name)  # return a list of names
    friend = friends[0]
    msg =str(input("Msg:"))
    sent = client.send(Message(text=msg), thread_id=friend.uid, thread_type=ThreadType.USER)
    if sent:
        print("Message sent successfully!")