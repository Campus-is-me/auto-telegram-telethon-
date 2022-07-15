#Fasst
#Made by Campus
#Contact for work or feedback to Telegram: @TokudaJav or Zalo: 0337176055
#Simple Tool
import asyncio, os, random, string, csv, traceback, subprocess
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
'''
➡️Before we start the airdrop, please prove you are human by answering the question below.
    
Please answer: 97 + 45 =
Click on Continue before typing the code
'''
"""
click continue
send code 
join https://t.me/VerasawOfficialGroup
https://t.me/verasawOfficial
click 
click
send twitter @NguynHo47196812
click Done
send gmail
click Done
send sol 

"""
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
def Fasst(stt, phone, api_id, api_hash, bot_id, ref, group, fgmail, ftwit, fwallet):
    #wait action
    def wait(client, bot_id, check):
        time.sleep(random.randint(2,5))
        for i in range(0, 9):
            tmp = client.get_messages(bot_id)
            if str(tmp[0].message).find(check) != -1:
                return True
            else: time.sleep(random.randint(4, 5))
        client.disconnect()
        return False
    def Pass_Captcha_2(join_bot):
        x = ''
        y = ''
        k = 0
        math = ''
        for i in range(15,len(join_bot) - 1):
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
        for i in range(0, len(group)):
            try:
                Client(JoinChannelRequest(group[i]))
                print("Join group ", i + 1)
                sleep(random.randint(4,5))
            except: pass
        print("Join group Done")
        #step 1 click
        #if not wait(Client, bot_id, '➡️'): return False  
        message = Client.get_messages(bot_id)[0]
        join_bot = str(message.message).split("\n")[2].strip()
        text = message.click()
        sleep(random.randint(4,5))   
        print("Done step 1 ", stt)
        #step_2 pass captcha
        if not wait(Client, bot_id, "Great, please enter the code"): return False
        Client.send_message(bot_id, Pass_Captcha_2(join_bot))
        print("Done step 2 ", stt)    
        sleep(random.randint(4,5))
        #step 3
        if not wait(Client, bot_id, "Welcome to participate in our airdrop!"): return False
        Client.get_messages(bot_id)[0].click()
        sleep(random.randint(4,5))
        print("Done step 3 ", stt) 
        #step_4 send username twitter
        if not wait(Client, bot_id, "then enter your twitter username with"): return False
        Client.send_message(bot_id,"@" +  ftwit)
        print("Done step 4 ", stt)
        sleep(random.randint(4,5))        
        #step_5 click pass youtube
        if not wait(Client, bot_id, 'and click the "Done" button below'): return False
        Client.get_messages(bot_id)[0].click()
        print("Done step 5 ", stt)
        sleep(random.randint(4,5)) 
        #step_6 send email
        if not wait(Client, bot_id, 'Please add VeraSaw watchlist on'): return False
        Client.send_message(bot_id, fgmail)
        print("Done step 6 ", stt)
        sleep(random.randint(4,5))
        #step_7 click pass 0
        if not wait(Client, bot_id, 'then Press "Done" or "Skip" button. (Optional + 2,000 VRS)'): return False
        Client.get_messages(bot_id)[0].click()
        print("Done step 7 ", stt)
        sleep(random.randint(4,5))
        #step 8 send wallet
        if not wait(Client, bot_id, 'Please submit your Solana-SOL wallet'): return False
        Client.send_message(bot_id, fwallet)
        print("Done step 9 and full task ", stt)
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
    ftwit = open_file('crawl_followers_VeraSaw.txt')
    #open file wallet sol
    fwallet = open_file('1000_sol.txt')
    #open file gmail 
    fgmail = open_file("gmail800.txt")
    #### info api, obt, ref
    api_id = '9711828' 
    api_hash = '09ee6b9d9dad99b9470fcbbdea601785'
    bot_id = 'VeraSawNewAirdropBot'                                                      
    ref = '5081536674'
    #group https://t.me/monkeyempiree
    group = ['verasawOfficial']
    #running ____________
    print("START BOT ------- ")
    i = 0
    while i < 388:
        try:
            j = 0 
            processes = [] 
            while j < 4 and i < 1000:
                ftwit[i] = ftwit[i].replace("https://twitter.com/", "")
                process =  Process(target=Fasst,args=(i + 1, fphone[i], api_id, api_hash, bot_id, ref, group, fgmail[i], ftwit[i], fwallet[i]))
                processes.append(process)
                j += 1
                i += 1
            print("Start multithreading")
            for process in processes:
                process.start()
                time.sleep(2)
            for process in processes: 
                process.join()
            print("Finish running multithreading")
            time.sleep(3)
        except:
            print("An unknown error :((((")
            i += 1
            pass
        