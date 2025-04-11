from pyrogram import Client, filters
from _date import rexButton
from classBot.MongoDB import savedbuser

@rexButton('acepconde')
async def gaters(client, message):
    try:
        if message.from_user.id == message.message.reply_to_message.from_user.id:
            savedbuser(id=message.from_user.id,username=message.from_user.username,name=message.from_user.first_name)
            await message.edit_message_text("<b>Thanks Por preferirnos, Registro exitoso. ❇️</b>")
        else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")
    except: 
            savedbuser(id=message.from_user.id,username=message.from_user.username,name=message.from_user.first_name)
            await message.edit_message_text("<b>Thanks Por preferirnos, Registro exitoso. ❇️</b>")