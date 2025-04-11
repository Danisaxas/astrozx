from _date import rex,bin_chk
from Source_pack.TextAll import _infochat,msgregist,iptext
from Source_pack.BoutnAll import selecidioma
from classBot.MongoDB import querygrup,queryUser
import requests

@rex(['tr'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:
            try:
                if msg.reply_to_message.text:await msg.reply('<b>Seleciona un idioma</b>',reply_markup=selecidioma)
            except:
                tr = msg.text[len('/tr '): ]
                if not tr: return await msg.reply('<b> ₪ Input ⇝ <code>$tr texto </code></b>')
                else: await msg.reply('<b>Seleciona un idioma</b>',reply_markup=selecidioma)