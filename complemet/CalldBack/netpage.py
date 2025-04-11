from pyrogram import Client, filters
from Source_pack.BoutnAll import _cmdsbontTools
from Source_pack.TextAll import _toolsAll
from _date import rexButton

@rexButton('tolsa')
async def gaters(client, message):
    if message.from_user.id == message.message.reply_to_message.from_user.id : await message.edit_message_text(_toolsAll,reply_markup=_cmdsbontTools)
    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")