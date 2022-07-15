import asyncio, os, random, string, csv, traceback
from http import client
import array as arr
from multiprocessing import Process
import time, urllib.request
from email.message import Message
from pyexpat.errors import messages
from telethon.tl.types import InputMessagesFilterPhotos
from telethon import TelegramClient
from time import sleep
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon import TelegramClient, connection, sync, functions
#from telethon.

def main():
    api_id = '9711828'
    api_hash = '09ee6b9d9dad99b9470fcbbdea601785'
    i = 0
    f = open(r'C:\Users\PC\OneDrive\Documents\Data\Full_Acc_Tele\Session\phone.txt','r')
    #while i < 18:
        #f.readline().strip()
        #i+=1
    while i < 30:
        phone = f.readline().strip()
        try:
            Cal = TelegramClient(phone, api_id, api_hash)
            Cal.connect()
            sleep(random.randint(3,4))
            if not Cal.is_user_authorized(): 
                print('Error Author lỗi:',phone)
                sleep(random.randint(5,7))
                Cal.disconnect()
            else:
                try:
                    sleep(random.randint(5,7))
                    Cal(JoinChannelRequest('plaiddaoglobal'))
                    sleep(random.randint(5,7))
                    Cal.send_message('plaiddaoglobal','hello')
                    sleep(random.randint(5,7))
                    #Cal.send_message('bemike2k5','hello')
                    #Cal.edit_2fa
                    Cal.disconnect()
                    print('Done Acc: ', i)
                    i+=1
                except:
                    print("Error fuck", phone)
                    Cal.disconnect()
                    i+=1
        except: 
            print("Error Client", phone)
            i +=1


if __name__ == "__main__": main()
