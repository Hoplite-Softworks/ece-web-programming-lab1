import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

def PrintSomeHeaders(headersDict, someHeadersList):
    for h in someHeadersList:
        print("\n{}: {}\n".format(h, headersDict.get(h)))

url = input("\nInsert URL:\t") # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    '''# τύπωσε τον κώδικα html
    html = response.text
    more(html)'''
    # τύπωσε τους headers με τις τιμές τους
    PrintSomeHeaders(response.headers, ["Server","Cookie"])
