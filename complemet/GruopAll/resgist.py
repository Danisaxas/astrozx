from _date import rex
from Source_pack.BoutnAll import _registerDb
from Source_pack.TextAll import  _infochat, regett
from classBot.MongoDB import querygrup,queryUser

@rex('regist')
async def addG(client,msg):
    if querygrup(msg.chat.id)==None:
        await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:
            await msg.reply(regett.format(msg.from_user.id,msg.from_user.username,msg.from_user.first_name),reply_markup=_registerDb)
        else:await msg.reply('<b>Ya estas registrado.</b>')