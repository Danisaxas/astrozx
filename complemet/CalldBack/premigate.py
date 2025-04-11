from pyrogram import Client, filters
from Source_pack.BoutnAll import _cmdsretbontgates
from Source_pack.TextAll import _gatepremm
from _date import rexButton

@rexButton('premiumgates')
async def premiumgates(client, message):
    if message.from_user.id == message.message.reply_to_message.from_user.id :await message.edit_message_text(_gatepremm,reply_markup=_cmdsretbontgates)
    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")