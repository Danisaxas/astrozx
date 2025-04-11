from _date import rex,atspam
from Source_pack.TextAll import _infochat,msgregist
from Source_pack.BoutnAll import binchk
from classBot.MongoDB import querygrup,queryUser
from def_gates.def_dl import chak
import re,requests,time


@rex(['dl'])
@atspam
async def dl(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:
            ccs = msg.text[len('/dl '): ]
            if not ccs:return await msg.reply('<b> ₪ Input ⇝ <code>$dl ccs</code></b>')
            else:

                req = requests.get(f'https://bins.antipublic.cc/bins/{ccs}')
                
                flag = req.json()['country_flag']
                text = """<b>₪ Gate | Stripe charged

₪ cc  ⇝ <code>{}</code>
₪ response  ⇝ {}
₪ code  ⇝ <code>{} {}</code>
₪ Name ⇝ dRgoodulino
-
₪ From ⇝ <code>{}</code>
₪ Access Owner ⇝ <code> 𝗺𝗮𝘅 ريكس 🇮🇳</code></b>"""
                
                msgs = await msg.reply('<b><i>Checkings..</i></b>')
                ccs = re.findall(r'[0-9]+',msg.text)
                req = chak(ccs[0],ccs[1],ccs[2],ccs[3])         
                msg1 = await msgs.edit_text('<b><i>Checkings 100%.</i></b>')
                time.sleep(1)
                
                try:
                    if "Your card has insufficient funds." in req.text:
                        await msg1.edit_text(text.format(
                                                    f'{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}',
                                                    req.json()['errors'][0]['Value'],
                                                    req.json()['errors'][1]['Value'],
                                                    '✅',
                                                    msg.from_user.id 
                                                    ),reply_markup=binchk(flag))
                        
                    elif "Your card's security code is invalid." in req.text:
                        await msg1.edit_text(text.format(
                                                    f'{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}',
                                                    req.json()['error']['message'],
                                                    req.json()['error']['code'],
                                                    '✅',
                                                    msg.from_user.id 
                                                    ),reply_markup=binchk(flag))
                        
                    elif "Incorrect CVC code" in req.text:
                        await msg1.edit_text(text.format(
                                                    f'{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}',
                                                    req.json()['errors'][0]['Value'],
                                                    req.json()['errors'][1]['Value'],
                                                    '✅',
                                                    msg.from_user.id 
                                                    ),reply_markup=binchk(flag))
                        
                    elif    "Your card's security code is incorrect." in req.text:
                        await msg1.edit_text(text.format(
                                                    f'{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}',
                                                    req.json()['errors'][0]['Value'],
                                                    'cvc_incorrect',
                                                    '✅',
                                                    msg.from_user.id 
                                                    ),reply_markup=binchk(flag))
                        
                    elif 'success":True' in req.text:
                        await msg1.edit_text(text.format(
                                                    f'{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}',
                                                    req.json()['errors'][0]['Value'],
                                                    req.json()['errors'][1]['Value'],
                                                    '✅',
                                                    msg.from_user.id 
                                                    ),reply_markup=binchk(flag))
                        
                    elif "incorrect_number" in req.text:
                        await msg1.edit_text(text.format(
                                                    f'{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}',
                                                    req.json()['error']['message'],
                                                    req.json()['error']['code'],
                                                    '❌',
                                                    msg.from_user.id 
                                                    ),reply_markup=binchk())
                    else:
                        await msg1.edit_text(text.format(
                                                    f'{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}',
                                                    req.json()['errors'][0]['Value'],
                                                    req.json()['errors'][1]['Value'],
                                                    '❌',
                                                    msg.from_user.id 
                                                    ),reply_markup=binchk(flag))
                except:
                    await msg1.edit_text(text.format(
                                                    f'{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}',
                                                    req.json()['error']['message'],
                                                    req.json()['error']['code'],
                                                    '❌',
                                                    msg.from_user.id 
                                                    ),reply_markup=binchk(flag))