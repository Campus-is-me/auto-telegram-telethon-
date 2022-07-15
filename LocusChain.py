#Made by Campus
import asyncio, os, random, string, csv, traceback, subprocess
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

#code for my life
list_error  = []
def Bot_Pass_Captcha(j,phone,api_id, api_hash, bot_id, ref, twit,wallet,group):
    #Pass Captcha
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
    #Pass full task 
    def Full_Task():
        for i in range(0, len(group)):
            try:
                Client(JoinChannelRequest(group[i]))
                sleep(random.randint(5,7))
            except: pass
        message = Client.get_messages(bot_id)
        join_bot = message[0].message.split("\n")[2]
        text = message[0].click()
        sleep(random.randint(5,7))
        Client.send_message(bot_id, Pass_Captcha_2(join_bot))
        print("step 1 success: ", j)

        sleep(random.randint(5,7))
        message = Client.get_messages(bot_id)
        message = message[0].click()
        print("step 2 success: ", j)

        sleep(random.randint(5,7))
        message = Client.get_messages(bot_id)
        message = message[0].click()
        print("step 3 success: ", j)

        sleep(random.randint(5,7)) 
        Client.send_message(bot_id,"@" + twit)
        print("step 4 success: ", j)

        sleep(random.randint(5,7))
        #Client.send_message(bot_id,gmail)
        #sleep(random.randint(5,7))
        message = Client.get_messages(bot_id)
        message = message[0].click(1)
        print("step 5 success: ", j)

        sleep(random.randint(5,7))
        Client.send_message(bot_id,wallet)
        print("step 6 success: ",j)
        time.sleep(2)


    Client = TelegramClient(phone,api_id, api_hash)
    Client.connect()
    if not Client.is_user_authorized():
        print("Session Error: ", phone)
        Client.disconnect()
        time.sleep(2)
        return False
    else:
        try:
            Client(StartBotRequest(bot_id, bot_id, ref))
            print(str(j) + " start bot success: " + phone)
            sleep(random.randint(6,7))
            Full_Task()
            print(str(j) + " Mission Success: " + phone)
            time.sleep(2)
            Client.disconnect()
            return True
        except:
            print(str(j) + " StartBot Error: " + phone)
            list_error.append(phone)
            Client.disconnect()
            time.sleep(2)
            return False




#https://t.me/locusofficialGroup https://t.me/locusofficial https://t.me/airdrop6community https://t.me/airdrop6officialchannel
if __name__ == '__main__':
    f = open('phone.txt','r')
    ftwit = open('8979_Twitter.txt','r')
    #fgmail = open('25130_Gmail.txt','r')
    fwallet = open('100_tron_wallet.txt','r')
    list_error = []
    ####
    api_id = '9711828'
    api_hash = '09ee6b9d9dad99b9470fcbbdea601785'
    bot_id = 'LocusChainAirdropBot'
    ref = '5081536674'
    group = ['locusofficialGroup','locusofficial','airdrop6officialchannel','airdrop6community']
    rate = 0
    while rate < 60:
        f.readline()
        ftwit.readline()
        fwallet.readline()
        rate += 1
        print(rate)
    i = rate
    while i < 388:
        try:
            if (i) % 8 == 0:
                try: 
                    subprocess.call('rasdial Mobiphone /DISCONNECT')
                    time.sleep(5)
                    subprocess.call('rasdial Mobiphone')
                    time.sleep(5)
                except: pass
            j = 0 
            processes = [] 
            while j < 4 and i < 388:
                phone = f.readline().strip()
                twit = ftwit.readline().strip()
                #gmail = fgmail.readline().strip()
                wallet  =fwallet.readline().strip()
                process =  Process(target=Bot_Pass_Captcha,args=(i + 1,phone,api_id,api_hash,bot_id,ref,twit,wallet,group))
                processes.append(process)
                j += 1
                i += 1
            print("Khoi chay da luong")
            for process in processes:
                process.start()
                time.sleep(1)
            for process in processes: 
                process.join()
            print("Ket thuc chay da luong")
        except:
            print("Loi khong xac dinh")
            i += 1
            pass
    f.close()
    ftwit.close()
    fwallet.close()
    for x in range(0,len(list_error)):
        print("Tele bị lỗi bị lỗi: {}".format(list_error[x]))