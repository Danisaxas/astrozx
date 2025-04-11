from _date import rex,bin_chk
from Source_pack.TextAll import _infochat,msgregist,iptext
from classBot.MongoDB import querygrup,queryUser
import requests

@rex(['ip'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:
            ips = msg.text[len('/ip '):]
            if not ips: return await msg.reply('<b> ₪ Input ⇝ <code>$ip 1.1.1.1</code></b>')
            req = requests.get(f'https://ipwho.is/{ips}')
            if '"success":false' in req.text:
                return await msg.reply('<b>Invalid IP address ❌</b>')
            else:
                rr = req.json()
                ms = iptext.format(ips,
                                   rr['country'],
                                   rr['country_code'],
                                   rr['flag']['emoji'],
                                   rr['latitude'],
                                   rr['longitude'],
                                   rr['capital'],
                                   rr['connection']['domain'],
                                   rr['postal'],
                                   msg.from_user.first_name)
                await msg.reply(ms) 