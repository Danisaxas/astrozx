from pyrogram import Client, filters
from Source_pack.BoutnAll import idiomatra
from _date import rexButton
import requests

@rexButton('fr')
async def gaters(client, message):   
    co = 'fr'
    if message.from_user.id == message.message.reply_to_message.from_user.id :
        try:
            rrr = message.message.reply_to_message.reply_to_message.text
       
            if rrr:
                res =  requests.get(f'https://translate.google.com/'+
                                        f'translate_a/'+
                                        f't?client=dict-chrome-ex&sl=auto&'+
                                        f'tl={co}&q={rrr}&tbb=1&ie=UTF-8&oe=UTF-8')
                result = res.text.strip('[""]')[:-5]
                await message.edit_message_text(f'<code>{result}</code>',reply_markup=idiomatra)
        except:
            r = message.message.reply_to_message.text.split(" ",1)[1]
            res =  requests.get(f'https://translate.google.com/'+
                                    f'translate_a/'+
                                    f't?client=dict-chrome-ex&sl=auto&'+
                                    f'tl={co}&q={r}&tbb=1&ie=UTF-8&oe=UTF-8')
            result = res.text.strip('[""]')[:-5]
            await message.edit_message_text(f'<code>{result}</code>',reply_markup=idiomatra)
    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")
