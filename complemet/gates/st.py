
from _date import rex, atspam
import requests
import time
from Source_pack.TextAll import _infochat, msgregist
from Source_pack.BoutnAll import binchk
from classBot.MongoDB import querygrup, queryUser


@rex(['st'])
@atspam
async def chk(client, msg):
    try:
        if queryUser(msg.from_user.id)['plan'] == 'premium' or queryUser(msg.from_user.id)['plan'] == 'owner':
            msgs = await msg.reply('<b><i>Checkings..</i></b>')
            if (msg.chat.id) == None:
                await msg.reply(_infochat)
            else:
                if queryUser(msg.from_user.id) == None:
                    await msg.reply(msgregist)
                else:
                    ccs = msg.text[len('/st '):]
                    if not ccs:
                        return await msgs.edit_text('<b> ₪ Input ⇝ <code>$chk ccs</code></b>')

                    else:
                        ccs = ccs.split('|')
                        req = requests.get(
                            f'https://bins.antipublic.cc/bins/{ccs[0]}')
                        flag = req.json()['country_flag']
                        tarjeta = ccs[0]+"|"+ccs[1]+"|"+ccs[2]+"|"+ccs[3]
                        resp = (ccs[0], ccs[1], ccs[2], ccs[3])
                        print(resp)
                        msg1 = await msgs.edit_text('<b><i>Checkings 100%.</i></b>')
                        time.sleep(1)
                        text = """<b>₪ Gate | Shopify 

₪ cc  ⇝ <code>{}</code>
₪ response  ⇝ {}
₪ code  ⇝ <code>{}</code>
₪ Name ⇝ Shofia
-
₪ From ⇝ <code>{}</code>
₪ Access Owner ⇝ <code> 𝗺𝗮𝘅 ريكس 🇮🇳</code></b>"""

                        if 'Security code was not matched by the processor' == resp:
                            await msg1.edit_text(text.format(tarjeta, resp, 'Approved [CCN] ✅', msg.from_user.id), reply_markup=binchk(flag))
                        elif 'Street address and postal code do not match' == resp:
                            await msg1.edit_text(text.format(tarjeta, resp, 'approved ✅', msg.from_user.id), reply_markup=binchk(flag))
                        elif 'No Match' == resp:
                            await msg1.edit_text(text.format(tarjeta, resp, 'approved ✅', msg.from_user.id), reply_markup=binchk(flag))
                        elif 'Charged' == resp:
                            await msg1.edit_text(text.format(tarjeta, resp, 'Charged ✅', msg.from_user.id), reply_markup=binchk(flag))
                        else:
                            await msg1.edit_text(text.format(tarjeta, resp, 'DECLINED ❌'), reply_markup=binchk(flag))

        else:
            await msg.reply('<b>₪ Access Denied - <code>Free User ❌</code></b>')
    except:
        await msg.reply('<b>Para continuar porfavor usa el comando de registros /regist</b>')
