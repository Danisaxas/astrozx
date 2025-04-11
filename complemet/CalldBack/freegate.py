from pyrogram import Client, filters
from Source_pack.BoutnAll import _cmdsretbontgates
from Source_pack.TextAll import _gatefree
from _date import rexButton


@rexButton('freegates')
async def freegates(client, message):
    if message.from_user.id == message.message.reply_to_message.from_user.id : await message.edit_message_text(_gatefree,reply_markup=_cmdsretbontgates)
    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")
