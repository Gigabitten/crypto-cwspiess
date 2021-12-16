#!/usr/bin/env python

# pip install requests

import requests
import json
import configparser
import pathlib
import time
from pathlib import Path

def getConfig(file=None):
    if (file == None):
        file = str(pathlib.Path.home() / ".bitcoin" / "bitcoin.conf")

    fd = open(file,"r")
    data = fd.read()
    fd.close()

    config=configparser.ConfigParser()
    config.read_string(f"""
    [default]
    {data}
    """)

    return config['default']

config=getConfig()

testnet=int(config.get('testnet',0))
user=str(config.get('rpcuser',''))
password=str(config.get('rpcpassword',''))
port=int(config.get('port',8332 if not testnet else 18332))

url = f"http://localhost:{port}/"

def rpcCall(method, params = []):
    payload = {
        "version" : "1.1",
        "method": method,
        "params": params,
        "id": 0,
    }
    return requests.post(url, json=payload, auth=(user,password)).json()

# very useful for figuring out what's going on
# but not used in the actual program
def jsonPrint(js):
    print(json.dumps(js, indent=4))

# overall program prints all past balances, essentially a transaction history
runningBal = rpcCall("getbalance")["result"]
transactions = rpcCall("listtransactions")["result"]
diffs = []
for transaction in reversed(transactions):
    amount = transaction["amount"]
    if("fee" in transaction):
        amount += transaction["fee"]
    runningBal -= amount
    print(f"Balance changed by {amount}")
    print(f"New balance: {runningBal}\n")
