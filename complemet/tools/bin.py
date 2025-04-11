from _date import rex,bin_chk
from Source_pack.TextAll import _infochat,msgregist
from classBot.MongoDB import querygrup,queryUser

@rex(['bin','bins'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:
            try:
                bins = msg.text[len('/bin '): ]
                if not bins: return await msg.reply('<b> ₪ Input ⇝ <code>$bin 456789</code></b>')
                else:await msg.reply(bin_chk(bina=bins,chkby=msg.from_user.first_name))

            except:return await msg.reply('<b>BIN DEAD ❌</b>')