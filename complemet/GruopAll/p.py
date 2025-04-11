from _date import rex

@rex('p')
async def addG(client,msg):
    if msg.from_user.id == 6411167257:await msg.reply(f'<code>{msg.reply_to_message.from_user.id}</code>')