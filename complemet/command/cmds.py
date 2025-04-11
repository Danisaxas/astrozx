from _date import rex
from Source_pack.TextAll import _cmds ,_infochat,msgregist
from Source_pack.BoutnAll import _cmdsbont
from classBot.MongoDB import querygrup,queryUser,savedbuser

@rex(['cmd','cmds','xmds','help','ayuda','helps'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else: await client.send_message(msg.chat.id, _cmds, reply_markup= _cmdsbont, reply_to_message_id =msg.id)