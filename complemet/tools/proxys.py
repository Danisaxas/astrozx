from _date import rex

@rex('txt')
async def addG(client,msg):
    if msg.from_user.id == 6411167257:
        text = await client.download_media(msg.reply_to_message.document.file_id)
        with open(text, "r") as file:
            ccs = file.read()

        await msg.reply(ccs)