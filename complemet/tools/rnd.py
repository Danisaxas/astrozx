from _date import rex,bin_chk
from Source_pack.TextAll import _infochat,msgregist,nrdtext
from classBot.MongoDB import querygrup,queryUser
import requests

@rex(['rnd'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:
            rnd = msg.text[len('/rnd '): ]
            if not rnd: return await msg.reply('<b> ₪ Input ⇝ <code>$rnd mx</code></b>')
            req = requests.get(f'https://randomuser.me/api/?nat={rnd}')
            if 'results' in req.text:
                    r = req.json()['results'][0]
                    genero = r['gender']
                    mr = r['name']['title']
                    first = r['name']['first']
                    last = r['name']['last']
                    mail = r['email']
                    location = r['location']
                    ciudad = location['city']
                    state = location['state']
                    country = location['country']
                    zip = location['postcode']
                    foto = r['picture']['large']
                    ms1 = nrdtext.format(genero,mr,first,last,mail,ciudad,state,country,zip,msg.from_user.first_name)
                    await client.send_photo(msg.chat.id,foto, ms1)
