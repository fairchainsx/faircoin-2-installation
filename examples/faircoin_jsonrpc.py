import sys
import requests
import json

URL = str('http://faircoin:mypassword@127.0.0.1:8332')

def jsonrpc(method, *params):
    try:
        headers = {'content-type': 'application/json'}
        payload = json.dumps({"id":"curltext", "method": method, 'params': params, 'jsonrpc': '2.0'})
        response = requests.post(URL, headers=headers, data=payload)
        return {'Status': "ok", "Data": (response.json()['result'])}
    except Exception as e:
        return {'Status': 'error', 'Data': e}

# a=jsonrpc('getblockcount')
a=jsonrpc('verifymessage', 'address','signature','message' )
print(a)
