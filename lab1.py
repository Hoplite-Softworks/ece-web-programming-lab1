# ================================================== #
#
# Πρώτη Εργαστηριακή Άσκηση Προγραμματισμού Διαδικτύου (ECE_ΓΚ802)
# 
# 2023-2024
# ΛΕΥΤΕΡΗΣ ΓΚΛΙΑΤΗΣ
# Α.Μ. 1066548
#
#   Σε αρχείο python γράψτε κώδικα που:
#   -Ζητάει από τον χρήστη ένα URL,
#   -Πραγματοποιεί ένα αίτημα HTTP σε αυτό το URL,
#   -Τυπώνει τις κεφαλίδες (headers) της απόκρισης HTTP.
#   
#   Τροποποιήστε τον κώδικα ώστε να απαντάει για το URL που έδωσε ο χρήστης με τις εξής πληροφορίες:
#       -Ποιο είναι το λογισμικό που χρησιμοποιεί ο εξυπηρετητής (ο web server) για να απαντήσει στο αίτημα;
#       -Αν η σελίδα χρησιμοποιεί cookies, και αν ναι να τυπώνει το όνομα κάθε cookie και για πόσο διάστημα θα είναι έγκυρο.
#
# ================================================== #


import requests # εισαγωγή της βιβλιοθήκης

def PrintSomeHeaders(headersDict, someHeadersList):
    # για κάθε επιθυμητό header, αν είναι κενός set-cookie header ή οποιοσδήποτε άλλος header τύπωσε τις πληροφορίες του,
    # αλλιώς...
    for h in someHeadersList:
        headerValue = str(headersDict.get(h))
        if h=="Set-Cookie" and headerValue != "None":
            cookieElements = []
            cookieNameValue = []
            cookieExpiration = '-'
            # για κάθε στοιχείο του cookie, πρόσθεσέ το σε μια λίστα ανάλογα με τη μορφή του: 'όνομα=τιμή' ή 'όνομα' μόνο
            for e in headerValue.split(';'):
                try:
                    cookieElements.append([e.split('=',1)[0], e.split('=',1)[1]])
                    if cookieElements[-1][0] == " expires": cookieExpiration = cookieElements[-1][1]    # βρες την ημ. λήξης του cookie
                except:
                    cookieElements.append(e)
            
            cookieNameValue = cookieElements[0] # το πρώτο στοιχείο αφορά την ταυτότητα του cookie
            print("Set-Cookie:\n\tname, value:\t{}, {}\n\texpires:\t{}\n".format(cookieNameValue[0], cookieNameValue[1], cookieExpiration))
        else:
            # για κενό set-cookies ή για οποιοσδήποτε άλλον header, τύπωσε το όνομα και την τιμή του
            print("{}: {}\n".format(h, headerValue))


url = input("\nInsert URL:\t")  # προσδιορισμός του url

# αν το url δεν περιέχει http/https, βγάλε σφάλμα
# χωρίς αυτό, θα το κάνει από μόνη της η κλήση της requests.get() παρακάτω
if url.startswith("http://") or url.startswith("https://"):
    pass
else:
    print("WARNING! NO HTTP/HTTPS SCHEME DETECTED IN URL.\nEXITING...")
    exit()

with requests.get(url) as response:  # το αντικείμενο response
    #print(response.headers)    # τύπωσε τους όλους τους headers με τις τιμές τους
    PrintSomeHeaders(response.headers, ["Server","Set-Cookie"])
