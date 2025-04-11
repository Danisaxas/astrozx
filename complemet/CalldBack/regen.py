from pyrogram import Client, filters
from _date import rexButton
from _date import rex
from Source_pack.TextAll import _infochat,msgregist,gen
from Source_pack.BoutnAll import regene
from classBot.MongoDB import querygrup,queryUser
from classBot.genccs import cc_gen
import requests,re




@rexButton('regen')
async def gaters(client, msg):   
    if msg.from_user.id == msg.message.reply_to_message.from_user.id :
        men = msg.message.reply_to_message.text
        geneoa= men.split()[1]

        binreq = requests.get(f'https://bins.antipublic.cc/bins/{geneoa}')
        geneo = re.findall(r'[0-9]+',geneoa)
        if len(geneo) == 1:
            cc = geneo[0]
            mes = 'x'
            ano = 'x'
            cvv = 'x'
        elif len(geneo) ==2:
            cc = geneo[0]
            mes = geneo[1]
            ano = 'x'
            cvv = 'x'
        elif len(geneo) ==3:
            cc = geneo[0]
            mes = geneo[1]
            ano = geneo[2]
            cvv = 'x'
        elif len(geneo) ==4:
            cc = geneo[0]
            mes = geneo[1]
            ano = geneo[2]
            cvv = geneo[3]
        else:
            cc = geneo[0]
            mes = geneo[1]
            ano = geneo[2]
            cvv = geneo[3]

        cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10, = cc_gen(cc,mes,ano,cvv)

        ms = gen.format(cc1=cc1,cc2=cc2,cc3=cc3,cc4=cc4,cc5=cc5,cc6=cc6,cc7=cc7,cc8=cc8,cc9=cc9,cc10=cc10,binif=binreq.json()['bin'],country = binreq.json()['country'],country_name = binreq.json()['country_name'],country_flag = binreq.json()['country_flag'],name=msg.from_user.first_name)
        await msg.edit_message_text(ms,reply_markup=regene)

    else:await msg.answer(f"‼️ Access denied is for: {msg.message.reply_to_message.from_user.first_name} ‼️")
