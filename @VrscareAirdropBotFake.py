try:
            
            Client(StartBotRequest(botid, botid, ref))
            #Client.send_message(botid,"/start")

            if not wait(Client,botid,"Before we start the airdrop") : return False
            mess = Client.get_messages(botid)
            mess[0].click()


            ######################## solve captcha math#############
            if not wait(Client,botid,"Great, please enter the code") : return False
            list = mess[0].text.strip().split(":")
           

            newlist = list[1].strip().split("=")
           
            newlist0 = newlist[0].strip()
            #newlist0 = newlist00.strip("**")
            print(newlist0)

            try:
                list_int = newlist0.split("+")
                cal = int(list_int[0]) + int(list_int[1])
                print(cal) 
                Client.send_message(botid,str(cal))
            except:
                list_int = newlist0.split("-")
                cal = int(list_int[0]) - int(list_int[1])
                print("Ket qua captcha: ",cal)
                Client.send_message(botid,str(cal))           
            ######################### solve captcha math#############

            if not wait(Client,botid,"Thats correct!"): return False
            Client(JoinChannelRequest("Vres_VRS"))
            Client(JoinChannelRequest("vrscare"))
            mess = Client.get_messages(botid)
            mess[0].click()

            if not wait(Client,botid,"Please join"): return False
            mess = Client.get_messages(botid)
            mess[0].click()

            if not wait(Client,botid,"Now please follow our"): return False
            Client.send_message(botid,twitter_user)

            if not wait(Client,botid,"Please Follow our"): return False
            Client.send_message(botid,medium_user)

            if not wait(Client,botid,"Optional + 0.5 BUSD"): return False
            mess = Client.get_messages(botid)
            mess[0].click(text = "Done")

            if not wait(Client,botid,"Please submit your Binance Smart"): return False
            Client.send_message(botid,bsc_wallet)
            

            Client.disconnect()