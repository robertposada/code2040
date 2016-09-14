import json
import requests
#Documentation for 'requests': http://docs.python-requests.org/en/latest/

def main():
    
    myToken = "6d4988504a8c2253612fad10082c099f"
    githubURL = "https://github.com/robertposada/code2040"
    url = "http://challenge.code2040.org/api/register"
    jsonData = {'token':myToken,'github': githubURL}
    requests.post(url,jsonData)
    
main()
    
    

