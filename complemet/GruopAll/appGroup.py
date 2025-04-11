from _date import rex
from classBot.MongoDB import MondB
from Source_pack.TextAll import textaddg


@rex('addG')
async def addG(client,msg):
    if msg.from_user.id == 6411167257:
        if MondB(idchat=msg.chat.id,tipo=f'{msg.chat.type}').querygrup() == None:
            await msg.reply(textaddg.format(msg.chat.id,msg.chat.title,msg.chat.username,msg.chat.type))
            MondB(idchat=msg.chat.id,tipo=f'{msg.chat.type}',).savedbgrup()
        else: await msg.reply('<b>_Message: <code>Grupo ya aprovado.</code></b>')
    else: await msg.reply('<b>_Message: <code>Access Denied.❌</code></b>')