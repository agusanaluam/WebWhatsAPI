#!/usr/bin/python

import time
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message


driver = WhatsAPIDriver(username="maulana")
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

while True:

    time.sleep(3)
    print('Checking for more messages')
    #print driver.get_unread()
    for contact in driver.get_unread():

        #print contact.messages
        for message in contact.messages:
            #print message.content
            if isinstance(message, Message): # Currently works for text messages only.
                file =open("chatlog.txt", "w")
                file.write(message.sender)
                print message.sender
				print message.safe_name
                print message.content
                #contact.chat.send_message("Sorry this account is under maintenance, please wait, i'll be back")
                file.close()
