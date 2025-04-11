from _date import rex
from Source_pack.TextAll import _infochat,msgregist
from classBot.MongoDB import querygrup,queryUser
import requests

@rex(['ich','idh','chatid','chat','infochat','idk','infochat','idc'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:await msg.reply(msg.chat.id)