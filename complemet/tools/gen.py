from _date import rex
from Source_pack.TextAll import _infochat,msgregist,gen
from Source_pack.BoutnAll import regene
from classBot.MongoDB import querygrup,queryUser
from classBot.genccs import cc_gen
import requests,re


@rex(['gen'])
async def chk(client,msg):
    if querygrup(msg.chat.id)==None:await msg.reply(_infochat)
    else:
        if queryUser(msg.from_user.id)==None:await msg.reply(msgregist)
        else:ccbin = msg.text[len('/gen '):]
        if not ccbin: return await msg.reply('<b> ₪ Input ⇝ <code>$gen 456789xxxxxx</code></b>')
        if len(str(ccbin)) < 6: return await msg.reply('<b>el bin es menos de 6 digitos | ingrese un bin.</b>')
        geneo = re.findall(r'[0-9]+',msg.text)
        if not geneo: return await msg.reply('<b>Ingrese el bin a generar | error de bin.</b>')

        binreq = requests.get(f'https://bins.antipublic.cc/bins/{ccbin}')
        if 'Invalid BIN' in binreq.text:return await msg.reply('<b>Status Dead ❌ | Invalid BIN.</b>')
        elif 'not found' in binreq.text:return await msg.reply('<b>Status Dead ❌ | not found</b>')
        else:

            if len(geneo) == 1:
                cc = geneo[0]
                mes = 'x'
                ano = 'x'
                cvv = 'x'
            elif len(geneo) ==2:
                if  int(geneo[1]) < 12:
                    cc = geneo[0]
                    mes = geneo[1]
                    ano = 'x'
                    cvv = 'x'
                else:
                    cc = geneo[0]
                    mes = 'x'
                    ano = 'x'
                    cvv = 'x'
            elif len(geneo) ==3:
                if  int(geneo[1]) < 12:
                    cc = geneo[0]
                    mes = geneo[1]
                    ano = 'x'
                    cvv = 'x'
                    if int(geneo[2]) in range(2023, 2032): 
                        cc = geneo[0]
                        mes = geneo[1]
                        ano = geneo[2]
                        cvv = 'x'
                    else:
                        cc = geneo[0]
                        mes = geneo[1]
                        ano = 'x'
                        cvv = 'x'
                else:
                    cc = geneo[0]
                    mes = geneo[1]
                    ano = 'x'
                    cvv = 'x'
                
            elif len(geneo) ==4:
                if  int(geneo[1]) < 12:
                    cc = geneo[0]
                    mes = geneo[1]
                    ano = 'x'
                    cvv = 'x'
                    if int(geneo[2]) in range(2023, 2032): 
                        cc = geneo[0]
                        mes = geneo[1]
                        ano = geneo[2]
                        cvv = 'x'
                        if int(geneo[3]) in range(000, 999):
                            cc = geneo[0]
                            mes = geneo[1]
                            ano = geneo[2]
                            cvv = geneo[3]
                        else:
                            cc = geneo[0]
                            mes = geneo[1]
                            ano = 'x'
                            cvv = 'x'

                    else:
                        cc = geneo[0]
                        mes = 'x'
                        ano = 'x'
                        cvv = 'x'
                else:
                    cc = geneo[0]
                    mes = geneo[1]
                    ano = geneo[2]
                    cvv = 'x'
            else:
                cc = geneo[0]
                mes = 'x'
                ano = 'x'
                cvv = 'x'

            cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10, = cc_gen(cc,mes,ano,cvv)
    
            ms = gen.format(cc1=cc1,cc2=cc2,cc3=cc3,cc4=cc4,cc5=cc5,cc6=cc6,cc7=cc7,cc8=cc8,cc9=cc9,cc10=cc10,binif=binreq.json()['bin'],country = binreq.json()['country'],country_name = binreq.json()['country_name'],country_flag = binreq.json()['country_flag'],name=msg.from_user.first_name)
            await msg.reply(ms,reply_markup=regene)
