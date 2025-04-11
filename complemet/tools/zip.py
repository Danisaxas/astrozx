from _date import rex,bin_chk
from Source_pack.TextAll import _infochat,msgregist,ziptext
from classBot.MongoDB import querygrup,queryUser
import requests

@rex(['zip'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:
            codep = msg.text[len('/zip '):]
            if not codep: return await msg.reply('<b> ₪ Input ⇝ <code>$zip 10100</code></b>')
            zip_api = requests.get(f'https://zip.getziptastic.com/v2/US/{codep}')
            if 'Not Found' in zip_api.text:
                return await msg.reply('<b>Not Found | codigo postal erroneo. ❌</b>')
            else:
                ms = ziptext.format(
                    zip_api.json()['country'],
                    zip_api.json()['postal_code'],
                    zip_api.json()['city'],
                    zip_api.json()['state_short'],
                    msg.from_user.first_name)
                
                await msg.reply(ms)    