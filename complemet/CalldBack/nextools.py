from pyrogram import Client, filters
from Source_pack.BoutnAll import _cmdsretbontgat
from Source_pack.TextAll import _nettoolst
from _date import rexButton

@rexButton('nettools')
async def gaters(client, message):
    if message.from_user.id == message.message.reply_to_message.from_user.id :await message.edit_message_text(_nettoolst,reply_markup=_cmdsretbontgat)
    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")
