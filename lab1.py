import requests # εισαγωγή της βιβλιοθήκης

def PrintSomeHeaders(headersDict, someHeadersList):
    for h in someHeadersList:
        print("\n{}: {}\n".format(h, headersDict.get(h)))

url = input("\nInsert URL:\t")  # προσδιορισμός του url
if ("http://" not in url) and ("https://" not in url):
    print("WARNING! NO HTTP/HTTPS DETECTED IN URL.\nEXITING...")
    exit()

with requests.get(url) as response:  # το αντικείμενο response
    #print(response.headers)    # τύπωσε τους όλους τους headers με τις τιμές τους
    PrintSomeHeaders(response.headers, ["Server","Set-Cookie"])
