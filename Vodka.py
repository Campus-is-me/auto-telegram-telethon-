#Fasst
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

#(target=Fasst(i + 1, fphone[i], api_id, api_hash, bot_id, ref, ftele[i], ftwit[i], fyou[i], fins[i], fwallet[i]))
#Funcion:
def Fasst(stt, phone, api_id, api_hash, bot_id, ref, ftele, ftwit, fyou, fins, fwallet, group):
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
        for i in range(0, len(group) - 1):
            try:
                Client(JoinChannelRequest(group[i]))
                sleep(random.randint(4,5))
            except: pass
        #step 1 click
        #if not wait(Client, bot_id, '➡️'): return False  
        message = Client.get_messages(bot_id)[0]
        join_bot = str(message.message).split("\n")[2].strip()
        text = message.click()
        sleep(random.randint(4,5))   
        print("Done step 1 ", stt)
        #step_2 pass captcha
        if not wait(Client, bot_id, "Great Send Answer"): return False
        Client.send_message(bot_id, Pass_Captcha_2(join_bot))
        print("Done step 2 ", stt)    
        sleep(random.randint(4,5))
        #step 3
        if not wait(Client, bot_id, "Welcome to Fasst Airdrop Bot"): return False
        Client.get_messages(bot_id)[0].click()
        sleep(random.randint(4,5))
        print("Done step 3 ", stt) 
        #step_4 send username tele
        if not wait(Client, bot_id, "Now please Send Your Telegram"): return False
        Client.send_message(bot_id,"@" +  ftele)
        print("Done step 4 ", stt)
        sleep(random.randint(4,5))        
        #step_5 send twitter
        if not wait(Client, bot_id, 'like and retweet the pinned post then send me your Twitter Profile'): return False
        Client.send_message(bot_id,ftwit)
        print("Done step 5 ", stt)
        sleep(random.randint(4,5)) 
        #step_6 send youtube
        if not wait(Client, bot_id, 'Please Subscribe'): return False
        Client.send_message(bot_id, fyou)
        print("Done step 6 ", stt)
        sleep(random.randint(4,5))
        #step_7 send instagram
        if not wait(Client, bot_id, 'Now please follow our'): return False
        Client.send_message(bot_id, fins)
        print("Done step 7")
        sleep(random.randint(4,5))
        #step 8 choose wallet
        if not wait(Client, bot_id, 'Submit your'): return False
        Client.send_message(bot_id, fwallet)
        print("Done step 9")
        #step 10
        sleep(random.randint(4,5))
        if not wait(Client, bot_id, 'Please Verify All Info Are Correct'): return False
        Client.get_messages(bot_id)[0].click(text = "✅ Yes")
        print("Done step 10 ", stt)
        sleep(random.randint(4,5))

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
            full_task()
            print("Mission successful ", stt)
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
    ftwit = open_file('crawl_followers_fasstofficial.txt')
    #open file wallet trx
    fwallet = open_file('100_tron_wallet.txt')
    #open username telegram
    ftele = open_file('user_name.txt')
    #open youtube
    fyou = open_file('craw_data_youtube.txt')
    #open instagram
    fins = open_file('crawl_instagramfas.txt')
    #### info api, obt, ref
    api_id = '9711828' 
    api_hash = '09ee6b9d9dad99b9470fcbbdea601785'
    bot_id = 'FasstAirdropBot'                                                      
    ref = '5081536674'
    #group https://t.me/monkeyempiree
    group = ['fassttoken','fasstofficial']
    #running ____________
    print("START BOT ------- ")
    i = 260
    while i < 388:
        try:
            if i > 0:
                try:
                    subprocess.call('rasdial Mobiphone /DISCONNECT')
                    time.sleep(5)
                    subprocess.call('rasdial Mobiphone')
                    time.sleep(5)
                except: pass
            j = 0 
            processes = [] 
            while j < 10 and i < 388:
                process =  Process(target=Fasst,args=(i + 1, fphone[i], api_id, api_hash, bot_id, ref, ftele[i], ftwit[i], fyou[i], fins[i], fwallet[i], group))
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
        except:
            print("Loi khong xac dinh")
            i += 1
            pass
        