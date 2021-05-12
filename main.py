import os, threading
import time
import urllib3
import requests

def title():
    while True:
        os.system(f"title Proxy Checker - Proxy Count: [{count}] Valid : [{valid}]  Invalid : [{invalid}]")
        if count == valid+invalid and count != 0:
            print('\n > finished')
            exit()

def check_proxy(proxy):  
    global valid
    global invalid
    try:
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        session.max_redirects = 300
        proxy = proxy.split('\n',1)[0]
        session.get(test_url, proxies={proxytype: proxytype + '://' + proxy}, timeout=timeout, allow_redirects=True)
    except requests.exceptions.ConnectionError as e:
        invalid += 1
        return 0
    except requests.exceptions.ConnectTimeout as e:
        invalid += 1
        return 0
    except requests.exceptions.HTTPError as e:
        invalid += 1
        return 0
    except requests.exceptions.Timeout as e:
        invalid += 1
        return 0
    except urllib3.exceptions.ProxySchemeUnknown as e:
        invalid += 1
        return 0
    except requests.exceptions.TooManyRedirects as e:
        invalid += 1
        return 0
    print("Valid Proxy: " + proxy)
    valid += 1
    f = open("valids.txt", "a")
    f.write(proxy+'\n')
    f.close()
    return 1

valid = 0
invalid = 0
count = 0
test_url = "http://google.com"
timeout = (3.05,27)

threading.Thread(target = title).start()
threadcount = int(input(" > number of threads\n > "))
filename = input(" > filename\n > ").lower()
proxytype = input(" > http or https\n > ").lower()

proxies = open(filename).read().splitlines()    
count = len(proxies)
for proxy in proxies:
    threading.Thread(target=check_proxy, args=(proxy.strip(), )).start()
    time.sleep(0.1)