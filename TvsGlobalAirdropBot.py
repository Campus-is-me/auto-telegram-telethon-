from cgitb import text
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


def task(phone,api_id,api_hash, botid,tw, wall,email,retweet,instagram,medium,ref): 
   
    Client = TelegramClient("C:\\Users\\Hieu\\Desktop\\seasion\\" + phone,api_id,api_hash)
    Client.connect()

    if not Client.is_user_authorized(): 
        print('SS lỗi:',phone)
        return False
    else:

        try:
            
            Client(StartBotRequest(botid, botid, ref))
            #Client.send_message(botid,"/start")

            if not wait(Client,botid,"Click on Continue before typing the code"): return False
            ######################### solve captcha math#############
            mess = Client.get_messages(botid)
            list = mess[0].text.strip().split(":")
            print(list)

            newlist = list[1].strip().split("=")
            print(newlist)
            newlist0 = newlist[0].strip()
            print(newlist0)

            try:
                list_int = newlist0.split("+")
                cal = int(list_int[0]) + int(list_int[1])
                print(cal) 
                mess[0].click()
                if not wait(Client, botid, "Great, please enter the code."): return False 
                Client.send_message(botid,str(cal))
            except:
                list_int = newlist0.split("-")
                cal = int(list_int[0]) - int(list_int[1])
                print("Ket qua captcha: ",cal)
                mess[0].click() 
                if not wait(Client, botid, "Great, please enter the code."): return False 
                Client.send_message(botid,str(cal))           
            ######################### solve captcha math#############
           

            if not wait(Client, botid, "Welcome to participate in our airdrop!"): return False 
            Client(JoinChannelRequest("tvstalk"))
            time.sleep(random.randint(1,2))
            mess = Client.get_messages(botid)
            mess[0].click()

            if not wait(Client, botid, "Now please follow our"): return False 
            Client. send_message(botid, tw)

            if not wait(Client, botid, "Submit your Medium"): return False
            Client.send_message(botid, medium)
      
            if not wait(Client,botid,"Please Join our"): return False
            mess = Client.get_messages(botid)
            mess[0].click()

            if not wait(Client,botid,"Optional + 0.5 DIA"): return False
            Client(JoinChannelRequest("airdrop6officialchannel"))
            time.sleep(random.randint(1,3))
            mess = Client.get_messages(botid)
            print(mess[0].text)
            mess[0].click()

            if not wait(Client,botid,"Please submit your Polygon-Matic wallet address below"): return False
            Client.send_message(botid, wall)

            Client.disconnect()

        except: 
            try: 
                Client.disconnect()
            except:pass

def main():

    listtwitter = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\telebot\\tw@.txt")
    listwall = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\telebot\\wall.txt")
    listphone = gettxt("C:\\Users\\Hieu\\Desktop\\seasion\\list.txt")
    listemail = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\telebot\\email.txt")
    listinstagram = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\telebot\\instagram.txt")
    listmedium = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\telebot\\medium@.txt")
    listretweet = gettxt("C:\\Users\\Hieu\\Desktop\\Python\\telebot\\retweet.txt")

    api_id = 16084692
    api_hash = 'd2854dd168da24ae3805cc6450488425'
    botid = "TvsGlobalAirdropBot"
    
    ref = "r00524220170"
    for i in range(0,1):
        try:
            task("+84906694405",api_id,api_hash,botid,listtwitter[i],listwall[i],listemail[i],listretweet[i],listinstagram[i],listmedium[i],ref)
        except:pass



if __name__ == '__main__':main()



