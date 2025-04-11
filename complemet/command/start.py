from _date import rex,video
from Source_pack.TextAll import _strat, _infochat,msgregist
from Source_pack.BoutnAll import _startbont
from classBot.MongoDB import querygrup,queryUser,savedbuser

@rex(['start','star'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:
        await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:
            await msg.reply(msgregist)
        else:
            await client.send_video(chat_id=msg.chat.id, caption=_strat.format(msg.from_user.first_name,msg.from_user.id),video=video,reply_markup=_startbont)