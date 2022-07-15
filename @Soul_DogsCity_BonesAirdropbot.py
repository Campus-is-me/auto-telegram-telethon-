from distutils.command.clean import clean
from multiprocessing.connection import Client
from turtle import right
from telethon.tl.functions.messages import StartBotRequest
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.sync import TelegramClient
import time, random ,requests , os
from anticaptchaofficial.imagecaptcha import *

def Captcha_imanage(Client,phone,botid): 
    try:
        solver = imagecaptcha()
        solver.set_verbose(1)
        solver.set_key("key")
      
        messages = Client.get_messages(botid)
        msg = messages[0]
        imageLink = "files/" + phone 
        imageFile =  Client.download_media(msg.media, imageLink )
        captcha_text = 0 
        captcha_text = solver.solve_and_return_solution(imageFile)   #nhận captcha từ anticaptcha
        os.remove(imageFile)
        
        if captcha_text != 0:
            print("captcha text "+captcha_text)
            Client.send_message(botid, captcha_text)          #Send captcha từ anticaptcha vào con bot
            time.sleep(random.randint(3,5))
            messages =  Client.get_messages(botid)             # Sau khi sent, nhận kết quả từ con bot 
            if messages[0].message.find('Wrong captcha') != -1:   #Kiểm tra xem captcha đúng chưa
                return False
            return True        
        else:
            print("task finished with error "+solver.error_code)
            return False 
    except: print("Loi khong xac dinh")

def gettxt(filetxt):
    with open(filetxt , 'r') as file:
        list = file.readlines()
    list_strip = []
    for i in list:
        list_strip.append(i.strip())
    return list_strip

def wait(Client,botID,check):

    time.sleep(random.randint(1,3))
    for i in range(0,10):
        tmp = Client.get_messages(botID)
        if str(tmp[0].message).find(check) != -1:
            return True
        else:time.sleep(5)

    Client.disconnect()
    return False

def random_sleep():
    time.sleep(random.randint(1,3))

def task(phone,api_id,api_hash, botid,twitter_link,linkyoutube,sol_wallet,ref): 
   
    Client = TelegramClient("C:\\Users\\Hieu\\Desktop\\Python\\session\\" + phone,api_id,api_hash)
    Client.connect()

    if not Client.is_user_authorized(): 
        print('SS lỗi:',phone)
        return False
    else:

        try:
            
            Client(StartBotRequest(botid, botid, ref))
            #Client.send_message(botid,"/start")

            if not wait(Client,botid,'❇️ Enter the captcha:'): return False
            Captcha_imanage(Client,phone,botid)
               

            if not wait(Client,botid,'Click "Continue" to proceed'): return False
            Client.send_message(botid,"Continue")
            
            if not wait(Client,botid,"Complete the tasks below!"):return False
            Client(JoinChannelRequest("airdropinspector"))
            random_sleep()
            Client.send_message(botid,"Submit Details")

                

            if not wait(Client, botid, "Join Bones Telegram"): return False 
            Client.send_message(botid, "✅Done")
        
            if not wait(Client, botid, "Follow Farm Bones on"): return False 
            Client. send_message(botid, twitter_link) 

            if not wait(Client, botid, "Subscribe Farm Bones on"): return False
            Client.send_message(botid, linkyoutube)
      
            if not wait(Client,botid,"Please join our advertiser telegram channel"): return False
            Client.send_message(botid,"✅Done")

            if not wait(Client,botid,"Follow our advertiser at"): return False
            Client.send_message(botid,"✅ Yes")

            if not wait(Client,botid,"Submit your Solana (SOL) wallet address"): return False
            Client.send_message(botid, sol_wallet)

          

            Client.disconnect()

        except: 
            try: 
                Client.disconnect()
            except:pass

def main():
    twitter_link = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\social_data\\twitter_link.txt")
    linkyoutube = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\social_data\\linkyoutube.txt")
    sol_wallet = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\wallet\\sol_wallet")
    listphone = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\session\\list_phone.txt")



    


    api_id = 16084692
    api_hash = 'd2854dd168da24ae3805cc6450488425'

    botid = "Soul_DogsCity_BonesAirdropbot"
    
    ref = "r00524220170"
    
    for i in range(1,len(listphone)):
        try:
            task(listphone[i],api_id,api_hash,botid,twitter_link[i],linkyoutube[i],sol_wallet[i],ref[-1])
        except:pass



if __name__ == '__main__':main()



