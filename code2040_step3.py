import json
import requests
#Documentation for 'requests': http://docs.python-requests.org/en/latest/

#searches for string in an array of strings
def needleInAHaystack(needle, haystack):
    for i in range(0,len(haystack)):
        if needle == haystack[i]:
            return i
    return -1 #return -1 if 'needle' never found in 'haystack'
                              
def main():

    url = "http://challenge.code2040.org/api/haystack"
    url2 = "http://challenge.code2040.org/api/haystack/validate"
    myToken = "6d4988504a8c2253612fad10082c099f"
    jsonData3 = {'token': myToken}
    req3 = requests.post(url, jsonData3)
    data = json.loads((req3.content))
    positionOfNeedle = needleInAHaystack(data['needle'],data['haystack'])
    jsonData3['needle'] = positionOfNeedle
    requests.post(url2,jsonData3)
    
main()
    
    

