from _date import rex
from classBot.MongoDB import MondB
from Source_pack.TextAll import textaddu

@rex('addU')
async def addG(client,msg):
    if msg.from_user.id == 6411167257:
        idU = msg.text[len('/addu '): ]
        if not idU: return await msg.reply('<b> ₪ Input ⇝ <code>$id User_id</code></b>')
        if MondB(idchat=idU).querygrup() == None:
            await msg.reply(textaddu.format(idU))
            MondB(idchat=int(idU),tipo='ChatType.PRIVATE').savedbgrup()
        else: await msg.reply('<b>_Message: <code>Grupo ya aprovado.</code></b>')
    else: await msg.reply('<b>_Message: <code>Access Denied.❌</code></b>')
    