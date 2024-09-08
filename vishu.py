import os
import requests
import re
import time
import datetime
from itertools import cycle
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor
psl = lambda command: os.system(command)  # Alias for system command
psl('rm -rf filer.txt')
idd = []

logo =  """\033[1;39;40m     

                                                                                                                                                
\033[1;38;40m-----------------------------------------------
\033[1;38;40m M9D3 BY  : : 4BH4Y KUM4R
\033[1;38;40m IF YOU'RE BAD THEN I'M YOUR DAD
\033[1;38;40m-----------------------------------------------"""

psl('rm -rf filer.txt')
idd = []
def send_messages_indefinitely(coki, lnk, delay, hater, file_contents):
    while True:
        for msgs in file_contents:
            send_message(coki, lnk, delay, hater, msgs)
            time.sleep(delay)
def clear_screen():
    os.system('clear')  # Use appropriate clear command for your system
            
def main():
    clear_screen()
    print(logo)
    print('-------------------------------------------')
    print('\x1b[1;97m  Put >>  Cookie Text File, Delay, Chat/Inbox Link id, Hater Name, File ')
    print('-------------------------------------------')
    
    cookies_filename = input(' [+] Cookies Text File: ')
    coki_list = read_cookies(cookies_filename)
    accounts = len(coki_list)
    
    if accounts == 0:
        print('No cookies found in the file.')
        os.sys.exit()
    
    delay = int(input(' [+] Delay : '))
    print('-------------------------------------------')
    lnk = input(' [+] Chat/Inbox Link id : ')
    print('-------------------------------------------')
    hater = input(' [+] Haters Name : ')
    print('-------------------------------------------')
    filee = input(' [+] Message File : ')
    file_contents = read_file(filee)
    
    with ThreadPoolExecutor(max_workers=accounts) as executor:
    	
        print(logo)
        clear_screen()
        print('')
        print(f' [+] Total messages : {len(file_contents)}')
        print(' [+] Your Process Started in Background')
        print('-------------------------------------------')
        
        for coki in coki_list:
            executor.submit(send_messages_indefinitely, coki, lnk, delay, hater, file_contents)

def read_cookies(filename):
    with open(filename, 'r') as cookies_file:
        return cookies_file.read().strip().split('\n')

def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()



def send_message(coki, lnk, delay, hater, msgs):
    try:
        time.sleep(delay)
        current_time = datetime.datetime.now()
        tim, _ = str(current_time).split('.')
        today = datetime.date.today()
        year, month, day = str(today).split('-')
        cookies = {'cookie': coki}
        g_url = 'https://d.facebook.com/messages/read/?tid=' + lnk
        g_headers = {
                    'authority': 'd.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'referer': 'https://d.facebook.com/messages/read/?tid=' + lnk,
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                    'sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"11.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
                }
        res1 = requests.get(url=g_url, cookies=cookies, headers=g_headers).text
        
        # Specify the HTML parser when creating the BeautifulSoup object
        soup = sop(res1, 'html.parser')  # Use the 'html.parser' parser
        
        j2 = soup.find('input', {'name': 'jazoest'})['value']
        fb_dtsg = soup.find('input', {'name': 'fb_dtsg'})['value']
        csid = soup.find('input', {'name': 'csid'})['value']
        tids = soup.find('input', {'name': 'tids'})['value']
        
        ses = requests.Session()  # Create a session object
        
        ses.headers.update({
            'content-type': 'application/x-www-form-urlencoded',
        })

        rose = soup.find('form', method='post')['action']
        payload = {
            'fb_dtsg': fb_dtsg,
            'jazoest': j2,
            'body': hater + ' ' + str(msgs),
            'send': 'Send',
            'tids': tids,
            'wwwupp': 'C3',
            'platform_xmd': '',
            'referrer': '',
            'ctype': '',
            'cver': 'legacy',
            'csid': csid
        }
        host = 'https://d.facebook.com'
        post = ses.post(url=host + rose, data=payload, cookies=cookies).text
        print(f' [+] Time: {tim}')
        print(f' [+] Date: {day}/{month}/{year}')
        print(f' [+] Haterz: {hater}')
        print(f' [+] Message: {hater + msgs}')
        print('-------------------------------------------')
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
