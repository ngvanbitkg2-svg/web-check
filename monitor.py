import requests
from curl_cffi import requests as cur_requests
import time
import os

URL = "https://iloto88.info/UserService.aspx"
PROXY_API = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all"

def get_proxies():
    try:
        r = requests.get(PROXY_API, timeout=10)
        return r.text.splitlines() if r.status_code == 200 else []
    except:
        return []

def run():
    proxies = get_proxies()
    print(f"Bắt đầu với {len(proxies)} proxies.")
    
    for p_addr in proxies[:20]: # GitHub Actions chạy có giới hạn, nên thử 20 proxy mỗi lần
        start = time.perf_counter()
        try:
            proxy = {"http": f"http://{p_addr}", "https": f"http://{p_addr}"}
            resp = cur_requests.post(URL, proxies=proxy, impersonate="chrome110", timeout=10)
            latency = (time.perf_counter() - start) * 1000
            print(f"[Proxy {p_addr}] Status: {resp.status_code} | Speed: {latency:.0f}ms")
        except:
            continue

if __name__ == "__main__":
    run()
