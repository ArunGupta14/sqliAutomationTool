'''Find sql automation tool '''

import requests
import time

def sqli_check(url):
    cmt = b'SQL syntax'
    payload = "'"
    resp = requests.get(f"{url}+{payload}")
    if (cmt in resp.content) or (b'sql' in resp.content):
        print('>>>[sql vulnerability] ',url)

with open("file1.txt","r")as f:

    print("Checking site is validity and sqli vulnerability.",'\nPlease wait...')

    time.sleep(1)
    for line in f:
        try:        
            url = line.strip()
            res = requests.head(f'{url}')
            print(f'[site: {url}][status:{res.status_code},{res.reason}]')
            if res.status_code == 200:
                sqli_check(url)
        except FileNotFoundError:
            print("file not found")
        except requests.exceptions.MissingSchema:
            continue
        except requests.ConnectionError:
            print('Connection Error')
        except KeyboardInterrupt:
            print('exit')

    
        

    
        