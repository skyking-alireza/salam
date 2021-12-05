from bitcoinrpc.authproxy import AuthServiceProxy
rpc_connection = AuthServiceProxy("http://%s:%s@6.tcp.ngrok.io:17562"%('skyking@123', 'skyking@123'))
best_block_hash = rpc_connection.listtransactions()
print(best_block_hash)

