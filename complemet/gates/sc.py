from _date import rex,atspam
import requests,time
from Source_pack.TextAll import _infochat,msgregist
from Source_pack.BoutnAll import binchk
from classBot.MongoDB import querygrup,queryUser
from def_gates.def_sc import shp,response_sh


@rex(['sc'])
@atspam
async def chk(client,msg):
    try:
        if queryUser(msg.from_user.id)['plan'] == 'premium' or queryUser(msg.from_user.id)['plan'] == 'owner':
            msgs = await msg.reply('<b><i>Checkings..</i></b>')       
            if (msg.chat.id)==None:await msg.reply(_infochat)
            else:
                if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
                else:
                    ccs = msg.text[len('/sc '): ]
                    if not ccs:return await msgs.edit_text('<b> ₪ Input ⇝ <code>$chk ccs</code></b>')

                    else:
                        ccs= ccs.split('|')

                        req = requests.get(f'https://bins.antipublic.cc/bins/{ccs[0]}')
                        
                        flag = req.json()['country_flag']
                        tarjeta = ccs[0]+"|"+ccs[1]+"|"+ccs[2]+"|"+ccs[3]
                        result = await shp(tarjeta)
                        status_ = await response_sh(result)
                        msg1 = await msgs.edit_text('<b><i>Checkings 100%.</i></b>')
                        time.sleep(1)
                        text = """<b>₪ Gate | Shopify + Cyber

₪ cc  ⇝ <code>{}</code>
₪ code  ⇝ <code>{}</code>
₪ response  ⇝ {}
₪ Name ⇝ Shofia
-
₪ From ⇝ <code>{}</code>
₪ Access Owner ⇝ <code> 𝗺𝗮𝘅 ريكس 🇮🇳</code></b>"""
                        await msg1.edit_text(text.format(
                                                        f'{ccs[0]}|{ccs[1]}|{ccs[2]}|{ccs[3]}',
                                                        status_,
                                                        result,
                                                        msg.from_user.id 
                                                            ),reply_markup=binchk(flag))
        else:await msg.reply('<b>₪ Access Denied - <code>Free User ❌</code></b>')
    except:await msg.reply('<b>Para continuar porfavor usa el comando de registros /regist</b>')