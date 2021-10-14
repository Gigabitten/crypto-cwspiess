from bitcoin.rpc import RawProxy

url=None
port=18332 # testnet, use None for main net client
conf="/home/caleb/.bitcoin/bitcoin.conf"

proxy = RawProxy(url,port,conf)

txid="17560751529ee048af00e4f0fdd7d20104275f7d731e66a4e0220ae738b8e337"
info = proxy.getrawtransaction(txid)
print(info)
print()
info = proxy.decoderawtransaction(info)
print(info)
