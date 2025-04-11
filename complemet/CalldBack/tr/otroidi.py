from pyrogram import Client, filters
from Source_pack.BoutnAll import selecidioma
from _date import rexButton
import requests

@rexButton('otroidi')
async def gaters(client, message):   
    if message.from_user.id == message.message.reply_to_message.from_user.id :await message.edit_message_text('<b>Seleciona un idioma</b>',reply_markup=selecidioma)
    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")