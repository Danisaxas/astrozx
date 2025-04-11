from _date import rexButton
import requests

@rexButton('binchk')
async def gaters(client, message):   
    if message.from_user.id == message.message.reply_to_message.from_user.id :
        
        ccs = message.message.reply_to_message.text.split(' ')[1]
        tt = message.message.text.split('\n')
        req = requests.get(f'https://bins.antipublic.cc/bins/{ccs}')
    
        text = f"""<b>₪ Gate | Stripe charged

₪ cc  ⇝ <code>{ccs}</code>
{tt[3]}
{tt[4]}
₪ Name ⇝ dRgoodulino
-
₪ bin ⇝ <code>{req.json()['bin']}</code>
₪ brand ⇝ {req.json()['brand']}
₪ country ⇝ {req.json()['country_name']} | {req.json()['country']} | {req.json()['country_flag']}
-
₪ info ⇝ {req.json()['level']} | {req.json()['bank']}
₪ bank ⇝ <code>{req.json()['type']}</code>
-
{tt[7]}
₪ Access Owner ⇝ <code> 𝗺𝗮𝘅 ريكس 🇮🇳</code></b>"""
        await message.edit_message_text(text)

    else:await message.answer(f"‼️ Access denied is for: {message.message.reply_to_message.from_user.first_name} ‼️")