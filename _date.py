from pyrogram import Client,filters
from Source_pack.TextAll import *
import time, logging,requests

def rex(bit:str= None):
    nix = Client.on_message(filters.command(bit, ["/", ".", ",","-","$","%","&"]))
    return nix

def rexButton(bit:str= None):
    nix = Client.on_callback_query(filters.regex(bit))
    return nix

_hasd = '3ed76d05d92a5203ca076066146a47bc'
_tokn= '7043053830:AAGfNstCHiakCBay8DFdc0j5QUVwc9yl4GI'
video = 'https://i.imgur.com/Ewq69ET.gif'

loogs = logging.basicConfig(level=logging.INFO)

print(requests.get('https://translate.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&es=en&q=hellow&tbb=1&ie=UTF-8&oe=UTF-8').text)


def bin_chk(bina:int=None,chkby:str= None):
    req = requests.get(f'https://bins.antipublic.cc/bins/{bina}')
    if  "detail" in req.text:
        return f"<b>{req.json()['detail']}</b>"
    else:
        text = bintext.format(
                        req.json()['bin'],
                        req.json()['brand'],
                        req.json()['country_name'],
                        req.json()['country'],
                        req.json()['country_flag'],
                        req.json()['level'],
                        req.json()['type'],
                        req.json()['bank'],
                        chkby
                        )
        return text

def skey(
        data,
        headers,
        key:str=None,
        name:str=None
        ):

        pos = requests.post(f"https://api.stripe.com/v1/tokens",data=data, headers=headers, auth=(key, ""))
        if 'Invalid API Key provided' in pos.text:
            resp = sk.format('Dead ❌','Invalid API Key provided',name)
            return resp
        elif 'api_key_expired' in pos.text:
            resp = sk.format('Dead ❌','api_key_expired',name)
            return resp
        elif 'testmode_charges_only' in pos.text:
            resp = sk.format('Dead ❌','testmode_charges_only',name)
            return resp
        elif 'test_mode_live_card' in pos.text:
            resp = sk.format('Live ✅','test_mode_live_card',name)
            return resp
        else:
            resp = sk.format('Live ✅','Aprovado',name)
            return resp



usertime = {}
timetake = 15
def atspam(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        if 5416957433 in usertime and time.time() - usertime[user_id] < timetake:
            await func(client, message)
            usertime[user_id] = time.time()
            return
        elif user_id in usertime and time.time() - usertime[user_id] < timetake:
            wait_time = int(timetake - (time.time() - usertime[user_id]))
            await message.reply(f"<b>₪ AntiFlood ⇝ <code>{wait_time} sg.</code> </b>")
            return
        else:
            await func(client, message)
            usertime[user_id] = time.time()

    return wrapper