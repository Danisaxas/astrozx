from pyrogram import Client, filters
from _date import rexButton

@rexButton('closed')
async def gaters(client, message):   
    if message.from_user.id == message.message.reply_to_message.from_user.id : await message.edit_message_text("<b>‼️ Fin closed. ‼️</b>")
    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")
