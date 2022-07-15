#made by Mike
import asyncio
from multiprocessing.connection import wait
import telethon, os, time, random, tracemalloc
from telethon.tl.functions.messages import GetMessagesRequest, SendMessageRequest
from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from time import sleep
#Nhập api_id, api_hash ở đây https://t.me/defiai_en
api_id = '19476436'
api_hash = '4e0239901c58218bf605e116f6c427c9'


def Solution(phone):
    async def main():
        me = await client.get_me()
        username = me.username
        #await print('Done get user name')
        return username
##############################################

    client = TelegramClient(phone,api_id, api_hash)
    time.sleep(2)
    client.connect()
    if not client.is_user_authorized():
        print("Session Lỗi: ", phone)
        client.disconnect()
        return False
    else:
        try:
            with client:
                username = client.loop.run_until_complete(main())
            #sleep(random.randint(5,7))
            #client(JoinChannelRequest('defiai_en'))
            #sleep(random.randint(1,2))
            #message = client.get_messages('defiai_en')
            #sleep(random.randint(1,2))
            #verify = message[0].click(0)
            #time.sleep(2)
            #print('Join group complete: ',phone)
            print("Nhiệm vụ hoàn thành: ", phone)
            time.sleep(2)
            client.disconnect()
            return username
        except:
            print("Qúa trình khởi chạy nhiệm vụ bị lỗi: ", phone)
            time.sleep(2)
            client.disconnect()
            return False
    



if __name__ == "__main__":
    f = open('list.txt','r')
    get_username = open('user_name_1.txt','w')
    i = 0
    time.sleep(2)
    while i < 10:
        phone = f.readline().strip()
        username =  Solution(phone)
        if username != False:
            get_username.write(username + '\n')
            i += 1
            time.sleep(2)
        else:
            get_username.write('\n')
            i += 1
            time.sleep(2)

    f.close()
    get_username.close()



