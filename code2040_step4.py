import json
import requests
#Documentation for 'requests': http://docs.python-requests.org/en/latest/

def excludePrefixedWords(prefix, array):
    newArray = []
    prefixLength = len(prefix)
    for i in range(0,len(array)):
        if prefix != array[i][0:prefixLength]:
            newArray.append(array[i].encode("ascii"))
    return newArray
                              
def main():

    myToken = "6d4988504a8c2253612fad10082c099f"
    url = "http://challenge.code2040.org/api/prefix"
    url2 = "http://challenge.code2040.org/api/prefix/validate"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    jsonData4 = {'token':myToken}
    req4 = requests.post(url, jsonData4)
    prefixDictionary = json.loads(req4.content) 
    noPrefixArray = excludePrefixedWords(prefixDictionary['prefix'],prefixDictionary['array'])
    jsonData4['array'] = noPrefixArray
    jsonData4 = json.dumps(jsonData4)
    requests.post(url2,jsonData4,headers = headers)
    
main()
    
    

