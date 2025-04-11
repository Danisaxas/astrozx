from _date import rex,bin_chk
from Source_pack.TextAll import _infochat,msgregist,info
from Source_pack.BoutnAll import _infouser
from classBot.MongoDB import querygrup,queryUser
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os


@rex(['me','info','yo','perfil','status','estatus','id'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:
            user_id = msg.from_user.id
            foto = await client.download_media(msg.from_user.photo.big_file_id)
            ms = info.format(
                            msg.from_user.first_name,
                            msg.from_user.id,
                            msg.from_user.username,
                            msg.chat.id)
 
            await msg.reply_photo(caption=ms,photo=foto,reply_markup=_infouser(msg.from_user.first_name,msg.from_user.username))
            os.remove(foto)


