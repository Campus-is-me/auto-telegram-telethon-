#Made by Campus
#Contact for work or feedback to Telegram: @TokudaJav or Zalo: 0337176055
#Simple Tool
import asyncio, os, random, string, csv, traceback, subprocess
from re import sub
#from asyncio import subprocess
import array as arr
from ntpath import join
from multiprocessing import Process
import time, urllib.request
from email.message import Message
from pyexpat.errors import messages
from telethon.tl.types import InputMessagesFilterPhotos
from telethon import TelegramClient
from time import sleep
from anticaptchaofficial.imagecaptcha import *
from telethon.tl.functions.messages import StartBotRequest
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon import TelegramClient, connection, sync, functions

#open file 
def open_file(link_file):
    with open(link_file,'r') as f:
        list = f.readlines()
    list_file = []
    for i in list:
        list_file.append(i.strip())
    return list_file

#def wait
def wait(Client,botID,check):

    time.sleep(random.randint(1,2))
    for i in range(0, 9):
        tmp = Client.get_messages(botID)
        if str(tmp[0].message).find(check) != -1:
            return True
        else:time.sleep(5)

    Client.disconnect()
    return False
#Solution
def task(botid,wallet): 
    api_id = "10584694"
    api_hash = "ec53cb270aa9b7de130a93f5ed71628d"
    phone = "+84568248860"
    Client = TelegramClient(phone,api_id,api_hash)
    Client.connect()
    if not Client.is_user_authorized(): return False
    else:
        print("Start Add Wallet")
        k = 1
        try:
            Client.send_message(botid,"/start")
                
            if not wait(Client,botid,"welcome on board!"): return False
            Client.get_messages(botid)[0].click(text = "➕ Add wallet")

            for i in range(128, 399):
                if not wait(Client,botid,"networks to add and press"):return False
                Client.get_messages(botid)[0].click(text = "☑️️ Done")
                time.sleep(random.randint(2,3))
                if not wait(Client,botid,"Enter address to watch"):return False 
                Client.send_message(botid,wallet[i])
                time.sleep(random.randint(2,3))
                if not wait(Client,botid,"Enter label for"):return False 
                Client.send_message(botid,"Wallet " + str(i + 1))
                time.sleep(random.randint(2,3))
                if not wait(Client,botid,"You can customize event types"):return False 
                Client.get_messages(botid)[0].click(text = "Add More to Main")
                time.sleep(random.randint(2,3))

        except:
            Client.disconnect()
            k = 0
        if k == 1: Client.disconnect()
        

if __name__ == '__main__':
    wallet = open_file(r'C:\Users\PC\OneDrive\Documents\Data\Full_Acc_Tele\Session\wallet_1000_1.txt')
    botid = "EtherDROPS6_bot"
    task(botid,wallet)