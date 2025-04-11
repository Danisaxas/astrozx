from pyrogram import Client, filters
from Source_pack.BoutnAll import _cmdsbontGater
from _date import rexButton
from Source_pack.TextAll import _gaterwa

@rexButton('gatesa')
async def gaters(client, message):
    if message.from_user.id == message.message.reply_to_message.from_user.id :await message.edit_message_text(_gaterwa,reply_markup=_cmdsbontGater)
    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")