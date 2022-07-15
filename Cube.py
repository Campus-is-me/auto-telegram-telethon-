#Fasst
#Made by Campus
#Contact for work or feedback to Telegram: @TokudaJav or Zalo: 0337176055
#Simple Tool
import asyncio, os, random, string, csv, traceback, subprocess
from http import client
from pickle import TRUE
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
#group 

#✨ Hello Johnny, welcome to Join Cube Genesis Airdrop. Please solve the task below to start: 46+2=

#✨ Hello Johnny, welcome to Join Cube Genesis Airdrop. Please solve the task below to start: 46+2=
#Airdrop pool: 100,000
#click 0
#Then, CLICK “Next Step” button to move forward.
#
#open file 
def open_file(link_file):
    with open(link_file,'r') as f:
        list = f.readlines()
    list_file = []
    for i in list:
        list_file.append(i.strip())
    return list_file

#(target=Fasst(i + 1, fphone[i], api_id, api_hash, bot_id, ref, ftele[i], ftwit[i], fyou[i], fins[i], fwallet[i]))
#Funcion:
def Fasst(stt, phone, api_id, api_hash, bot_id, ref, fgmail, fretwit, fwallet):
    #wait action
    def wait(client, bot_id, check):
        time.sleep(random.randint(4, 5))
        for i in range(0, 9):
            tmp = client.get_messages(bot_id)
            if str(tmp[0].message).find(check) != -1:
                return True
            else: time.sleep(random.randint(4, 5))
        client.disconnect()
        return False
    def Pass_Captcha_2(join_bot):
        join_bot = join_bot.replace('Please answer: ',"")
        x = ''
        y = ''
        k = 0
        math = ''
        for i in range(0,len(join_bot) - 1):
            if join_bot[i] >= '0' and join_bot[i] <= '9' and k == 0:
                x += join_bot[i]
            elif join_bot[i] == '+' or join_bot[i] == '-':
                math += join_bot[i]
                k = 1
            elif join_bot[i] == ' ':
                continue
            else:
                y += join_bot[i]
        if math == '+':
            return str(int(x) + int(y))
        else:
            return str(int(x) - int(y))
    #Solution
    def full_task():
        print("Start: ", stt)
        for i in range(0, 1):
            try:
                #@legit365airdrops
                Client(JoinChannelRequest('legit365airdrops'))
                sleep(random.randint(7,8))
                print("Join group 1")
                Client(JoinChannelRequest('Cube_Network'))
                print("Join group 2")
                sleep(random.randint(7,8))
                Client(JoinChannelRequest('CUBE_Announcement'))
                sleep(random.randint(4,5))
                print("Join group 3")
            except: pass
        print("Join group Done")
        #step 1 check message
        if not wait(Client, bot_id, "Please solve the task below to start"): return False
        Client.send_message(bot_id, "888")
        print("Done step 1 ", stt)
        sleep(random.randint(4,5))  
        #step 2 send answer
        if not wait(Client, bot_id,"Please answer: "): return False
        message = Client.get_messages(bot_id)[0]
        join_bot = str(message.message).strip()
        print(join_bot)
        Client.send_message(bot_id,Pass_Captcha_2(join_bot))
        sleep(random.randint(4,5))  
        print("Done step 2 ", stt)
        #step 3 click start task 
        if not wait(Client, bot_id, "Airdrop pool: 100,000"): return False
        Client.get_messages(bot_id)[0].click()
        sleep(random.randint(4,5))   
        print("Done step 3 ", stt)
        #step_4 click next step
        if not wait(Client, bot_id, "Please CLICK “Join Cube Telegram” button to join our Telegram group."): return False
        Client.get_messages(bot_id)[0].click(1)
        print("Done step 4 ", stt)    
        sleep(random.randint(4,5))
        #step 5
        if not wait(Client, bot_id, "Please CLICK “Join Cube Telegram Channel” button"): return False
        Client.get_messages(bot_id)[0].click(1)
        print("Done step 5 ", stt)    
        sleep(random.randint(4,5))

        #step_6 send username twitter
        ftwit = fretwit
        ftwit = ftwit.replace('https://twitter.com/',"").split("/")[0]
        if not wait(Client, bot_id, "Then, ENTER your Twitter username to move forward."): return False
        Client.send_message(bot_id,"@" +  ftwit)
        print("Done step 6 ", stt)
        sleep(random.randint(4,5))        
        #step_7 send retwitter
        if not wait(Client, bot_id, 'Then, ENTER your retweet link to move forward.'): return False
        Client.send_message(bot_id, fretwit)
        print("Done step 7 ", stt)
        sleep(random.randint(4,5)) 
        #step_8 click next step
        if not wait(Client, bot_id, 'Please CLICK “Join Cube Discord” button to join our Discord.'): return False
        Client.get_messages(bot_id)[0].click(1)
        print("Done step 8 ", stt)
        sleep(random.randint(4,5))
        #step_9 send wallet
        if not wait(Client, bot_id, 'Please COPY your CUBE ADDRESS and ENTER it below to receive CUBE (How to set up CUBE on Metamask'): return False
        Client.send_message(bot_id, fwallet)
        print("Done step 9 ", stt)
        sleep(random.randint(4,5))
        return True

#start bot 
    Client = TelegramClient(phone, api_id, api_hash)
    Client.connect()
    if not Client.is_user_authorized:
        print("SESSION ERROR -----> ", phone)
        Client.disconnect()
        time.sleep(2)
        return False
    else:
        try:
            Client(StartBotRequest(bot_id, bot_id,ref))
            sleep(random.randint(4,6))
            if not full_task(): print("Mission not Successfull ", stt)
            else: print("mission successfull")
            Client.disconnect()
            time.sleep(2)
            return True
        except:
            print("Error running bot ", phone)
            time.sleep(2)
            Client.disconnect()
            time.sleep(2)
            return False


#main funcion
if __name__ == '__main__':
    #open file phone 
    fphone = open_file('phone.txt')
    #open file username twitter
    fretwit = open_file('crawl_retwitter_code_tool.txt')
    #open file wallet sol
    fwallet = open_file('wallet_1000_1.txt')
    #open file gmail 
    fgmail = open_file("gmail800.txt")
    #### info api, obt, ref
    api_id = '9711828' 
    api_hash = '09ee6b9d9dad99b9470fcbbdea601785'
    bot_id = 'CubeAirdropBot'                                                      
    ref = '5081536674'
    #group https://t.me/monkeyempiree  https://t.me/CUBE_Announcement
    #group = ['CUBE_Announcement','Cube_Network','']
    #running ____________
    print("START BOT ------- ")
    i = 1
    while i < 388:
        try:
            j = 0 
            processes = [] 
            while j < 6 and i < 388:
                process =  Process(target=Fasst,args=(i + 1, fphone[i], api_id, api_hash, bot_id, ref, fgmail[i], fretwit[i], fwallet[i]))
                processes.append(process)
                j += 1
                i += 1
            print("Khoi chay da luong")
            for process in processes:
                process.start()
                time.sleep(2)
            for process in processes: 
                process.join()
            print("Ket thuc chay da luong")
            time.sleep(3)
        except:
            print("Loi khong xac dinh")
            i += 1
            pass
        