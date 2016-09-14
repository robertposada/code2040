import json
import requests
#Documentation for 'requests': http://docs.python-requests.org/en/latest/

def reverseString(s):
    reversedString = ""
    for i in range(len(s)-1,-1,-1):
        reversedString = reversedString + s[i]

    return reversedString
                             
def main():

    url = "http://challenge.code2040.org/api/reverse"
    url2 = "http://challenge.code2040.org/api/reverse/validate"
    myToken = "6d4988504a8c2253612fad10082c099f"
    jsonData2 = {'token' : myToken}
    req2 = requests.post(url, jsonData2)
    newString = reverseString(req2.text)
    jsonData2['string'] = newString
    requests.post(url2, jsonData2)

main()
    
