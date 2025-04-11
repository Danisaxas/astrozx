from _date import rex,skey
from Source_pack.TextAll import _infochat,msgregist
from classBot.MongoDB import querygrup,queryUser

@rex(['sk'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:
            sky = msg.text[len('/sk '): ]
            if not sky: return await msg.reply('<b> ₪ Input ⇝ <code>$sk sk_live+++</code></b>')

            headers={
            "Content-Type": "application/x-www-form-urlencoded"
            }

            data={
            "card[number]": 4543218722787334,
            "card[cvc]": 780,
            "card[exp_month]": 7,
            "card[exp_year]": 2026
            }
            await msg.reply(skey(
                data=data,
                headers=headers,
                key=sky,
                name=msg.from_user.first_name)
                )   