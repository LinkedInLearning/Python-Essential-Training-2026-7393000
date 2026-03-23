import ping3
ping3.EXCEPTIONS = True

target_ip = "127.0.0.1"
# target_ip = "192.168.8.109"
try:
    result = ping3.ping(target_ip, timeout = 0.5, unit ='ms', ttl = 64) 
    print(f'Host : {target_ip} is reachable : {result}(ms)')
except Exception as e:
    print(e)
