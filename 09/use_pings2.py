import ping3
ping3.EXCEPTIONS = True	#EXCEPTIONSモード例外を投げる
#Pingに応答がなかった時に例外を投げるようになる

target_ip = "127.0.0.1"
# target_ip = "192.168.8.109"
try:                                                         
    result = ping3.ping(target_ip, timeout = 0.5, unit ='ms', ttl = 64) 
except ping3.errors.Timeout:
    print(f"Host : {target_ip} is NOT reachable (Timeout)")
except ping3.errors.TimeToLiveExpired:
    print(f"Host : {target_ip} is NOT reachable (TTL)")
except ping3.errors.PingError:
    print(f"Host : {target_ip} is NOT reachable (Error)"  )
else:
    print(f"Host : {target_ip} is reachable:{result}(ms)")