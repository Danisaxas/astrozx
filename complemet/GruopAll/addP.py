from _date import rex
from classBot.MongoDB import MondB
from Source_pack.TextAll import textaddp

@rex('addP')
async def addG(client,msg):
    if msg.from_user.id == 6411167257:
        idU = msg.text[len('/addp '): ]
        if not idU: return await msg.reply('<b> ₪ Input ⇝ <code>$id User_id</code></b>')
        if MondB(idchat=idU).queryUser() == None:
            await msg.reply(textaddp.format(idU))
            MondB(idchat=idU).savepremium()     
        else: await msg.reply('<b>_Message: <code>user ya aprovado.</code></b>')
    else: await msg.reply('<b>_Message: <code>Access Denied.❌</code></b>')
    