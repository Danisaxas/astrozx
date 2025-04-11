from pyrogram import Client, filters
from Source_pack.TextAll import _cmds ,_toolsAll
from Source_pack.BoutnAll import _cmdsbont
from _date import rexButton

@rexButton('rrtolls')
async def tools(client, message):
    if message.from_user.id == message.message.reply_to_message.from_user.id : await message.edit_message_text( _cmds, reply_markup= _cmdsbont)
    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")